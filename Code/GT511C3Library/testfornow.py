import mainFile, sys
import time
fp = mainFile.fingerprintsensor()
fp.Open()
while(1):
    fp.SetLED(true)
    mainFile.delay(1)
    fp.SetLED(false)
    mainFile.delay(1)
