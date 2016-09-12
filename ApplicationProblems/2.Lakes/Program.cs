/*
 * We are living in 2D world and we are running out of water! We are migrating to KEPLER-186F, the new planet that NASA discovered, but it is a slow migration because that planet is far far away.

Luckily we still have some big lakes full of clean water. We need to know exactly how much water is in every lake.

Write a program that takes the lake structure and calculates the amount of water there.

Few important things:

Our lakes live in a 2D grid of 1x1 squares.
We are always going to start from depth 0 and finish at depth 0.
Each square can be filled with 1000 liters of water.
Input

On the standard input, we read a line - string that represents the structure of the lake.

d - stands for down. We are always taking the horizontal line that splits the 1x1 square in half.
h - stands for horizontal
u - stands for up
Output should be the total liters of water.
 */

namespace Lakes
{
    using System;
    using System.Collections.Generic;

    class Program
    {
        static readonly Dictionary<char, double> DirToValue = new Dictionary<char, double>();

        static void Main()
        {
            // Initialize directions to values list
            DirToValue.Add('d', 0.5);
            DirToValue.Add('u', 0.5);
            DirToValue.Add('h', 1);

            // Read input
            int currentDepth = 0;
            double sum = 0;
            string input = Console.ReadLine();

            if (input == null)
            {
                throw new NullReferenceException();
            }

            foreach (char currentDir in input)
            {
                // Get current moving direction

                // prefIsDown fixes a bug where moving down from a level lower than -1 cause miss calculations 
                bool prefIsDown;
                switch (currentDir)
                {
                    case 'd':
                        currentDepth++;
                        prefIsDown = true;
                        break;
                    case 'u':
                        currentDepth--;
                        prefIsDown = false;
                        break;
                    default:
                        prefIsDown = false;
                        break;
                }

                // Do the math according to depth level and movement
                if (currentDepth > 0)
                {
                    if (currentDir == 'u')
                    {
                        sum += 1000;
                    }
                    sum += DirToValue[currentDir] * 1000 + (1000 * (currentDepth - 1));

                }
                else if (currentDepth >= 0 && !prefIsDown)
                {
                    sum += DirToValue[currentDir] * 1000;
                }
            }

            Console.WriteLine(sum);
        }
    }
}
