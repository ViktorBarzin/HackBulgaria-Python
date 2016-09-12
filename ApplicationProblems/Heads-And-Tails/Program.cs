/*Heads and Tails

You are playing a coin-flipping game with your friend.

The rules are:

You toss a coin n times, writing down the results. H for heads and T for tails.
After n tosses, the winner is the one who has the longest consecutive win-streak.
Write a program that reads from the standard input one line - a comma-separated string of H and T and outputs:

H wins! if H wins according to the game rules.
T wins! if T wins according to the game rules.
Draw! if there is no winner.
 */

namespace Heads_And_Tails
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    class Program
    {
        private const char H_VALUE = 'H';
        private const char T_VALUE = 'T';

        private static void Main()
        {
            var readLine = Console.ReadLine();
            if (readLine == null)
            {
                throw new ArgumentNullException();
            }

            List<string> tosses = readLine.Split(new[] { ',', ' ' }, StringSplitOptions.RemoveEmptyEntries).ToList();

            int tMax = int.MinValue;
            int tCurr = 0;
            int hMax = int.MinValue;
            int hCurr = 0;

            // Start counting tosses
            foreach (string t in tosses)
            {
                char currChar = GetTossValue(t);

                // Count consecutive equal tosses and get max
                if (currChar == T_VALUE)
                {
                    tCurr++;
                    if (hCurr > hMax)
                    {
                        hMax = hCurr;
                    }
                    hCurr = 0;
                }
                else
                {
                    hCurr++;
                    if (tCurr > tMax)
                    {
                        tMax = tCurr;
                    }
                    tCurr = 0;
                }
            }

            // Update max values if currMax get bigger than max in changed in last iteration
            if (hCurr > hMax)
            {
                hMax = hCurr;
            }
            if (tCurr > tMax)
            {
                tMax = tCurr;
            }

            Console.WriteLine(hMax > tMax ? "H wins!" : "T wins!");
        }

        // Returns h_Value if char is H and T_value if char is T
        private static char GetTossValue(string c)
        {
            return c == H_VALUE.ToString() ? H_VALUE : T_VALUE;
        }
    }

}
