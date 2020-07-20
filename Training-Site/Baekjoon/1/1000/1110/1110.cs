using System;
using System.Linq;

namespace Dotnet
{
    class Program
    {
        static void Main(string[] args)
        {
            int _input = int.Parse(Console.ReadLine());
            int result = _input;
            int cycle = 0;

            do
            {
                string a = (result.ToString("00")
                            .Select(o => Convert.ToInt32(o))
                            .Last() - 48)
                            .ToString();

                string b = result.ToString("00")
                            .Select(o => Convert.ToInt32(o) - 48)
                            .ToArray()
                            .Sum()
                            .ToString();

                result = int.Parse(a.Last().ToString() + b.Last().ToString());

                cycle++;
            } while (_input != result);

            Console.WriteLine(cycle);
        }
    }
}
