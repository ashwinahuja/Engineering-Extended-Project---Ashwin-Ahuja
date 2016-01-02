using System;
using System.IO;
namespace TEMP
{
	class MainClass
	{
		public static void Main (string[] args)
		{
						using (StreamWriter writer = new StreamWriter ("i.txt")) {
							for (int i = 33; i < 325; i++) {
								if (i > 126 && i < 160) {
									i = 161;
								}
								Console.WriteLine ("I: " + i + "\t" + (char)i);
								writer.WriteLine ("I: " + i + "\t" + (char)i);			
							}
						}
			Console.ReadLine ();
		}
	}
}
