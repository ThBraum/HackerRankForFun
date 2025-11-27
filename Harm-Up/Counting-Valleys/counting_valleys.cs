using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Result
{
    /*
     * Complete the 'countingValleys' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER steps
     *  2. STRING path
     */

    public static int countingValleys(int steps, string path)
    {
        int altitude = 0;
        int valleys = 0;

        foreach (char c in path)
        {
            if (c == 'U')
            {
                altitude++;
                if (altitude == 0)
                    valleys++;
            }
            else
            {
                altitude--;
            }
        }

        return valleys;
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(Environment.GetEnvironmentVariable("OUTPUT_PATH") ?? "output.txt", true);

        int steps = Convert.ToInt32(Console.ReadLine().Trim());

        string path = Console.ReadLine().Trim();

        int result = Result.countingValleys(steps, path);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
