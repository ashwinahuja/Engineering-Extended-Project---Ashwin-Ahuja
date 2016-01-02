using System;

namespace EPCipherDecoderForDeviceJustForShow
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			const int product_number = 1234567890;
			char usual = Convert.ToChar (253);
			string pn = Convert.ToString (product_number);
			Console.WriteLine ("Hello World!");
			string inputs = Console.ReadLine ();
			int counter = 0;
			int toEnd = Convert.ToString (product_number).Length;
			string finalString = "";
			for (int i = 0; i < inputs.Length; i++) {
				if (counter >= toEnd) {
					if (toEnd == 0) {
						toEnd = Convert.ToString (product_number).Length +1;
					}
					toEnd--;
					counter = 0;
				}
				if (inputs [i] == usual) {
					finalString = finalString + Convert.ToString(usual);
				}
				else{
					int toDealWith = Convert.ToInt32 (inputs [i]);
					if (toDealWith > 150) {
						toDealWith = toDealWith - 34;
					}
					int originalNumber = toDealWith - Convert.ToInt32(Char.GetNumericValue (pn [counter]));
					finalString = finalString + Convert.ToChar (originalNumber);
				}
				counter++;
			}
			string[] finals = finalString.Split (usual);
			Console.WriteLine ("NAME: " + finals [0] + "\nUSERNAME: " + finals [1] + "\nPASSWORD: " + finals [2]);
			Console.ReadLine ();
		}
	}
}
