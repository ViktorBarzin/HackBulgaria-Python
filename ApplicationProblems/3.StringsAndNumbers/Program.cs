/*
 * Strings and Numbers

You are given a string s that consists of characters, that encode digits & characters that encode nothing. Your goal is to return the sum of all numbers in that string.

Number encoding

In our string s, the digits from 0 to 9 are encoded as follows:

9 is encoded with the most repeated character in s.
8 is encoded with the most repeated character in s, that comes after the one that encodes 9.
...
0 is encoded with the most repeated character in s, that comes after the one that encodes 1.
For example, if 9 is encoded with a, which is repeated 16 times in s, 8 can be encoded with x, which is repeated 15 times in s.

Input details

You read one line from the standard input - the encoded string.
You are guaranteed that there won't be two digits encoded with the same number of repeating characters.
There will always be encoding for all digits between 0 and 9.
Not all digits from 0 to 9 can be encoded. We can have shorter strings that encode small number of digits.
There will always be enough characters to encode digits from 0 to 9.
Input set is "abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~"
If after decoding there are numbers with leading zeroes, ignore them.
Results can get very large. Tackle it with big integers.
Output should be the sum of all numbers in the string.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace StringsAndNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            #region initialize
            Dictionary<char, int> charrOccurences = new Dictionary<char, int>();
            if (input == null)
            {
                throw new ArgumentNullException();
            }

            foreach (var c in input)
            {
                if (charrOccurences.ContainsKey(c))
                {
                    charrOccurences[c]++;
                }
                else
                {
                    charrOccurences.Add(c, 1);
                }
            }
            StringBuilder decodedInput = new StringBuilder();
            #endregion

            // Ordered by occurences
            charrOccurences = charrOccurences.OrderByDescending(x => x.Value)
                                             .Take(10)
                                             .ToDictionary(x => x.Key, y => y.Value);

            // Decodes string
            foreach (char t in input)
            {
                if (charrOccurences.ContainsKey(t))
                {
                    decodedInput.Append(GetPositionInTopTen(charrOccurences.Values, charrOccurences[t]));
                }
                else
                {
                    decodedInput.Append(t);
                }
            }

            // Filter and extract numbers from decoded string
            BigInteger sum = new BigInteger();
            Regex digitRegex = new Regex("[0-9]");
            List<BigInteger> numbers = Regex.Split(decodedInput.ToString(), @"\D+").Where(x => !string.IsNullOrWhiteSpace(x)).Select(BigInteger.Parse).ToList();

            // Get sum sum
            sum = numbers.Aggregate(sum, (current, num) => current + num);

            Console.WriteLine(sum);
        }

        private static int GetPositionInTopTen(IEnumerable<int> list, int n)
        {
            return list.OrderBy(x => x).ToList().IndexOf(n);
        }
    }
}
