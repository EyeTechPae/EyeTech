using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Text;
using System.IO;
using System.Windows.Forms;

namespace LicensePlateDatabase
{
    // State object for receiving data from remote device.
    public class StateObject {
        // Client socket.
        public Socket workSocket = null;
        // Size of receive buffer.
        public const int BufferSize = 256;
        // Receive buffer.
        public byte[] buffer = new byte[BufferSize];
        // Received data string.
        public StringBuilder sb = new StringBuilder();
    }

    public class AsynchronousClient
    {
        // The port number for the remote device.
        // ManualResetEvent instances signal completion.
        private static ManualResetEvent connectDone =
            new ManualResetEvent(false);
        private static ManualResetEvent sendDone =
            new ManualResetEvent(false);
        private static ManualResetEvent receiveDone =
            new ManualResetEvent(false);

        // The response from the remote device.
        private static String response = String.Empty;

        private static void StartClient()
        {
            
            string ipadress = "46.101.132.172";
            int port = 3333;
            // Connect to a remote device.
            try
            {
                // Establish the remote endpoint for the socket.
				//IPHostEntry ipHostInfo = Dns.GetHostEntry(ipadress);
				//IPAddress ipAddress = ipHostInfo.AddressList[0];
				IPEndPoint remoteEP = new IPEndPoint(IPAddress.Parse(ipadress), port);

                // Create a TCP/IP socket.
                Socket client = new Socket(AddressFamily.InterNetwork,
                    SocketType.Stream, ProtocolType.Tcp);

                // Connect to the remote endpoint.
                client.BeginConnect(remoteEP,
                    new AsyncCallback(ConnectCallback), client);
                connectDone.WaitOne();

                // Send test data to the remote device.
                Send(client, "Send me de info");
                sendDone.WaitOne();

                //// Receive the response from the remote device.
                //Receive(client);
                //receiveDone.WaitOne();

                //// Write the response to the console.
                //Console.WriteLine("Response received : {0}", response);
                //Send(client, "Received");

                // Release the socket.
                client.Shutdown(SocketShutdown.Both);
                client.Close();

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static void ConnectCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.
                Socket client = (Socket)ar.AsyncState;

                // Complete the connection.
                client.EndConnect(ar);

                Console.WriteLine("Socket connected to {0}",
                    client.RemoteEndPoint.ToString());

                // Signal that the connection has been made.
                connectDone.Set();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static void Receive(Socket client)
        {
            try
            {
                // Create the state object.
                StateObject state = new StateObject();
                state.workSocket = client;

                // Begin receiving the data from the remote device.
                client.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                    new AsyncCallback(ReceiveCallback), state);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static void ReceiveCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the state object and the client socket 
                // from the asynchronous state object.
                StateObject state = (StateObject)ar.AsyncState;
                Socket client = state.workSocket;

                // Read data from the remote device.
                int bytesRead = client.EndReceive(ar);

                if (bytesRead > 0)
                {
                    // There might be more data, so store the data received so far.
                    state.sb.Append(Encoding.ASCII.GetString(state.buffer, 0, bytesRead));
                    string rec = Encoding.ASCII.GetString(state.buffer, 0, bytesRead);
                    System.IO.File.AppendAllText("Registre de vehicles.xml", rec, Encoding.UTF8);
                    // Get the rest of the data.
                    client.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                        new AsyncCallback(ReceiveCallback), state);
                }
                else
                {
                    // All the data has arrived; put it in response.
                    if (state.sb.Length > 1)
                    {
                        response = state.sb.ToString();
                    }
                    // Signal that all bytes have been received.
                    receiveDone.Set();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static void Send(Socket client, String data)
        {
            // Convert the string data to byte data using ASCII encoding.
            //byte[] byteData = Encoding.ASCII.GetBytes(data);
            byte[] byteData = Encoding.UTF8.GetBytes(data);

            // Begin sending the data to the remote device.
            client.BeginSend(byteData, 0, byteData.Length, 0,
                new AsyncCallback(SendCallback), client);
        }

        private static void SendCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.
                Socket client = (Socket)ar.AsyncState;

                // Complete sending the data to the remote device.
                int bytesSent = client.EndSend(ar);
                Console.WriteLine("Sent {0} bytes to server.", bytesSent);

                // Signal that all bytes have been sent.
                sendDone.Set();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
        public static int StartConnection()
        {
            StartClient();
            return 0;
        }

        public static int SendMessage(string message)
        {
            string ipadress = "46.101.132.172";
            int port = 3335;
            // Connect to a remote device.
            try
            {
				IPEndPoint remoteEP = new IPEndPoint(IPAddress.Parse(ipadress), port);

                // Create a TCP/IP socket.
                Socket client = new Socket(AddressFamily.InterNetwork,
                    SocketType.Stream, ProtocolType.Tcp);

                // Connect to the remote endpoint.
                client.BeginConnect(remoteEP,
                    new AsyncCallback(ConnectCallback), client);
                connectDone.WaitOne();

                // Send test data to the remote device.
                Send(client, message);
                sendDone.WaitOne();
                client.Shutdown(SocketShutdown.Both);
                client.Close();
            return 0;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
                return 0;
            }
        }

        public static string ReceiveXML()
        {
            string ipadress = "46.101.132.172";
            int port = 3333;
            // Connect to a remote device.
            try
            {
                IPEndPoint remoteEP = new IPEndPoint(IPAddress.Parse(ipadress), port);

                // Create a TCP/IP socket.
                Socket client = new Socket(AddressFamily.InterNetwork,
                    SocketType.Stream, ProtocolType.Tcp);

                // Connect to the remote endpoint.
                client.BeginConnect(remoteEP,
                    new AsyncCallback(ConnectCallback), client);
                connectDone.WaitOne();
                try
                {
                    //guardamos una copia del archivo por si falla algo
                    File.Copy("Registre de vehicles.xml", "Registre de vehicles - last.xml", true);
                    File.Delete("Registre de vehicles.xml");
                }
                catch (Exception fi)
                {
                    Console.WriteLine(fi.ToString());
                }
                
                //// Receive the response from the remote device.
                Receive(client);
                receiveDone.WaitOne();

                //// Write the response to the console.
                //Console.WriteLine("Response received : {0}", response);
                //Send(client, "Received");

                // Release the socket.
                client.Shutdown(SocketShutdown.Both);
                client.Close();
                try
                {
                    //borramos el archivo copia
                    File.Delete("Registre de vehicles - last.xml");
                }
                catch (Exception fi)
                {
                    Console.WriteLine(fi.ToString());
                }
                return response;

            }
            catch (Exception e)
            {
                Console.WriteLine("Algo ha fallado");
                Console.WriteLine(e.ToString());
                //Recuperamos el archivo anterior
                try
                {
                    File.Copy("Registre de vehicles - last.xml", "Registre de vehicles.xml", true);
                    File.Delete("Registre de vehicles - last.xml");
                }
                catch (Exception fi)
                {
                    Console.WriteLine(fi.ToString());
                }

                MessageBox.Show(e.Message.ToString());
                return null;
            }
        }
    }
    class HttpWebRequest_Connection
    {
        public static void Read()
        {
            try
            {

                // Create a new HttpWebRequest object.Make sure that 
                // a default proxy is set if you are behind a firewall.
                HttpWebRequest myHttpWebRequest1 =
                  (HttpWebRequest)WebRequest.Create("http://46.101.132.172:3333");
                myHttpWebRequest1.KeepAlive = false;
                // Assign the response object of HttpWebRequest to a HttpWebResponse variable.
                HttpWebResponse myHttpWebResponse1 =
                  (HttpWebResponse)myHttpWebRequest1.GetResponse();

                Console.WriteLine("\nThe HTTP request Headers for the first request are: \n{0}", myHttpWebRequest1.Headers);
                Console.WriteLine("Press Enter Key to Continue..........");
                Console.Read();

                Stream streamResponse = myHttpWebResponse1.GetResponseStream();
                StreamReader streamRead = new StreamReader(streamResponse);
                Char[] readBuff = new Char[256];
                int count = streamRead.Read(readBuff, 0, 256);
                Console.WriteLine("The contents of the Html page are.......\n");
                while (count > 0)
                {
                    String outputData = new String(readBuff, 0, count);
                    Console.Write(outputData);
                    count = streamRead.Read(readBuff, 0, 256);
                }
                Console.WriteLine();
                // Close the Stream object.
                streamResponse.Close();
                streamRead.Close();
                // Release the resources held by response object.
                myHttpWebResponse1.Close();
                // Create a new HttpWebRequest object for the specified Uri.
                HttpWebRequest myHttpWebRequest2 =
                  (HttpWebRequest)WebRequest.Create("http://46.101.132.172:3333");
                myHttpWebRequest2.Connection = "Close";
                // Assign the response object of 'HttpWebRequest' to a 'HttpWebResponse' variable.
                HttpWebResponse myHttpWebResponse2 =
                  (HttpWebResponse)myHttpWebRequest2.GetResponse();
                // Release the resources held by response object.
                myHttpWebResponse2.Close();
                Console.WriteLine("\nThe Http RequestHeaders are \n{0}", myHttpWebRequest2.Headers);
                Console.WriteLine("\nPress 'Enter' Key to Continue.........");
                Console.Read();
            }
            catch (ArgumentException e)
            {
                Console.WriteLine("\nThe second HttpWebRequest object has raised an Argument Exception as 'Connection' Property is set to 'Close'");
                Console.WriteLine("\n{0}", e.Message);
            }
            catch (WebException e)
            {
                Console.WriteLine("WebException raised!");
                Console.WriteLine("\n{0}", e.Message);
                Console.WriteLine("\n{0}", e.Status);
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception raised!");
                Console.WriteLine("Source :{0} ", e.Source);
                Console.WriteLine("Message :{0} ", e.Message);
            }
        }
    }
}
