using System;
using System.Text;

namespace Dotnet
{
    class Program
    {
        static void Main(string[] args)
        {
            StringBuilder sb = new StringBuilder();

            string str = Console.ReadLine();
            int n = int.Parse(str.Split(" ")[0]);
            int m = int.Parse(str.Split(" ")[1]);
            int sum = 1;

            for (int i = 0; i < n; i++)
            {
                for (int ii = 0; ii < m; ii++)
                {
                    sb.Append(sum+" ");
                    sum++;
                }
                Console.WriteLine(sb.ToString().Trim());
                sb.Clear();
            }
        }
    }
}
