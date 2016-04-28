using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace LicensePlateDatabase
{
    public partial class SendMessageForm : Form
    {
        public SendMessageForm()
        {
            InitializeComponent();
        }

        private void btnSendMessage_Click(object sender, EventArgs e)
        {
            string message = txtType.SelectedIndex.ToString();
            message = message+txtMessage.Text+"\0";
            AsynchronousClient.SendMessage(message);
            this.Close();
        }
    }
}
