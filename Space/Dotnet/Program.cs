using System;
using System.Text;
using System.Net;
using System.Net.Sockets;

namespace Dotnet
{
    class Program
    {
        static void Main(string[] args)
        {
            WebClient dd = new WebClient();
            Console.WriteLine(dd.DownloadString("https://github.com/monegit"));

        }
    }
}
