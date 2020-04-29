using System;
using System.IO;
using System.Collections.Generic;
namespace TestOfCipherForEP
{
	class MainClass
	{
		public static List<int> toNumbers(string i)
		{
			List<int> final = new List<int>();
			for (int j = 0; j < i.Length; j++)
			{
					final.Add (Convert.ToInt32 (i [j]));
			}
			return final;
		}
		public static void Main (string[] args)
		{
//			#define productNumber 1011
//			using (StreamWriter writer = new StreamWriter ("i.txt")) {
//				for (int i = 33; i < 100; i++) {
//					if (i > 126 && i < 160) {
//						i = 161;
//					}
//					Console.WriteLine ("I: " + i + "\t" + (char)i);
//					writer.WriteLine ("I: " + i + "\t" + (char)i);			
//				}
//			}
//			Console.ReadLine ();
////			Console.ReadLine ();
////				while (Convert.ToInt32 (Console.ReadLine ()) != 0) {
////					Console.WriteLine ("Hello World!");
////					char input = Console.ReadLine () [0];
////					int inputOfCipherDistance = Convert.ToInt32 (Console.ReadLine ());
////					int inputComverted = Convert.ToInt32 (input);
////					Console.WriteLine ("\t" + inputComverted);
////					int final = inputComverted + inputOfCipherDistance;
////					Console.WriteLine ((char)final);
////				}
			using (StreamWriter writer = new StreamWriter ("i.txt")) {
				const int product_number = 1234567890;
				string input = Convert.ToString (product_number);
					Console.WriteLine ("Enter name of the account");
					string account = Console.ReadLine ();
					Console.WriteLine ("Enter username");
					string username = Console.ReadLine ();
					Console.WriteLine ("Enter password");
					string password = Console.ReadLine ();
				string combined = account + Convert.ToChar (253) + username + Convert.ToChar (253) + password;
					List<int> combinedToNumbers = toNumbers (combined);
				int until = input.Length;
				int counter = 0;
				string finalToOutput = "";
				for (int i = 0; i < combinedToNumbers.Count; i++) {
					if (counter >= until) {
						if (until == 0) {
							until = input.Length+1;
						}
						until--;
						counter = 0;
					} else {
					}
					if (combinedToNumbers [i] == 253) {
						//It is a null so dont change it and make it the correct 
						char temp = Convert.ToChar (253);
						finalToOutput = finalToOutput + Convert.ToString (temp);
					} else {
						char charToDealWith = input [counter];
						int toDoThingsTo = combinedToNumbers [i];
						int changed = (int)toDoThingsTo + (int)Char.GetNumericValue (charToDealWith);
						if (changed > 127) {
							changed = changed + 34;
						}
						char newChar = Convert.ToChar (changed);
						string toAdd = Convert.ToString (newChar);
						finalToOutput = finalToOutput + toAdd;
					}
					counter++;
				}
				Console.WriteLine (finalToOutput);
				writer.WriteLine (finalToOutput);
				Console.ReadLine ();
		}


		}

	}
}
