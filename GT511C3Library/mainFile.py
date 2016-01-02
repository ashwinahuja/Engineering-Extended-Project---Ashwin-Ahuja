'''
Ashwin Ahuja - ashhwin.ahuja@gmail.com
December 2015
This code is published under the MIT License, please look at the main folder for more information
This code makes use of the module obtained from SparkFun - the GT511C3 - and makes lots of use of the
library for arduino provided by them - hence, please look at this.
This code has been tested on a Raspberry Pi 2 B, however, will in finality be used with a Raspberry Pi
Zero, so code has been designed to work with both of these.

This inherits majorly from Jean Machuca's attempts to do the same - please look at his library as well

'''

'''
Connections are as follows:

FP (Fingerprint Sensor) TX - RXD of Raspberry Pi GPIO
FP (Fingerprint Sensor) RX - TXD of Raspberry Pi GPIO
VCC of Fingerprint Sensor  - 3V3 of Raspberry Pi GPIO
GND of Fingerprint Sensor  - GND of Raspberry Pi GPIO

'''

import os
import serial
import time
import binascii

def delay(milliseconds):
    #allows me to maximise the code that can be lifted directly from the sparkfun library
    time.sleep(milliseconds)

deviceName = '/dev/cu.usbserial-A601EQ14' #this is the Pi Serial Connection

class packet:
    byte1 = 0x55;
    byte2 = 0xAA;
    bytedevid1 = 0x01;
    bytedevid2 = 0x00;
    
    def returnHighByte(self, word):
        return (w>>8)&0x00FF
    def returnLowByte (self, word):
        return w&0x00FF
    def CalculateCheckSum(self,bytearr):
        return sum(map(ord,bytes(bytearr)))
    
    def serializeToSend(self,bytearr):
        return ' '.join(binascii.hexlify(ch) for ch in bytes(bytearr))
class commandpacket(packet):
    cmd = ''
    command = bytearray(2)
    commands = {
                    'NotSet'                  : 0x00,        # Default value for enum. Scanner will return error if sent this.
                    'Open'                    : 0x01,        # Open Initialization
                    'Close'                   : 0x02,        # Close Termination
                    'UsbInternalCheck'        : 0x03,        # UsbInternalCheck Check if the connected USB device is valid
                    'ChangeBaudrate'          : 0x04,        # ChangeBaudrate Change UART baud rate
                    'SetIAPMode'              : 0x05,        # SetIAPMode Enter IAP Mode In this mode, FW Upgrade is available
                    'CmosLed'                 : 0x12,        # CmosLed Control CMOS LED
                    'GetEnrollCount'          : 0x20,        # Get enrolled fingerprint count
                    'CheckEnrolled'           : 0x21,        # Check whether the specified ID is already enrolled
                    'EnrollStart'             : 0x22,        # Start an enrollment
                    'Enroll1'                 : 0x23,        # Make 1st template for an enrollment
                    'Enroll2'                 : 0x24,        # Make 2nd template for an enrollment
                    'Enroll3'                 : 0x25,        # Make 3rd template for an enrollment, merge three templates into one template, save merged template to the database
                    'IsPressFinger'           : 0x26,        # Check if a finger is placed on the sensor
                    'DeleteID'                : 0x40,        # Delete the fingerprint with the specified ID
                    'DeleteAll'               : 0x41,        # Delete all fingerprints from the database
                    'Verify1_1'               : 0x50,        # Verification of the capture fingerprint image with the specified ID
                    'Identify1_N'             : 0x51,        # Identification of the capture fingerprint image with the database
                    'VerifyTemplate1_1'       : 0x52,        # Verification of a fingerprint template with the specified ID
                    'IdentifyTemplate1_N'     : 0x53,        # Identification of a fingerprint template with the database
                    'CaptureFinger'           : 0x60,        # Capture a fingerprint image(256x256) from the sensor
                    'MakeTemplate'            : 0x61,        # Make template for transmission
                    'GetImage'                : 0x62,        # Download the captured fingerprint image(256x256)
                    'GetRawImage'             : 0x63,        # Capture & Download raw fingerprint image(320x240)
                    'GetTemplate'             : 0x70,        # Download the template of the specified ID
                    'SetTemplate'             : 0x71,        # Upload the template of the specified ID
                    'GetDatabaseStart'        : 0x72,        # Start database download, obsolete
                    'GetDatabaseEnd'          : 0x73,        # End database download, obsolete
                    'UpgradeFirmware'         : 0x80,        # Not supported
                    'UpgradeISOCDImage'       : 0x81,        # Not supported
                    'Ack'                     : 0x30,        # Acknowledge.
                    'Nack'                    : 0x31         # Non-acknowledge
                }

    def __init__(self,*args,**kwargs):
            commandName=args[0]
            kwargs.setdefault('UseSerialDebug', True)
            self.UseSerialDebug= kwargs['UseSerialDebug']
            if self.UseSerialDebug:
                print 'Command: %s' % commandName
            self.cmd = self.commands[commandName]
            
    UseSerialDebug = True
    Parameter = bytearray(4)
        
    def GetPacketBytes(self):
        self.command[0] = self.GetLowByte(self.cmd)
        self.command[1] = self.GetHighByte(self.cmd)
        
        packetbytes= bytearray(12)
        packetbytes[0] = self.COMMAND_START_CODE_1
        packetbytes[1] = self.COMMAND_START_CODE_2
        packetbytes[2] = self.COMMAND_DEVICE_ID_1
        packetbytes[3] = self.COMMAND_DEVICE_ID_2
        packetbytes[4] = self.Parameter[0]
        packetbytes[5] = self.Parameter[1]
        packetbytes[6] = self.Parameter[2]
        packetbytes[7] = self.Parameter[3]
        packetbytes[8] = self.command[0]
        packetbytes[9] = self.command[1]
        chksum = self.CalculateCheckSum(packetbytes[0:9])
        packetbytes[10] = self.GetLowByte(chksum)
        packetbytes[11] = self.GetHighByte(chksum)

        return packetbytes;

    def ParameterFromInt(self, i):
        self.Parameter[0] = (i & 0x000000ff);
        self.Parameter[1] = (i & 0x0000ff00) >> 8;
        self.Parameter[2] = (i & 0x00ff0000) >> 16;
        self.Parameter[3] = (i & 0xff000000) >> 24;

class Response_Packet(Packet):
    '''
        Response Packet Class
    '''
    
    errors = {
                    'NO_ERROR'                      : 0x0000,    # Default value. no error
                    'NACK_TIMEOUT'                  : 0x1001,    # Obsolete, capture timeout
                    'NACK_INVALID_BAUDRATE'         : 0x1002,    # Obsolete, Invalid serial baud rate
                    'NACK_INVALID_POS'              : 0x1003,    # The specified ID is not between 0~199
                    'NACK_IS_NOT_USED'              : 0x1004,    # The specified ID is not used
                    'NACK_IS_ALREADY_USED'          : 0x1005,    # The specified ID is already used
                    'NACK_COMM_ERR'                 : 0x1006,    # Communication Error
                    'NACK_VERIFY_FAILED'            : 0x1007,    # 1:1 Verification Failure
                    'NACK_IDENTIFY_FAILED'          : 0x1008,    # 1:N Identification Failure
                    'NACK_DB_IS_FULL'               : 0x1009,    # The database is full
                    'NACK_DB_IS_EMPTY'              : 0x100A,    # The database is empty
                    'NACK_TURN_ERR'                 : 0x100B,    # Obsolete, Invalid order of the enrollment (The order was not as: EnrollStart -> Enroll1 -> Enroll2 -> Enroll3)
                    'NACK_BAD_FINGER'               : 0x100C,    # Too bad fingerprint
                    'NACK_ENROLL_FAILED'            : 0x100D,    # Enrollment Failure
                    'NACK_IS_NOT_SUPPORTED'         : 0x100E,    # The specified command is not supported
                    'NACK_DEV_ERR'                  : 0x100F,    # Device Error, especially if Crypto-Chip is trouble
                    'NACK_CAPTURE_CANCELED'         : 0x1010,    # Obsolete, The capturing is canceled
                    'NACK_INVALID_PARAM'            : 0x1011,    # Invalid parameter
                    'NACK_FINGER_IS_NOT_PRESSED'    : 0x1012,    # Finger is not pressed
                    'INVALID'                       : 0XFFFF     # Used when parsing fails          
              }
    
    def __init__(self,_buffer=None,UseSerialDebug=False):
        '''
        creates and parses a response packet from the finger print scanner
        '''
        self.UseSerialDebug= UseSerialDebug
        
        if not (_buffer is None ):
            self.RawBytes = _buffer
            self._lastBuffer = bytes(_buffer)
            if self.UseSerialDebug:
                print 'readed: %s'% self.serializeToSend(_buffer)
            if _buffer.__len__()>=12:
                self.ACK = True if _buffer[8] == 0x30 else False
                self.ParameterBytes[0] = _buffer[4]
                self.ParameterBytes[1] = _buffer[5]
                self.ParameterBytes[2] = _buffer[6]
                self.ParameterBytes[3] = _buffer[7]
                self.ResponseBytes[0]  = _buffer[8]
                self.ResponseBytes[1]  = _buffer[9]
                self.Error = self.ParseFromBytes(self.GetHighByte(_buffer[5]),self.GetLowByte(_buffer[4]))
        
    _lastBuffer = bytes()
    RawBytes = bytearray(12)
    ParameterBytes=bytearray(4)
    ResponseBytes=bytearray(2)
    ACK = False
    Error = None
    UseSerialDebug = True
    
    
    def ParseFromBytes(self,high,low):
        '''
        parses bytes into one of the possible errors from the finger print scanner
        '''
        e  = 'INVALID'
        if high == 0x01:
            if low in self.errors.values():
                errorIndex = self.errors.values().index(low)
                e = self.errors.keys()[errorIndex]
        return e
    
    
    def IntFromParameter(self):
        retval = 0;
        retval = (retval << 8) + self.ParameterBytes[3];
        retval = (retval << 8) + self.ParameterBytes[2];
        retval = (retval << 8) + self.ParameterBytes[1];
        retval = (retval << 8) + self.ParameterBytes[0];
        return retval;

class SerialCommander:
    def __serialize_args_hex__(self,*arg,**kwargs):
        return bytes(bytearray([v for v in kwargs.values()]))
    def serializeToSend(self,bytearr):
        return ' '.join(binascii.hexlify(ch) for ch in bytes(bytearr))
    def unserializeFromRead(self,char_readed,bytearr):
        bytearr.append(char_readed)
        return bytearr

def connect(device_name=None,baud=None,timeout=None,is_com=True):
    _ser = None
        is_com = false
    baud = 9600
    device_name = '/dev/ttyAMA0'
    timeout = 2000
    return _ser

    

BAUD = 9600

class fingerprintseonsor(SerialCommander):
    _serial = None
    _lastResponse = None
    _device_name = None
    _baud = None
    _timeout= None

    UseSerialDebug = True
    
    def __init__(self,device_name=None,baud=None,timeout=None,is_com=True):
        self._device_name = device_name
        self._baud=baud
        self._timeout = timeout
        self._serial = connect(device_name,baud,timeout,is_com=is_com)
        if not self._serial is None:
            delay(0.1)
            self.Open()
        elif self.UseSerialDebug:
            print 'No connection with this device:- %s' % self._device_name
            
     
    def Open(self):

        self.ChangeBaudRate(BAUD)
        delay(0.1)
        cp = Command_Packet('Open',UseSerialDebug=self.UseSerialDebug)
        cp.ParameterFromInt(1)
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        del packetbytes
        return rp.ACK
        
    
    def Close(self):
        cp = Command_Packet('Close',UseSerialDebug=self.UseSerialDebug)
        cp.Parameter[0] = 0x00;
        cp.Parameter[1] = 0x00;
        cp.Parameter[2] = 0x00;
        cp.Parameter[3] = 0x00;
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        if not self._serial is None:
            self._serial.close()
        del packetbytes
        return rp.ACK
    
    def SetLED(self,on=True):
        cp = Command_Packet('CmosLed',UseSerialDebug=self.UseSerialDebug)
        cp.Parameter[0] = 0x01 if on else 0x00;
        cp.Parameter[1] = 0x00;
        cp.Parameter[2] = 0x00;
        cp.Parameter[3] = 0x00;
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        retval = rp.ACK
        del rp
        del packetbytes
        return retval

    def CheckEnrolled(self,ID):
        cp = Command_Packet('CheckEnrolled',UseSerialDebug=self.UseSerialDebug)
        cp.ParameterFromInt(ID)
        packetbytes = cp.GetPacketBytes()
        del cp
        self.SendCommand(packetbytes, 12)
        del packetbytes
        rp = self.GetResponse()
        retval = rp.ACK
        del rp
        return retval
    def EnrollStart(self,ID):
        cp = Command_Packet('EnrollStart',UseSerialDebug=self.UseSerialDebug)
        cp.ParameterFromInt(ID)
        packetbytes = cp.GetPacketBytes()
        del cp
        self.SendCommand(packetbytes, 12)
        del packetbytes
        rp = self.GetResponse()
        retval = 0
        if not rp.ACK:
            if rp.Error == rp.errors['NACK_DB_IS_FULL']:
                retval = 1
            elif rp.Error == rp.errors['NACK_INVALID_POS']:
                retval = 2
            elif rp.Error == rp.errors['NACK_IS_ALREADY_USED']:
                retval = 3
        del rp
        return retval
    def Enroll1(self):
        cp = Command_Packet('Enroll1',UseSerialDebug=self.UseSerialDebug)
        packetbytes = cp.GetPacketBytes()
        del cp
        self.SendCommand(packetbytes, 12)
        del packetbytes
        rp = self.GetResponse()
        retval = rp.IntFromParameter()
        retval = 3 if retval < 200 else 0
        if not rp.ACK:
            if rp.Error == rp.errors['NACK_ENROLL_FAILED']:
                retval = 1
            elif rp.Error == rp.errors['NACK_BAD_FINGER']:
                retval = 2
        return 0 if rp.ACK else retval
    def Enroll2(self):
        cp = Command_Packet('Enroll2',UseSerialDebug=self.UseSerialDebug)
        packetbytes = cp.GetPacketBytes()
        del cp
        self.SendCommand(packetbytes, 12)
        del packetbytes
        rp = self.GetResponse()
        retval = rp.IntFromParameter()
        retval = 3 if retval < 200 else 0
        if not rp.ACK:
            if rp.Error == rp.errors['NACK_ENROLL_FAILED']:
                retval = 1
            elif rp.Error == rp.errors['NACK_BAD_FINGER']:
                retval = 2
        return 0 if rp.ACK else retval
    def Enroll3(self):
        cp = Command_Packet('Enroll3',UseSerialDebug=self.UseSerialDebug)
        packetbytes = cp.GetPacketBytes()
        del cp
        self.SendCommand(packetbytes, 12)
        del packetbytes
        rp = self.GetResponse()
        retval = rp.IntFromParameter()
        retval = 3 if retval < 200 else 0
        if not rp.ACK:
            if rp.Error == rp.errors['NACK_ENROLL_FAILED']:
                retval = 1
            elif rp.Error == rp.errors['NACK_BAD_FINGER']:
                retval = 2
        return 0 if rp.ACK else retval
    def IsPressFinger(self):
        cp = Command_Packet('IsPressFinger',UseSerialDebug=self.UseSerialDebug)
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        pval = rp.ParameterBytes[0]
        pval += rp.ParameterBytes[1]
        pval += rp.ParameterBytes[2]
        pval += rp.ParameterBytes[3]
        retval = True if pval == 0 else False
        del rp
        del packetbytes
        del cp
        return retval
    
    def DeleteID(self,ID):
        cp = Command_Packet('DeleteID',UseSerialDebug=self.UseSerialDebug)
        cp.ParameterFromInt(ID)
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        retval = rp.ACK
        del rp
        del packetbytes
        del cp
        return retval
    
    def Identify1_N(self):
        cp = Command_Packet('Identify1_N',UseSerialDebug=self.UseSerialDebug)
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        retval = rp.IntFromParameter()
        if retval > 200:
            retval = 200
        del rp
        del packetbytes
        del cp
        return retval
    
    
    def CaptureFinger(self,highquality=True):
        cp = Command_Packet('CaptureFinger',UseSerialDebug=self.UseSerialDebug)
        cp.ParameterFromInt(1 if highquality else 0)
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        retval = rp.ACK
        del rp
        del packetbytes
        del cp
        return retval

    def GetTemplate(self, ID):
        '''
             Gets a template from the fps (498 bytes) in 4 Data_Packets
             Use StartDataDownload, and then GetNextDataPacket until done
             Parameter: 0-199 ID number
             Returns: 
                0 - ACK Download starting
                1 - Invalid position
                2 - ID not used (no template to download
        '''
        cp = Command_Packet('GetTemplate',UseSerialDebug=self.UseSerialDebug)
        cp.ParameterFromInt(ID)
        packetbytes = cp.GetPacketBytes()
        self.SendCommand(packetbytes, 12)
        rp = self.GetResponse()
        retval = 0
        if not rp.ACK:
            if rp.Error == rp.errors['NACK_INVALID_POS']:
                retval = 1
            elif rp.Error == rp.errors['NACK_IS_NOT_USED']:
                retval = 2
        return retval
