using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Xml.Linq;
using System.IO;
using System.Net;
using System.Net.Sockets;

namespace LicensePlateDatabase
{
    public partial class MainForm : Form
    {
        private String historicFilePath = "Registre de vehicles.xml";
        private DateTime startDate, endDate;
        
        public MainForm()
        {
            InitializeComponent();
            filtersBox.SelectedIndex = 2;
            DateTime nowtime = DateTime.Now;
			this.pickDate.Value = this.pickDate2.Value = nowtime.Date;
            this.pickHour.Text = nowtime.Hour.ToString();
            this.pickHour2.Text = (nowtime.Hour +1).ToString();
            this.pickMin.Text = this.pickMin2.Text = nowtime.Minute.ToString();
        }

        private void filtersBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (filtersBox.SelectedIndex == 0)
            {
                pickDate.Visible = pickHour.Visible = pickMin.Visible = pointsLabel.Visible = fromLabel.Visible = true;
                pickDate2.Visible = pickHour2.Visible = pickMin2.Visible = pointsLabel2.Visible = toLabel.Visible = true;
                licenseText.Visible = false;
            }
            else if (filtersBox.SelectedIndex == 1)
            {
                licenseText.Visible = true;
                pickDate.Visible = pickHour.Visible = pickMin.Visible = pointsLabel.Visible = fromLabel.Visible = false;
                pickDate2.Visible = pickHour2.Visible = pickMin2.Visible = pointsLabel2.Visible = toLabel.Visible = false;
            }
            else
            {
                pickDate.Visible = pickHour.Visible = pickMin.Visible = pointsLabel.Visible = fromLabel.Visible = false;
                pickDate2.Visible = pickHour2.Visible = pickMin2.Visible = pointsLabel2.Visible = toLabel.Visible = false;
                licenseText.Visible = false;
            }
        }

        private void FilterButton_Click(object sender, EventArgs e)
        {
            noDataText.Visible = false;
            DataBaseGrid.Rows.Clear();
            if (filtersBox.SelectedIndex == 0)
            {
                
                startDate = pickDate.Value;
                startDate = startDate.AddHours(Convert.ToDouble(pickHour.Text));
                startDate = startDate.AddMinutes(Convert.ToDouble(pickMin.Text));

                endDate = pickDate2.Value;
                endDate = endDate.AddHours(Convert.ToDouble(pickHour2.Text));
                endDate = endDate.AddMinutes(Convert.ToDouble(pickMin2.Text));

                FilterByDate();
            }
            else if (filtersBox.SelectedIndex == 1)
            {
                if (licenseText.Text == "")
                {
                    noDataText.Text = "Please enter the license plate you want to filter";
                    noDataText.Visible = true;
                }
                else
                {
                    FilterByLicensePlate();
                }
                
            }
            else
            {
                ShowAll();
            }
        }

        private void FilterByDate()
        {
            try
            {
                if (!File.Exists(historicFilePath))
                {
                    MessageBox.Show("No xml document '"+historicFilePath+"' exists");
                }
                else
                {
                    XDocument xDoc = XDocument.Load(historicFilePath);
                    bool exists = false;
                    foreach (var item in (from item in xDoc.Descendants("Action") select item).ToList())
                    {
                        DateTime selectedDate = Convert.ToDateTime(item.Element("DateTime").Value.ToString());
                        int a = DateTime.Compare(selectedDate, startDate);
                        int b = DateTime.Compare(selectedDate, endDate);
                        if ((a >= 0) && (b <= 0))
                        {
                            exists = true;
                            DataBaseGrid.Rows.Add(new object[] { item.Element("DateTime").Value.ToString(), item.Element("LicensePlate").Value.ToString(), item.Element("INOUT").Value.ToString()});
                        }
                    }
                    if (!exists)
                    {
                        noDataText.Text = "No registers in this period";
                        noDataText.Visible = true;
                    }
                }
            }
            catch (Exception e)
            {
                MessageBox.Show("Input document '" + historicFilePath + "' seems to be corrupt. Exception: " + e.ToString());
            }
        }

        private void FilterByLicensePlate()
        {
            try
            {
                if (!File.Exists(historicFilePath))
                {
                    MessageBox.Show("No xml document '" + historicFilePath + "' exists");
                }
                else
                {
                    XDocument xDoc = XDocument.Load(historicFilePath);
                    bool exists = false;
                    foreach (var item in (from item in xDoc.Descendants("Action") select item).ToList())
                    {
                        if (licenseText.Text.ToUpper() == item.Element("LicensePlate").Value.ToString().ToUpper())
                        {
                            exists = true;
                            DataBaseGrid.Rows.Add(new object[] { item.Element("DateTime").Value.ToString(), item.Element("LicensePlate").Value.ToString(), item.Element("INOUT").Value.ToString() });
                        }
                    }
                    if (!exists)
                    {
                        noDataText.Text = "License Plate '"+licenseText.Text.ToUpper()+"' has not been registered in this period";
                        noDataText.Visible = true;
                    }
                }
            }
            catch (Exception e)
            {
                MessageBox.Show("Input document '" + historicFilePath + "' seems to be corrupt. Exception: " + e.ToString());
            }
        }

        private void ShowAll()
        {
            try
            {
                if (!File.Exists(historicFilePath))
                {
                    MessageBox.Show("No xml document '" + historicFilePath + "' exists");
                }
                else
                {
                    XDocument xDoc = XDocument.Load(historicFilePath);
                    foreach (var item in (from item in xDoc.Descendants("Action") select item).ToList())
                    {
                       DataBaseGrid.Rows.Add(new object[] { item.Element("DateTime").Value.ToString(), item.Element("LicensePlate").Value.ToString(), item.Element("INOUT").Value.ToString() });
                    }
                }
            }
            catch (Exception e)
            {
                MessageBox.Show("Input document '" + historicFilePath + "' seems to be corrupt. Exception: " + e.ToString());
            }
        }

        private void CloseApp(object sender, EventArgs e)
        {
            this.Close();
        }

        private void About(object sender, EventArgs e)
        {
            string aboutText = "LicensePlate Database has been developed by Eye-Tech company as a complement to the ParKing project. \n \n Visit us in eye-tech.orgfree.com";
            string titleText = "  About LicensePlate Database : ";
            MessageBoxButtons button = MessageBoxButtons.OK;
            MessageBoxIcon icon = MessageBoxIcon.Information;
            MessageBox.Show(aboutText, titleText, button, icon);
        }

        private void updateToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //IPEndPoint ipe = new IPEndPoint(new IPAddress([123,324,21,23]), 8080);
            //Socket sk= new Socket(ipe.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
			try
			{
				//AsynchronousClient.StartConnection();
                HttpWebRequest_Connection.Read();
			}
			catch (Exception ex)
			{
				
				Console.WriteLine(ex.StackTrace);
			} 
        }

        private void sendMessageToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SendMessageForm sendMessageForm = new SendMessageForm();
            sendMessageForm.ShowDialog();
        }

        private void NewRegister(object sender, EventArgs e)
        {
            NewRegisterForm registerForm = new NewRegisterForm();
            registerForm.ShowDialog();
        }

    }
}
