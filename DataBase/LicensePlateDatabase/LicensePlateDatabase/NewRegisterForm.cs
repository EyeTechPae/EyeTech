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

namespace LicensePlateDatabase
{
    public partial class NewRegisterForm : Form
    {
        private String historicFilePath = "Registre de vehicles.xml";

        public NewRegisterForm()
        {
            InitializeComponent();
            txtInOut.SelectedIndex = 0;
        }

        private void AddRegister(object sender, EventArgs e)
        {
            WriteLogs(new Action(txtLicensePlate.Text.ToUpper(), txtInOut.Text));
            this.Close();
        }

        private void WriteLogs(Action action)
        {
            if (!File.Exists(historicFilePath))
            {
                CreateXmlFile();
            }

            else
            {
                var reader = new StreamReader(historicFilePath);
                var header = reader.ReadLine();
                reader.Close();

                if (header == null)
                {
                    CreateXmlFile();
                }
            }

            XDocument xDoc = XDocument.Load(historicFilePath);

            XElement newAction =
                new XElement("Action",
                    new XElement("LicensePlate", action.licensePlate),
                    new XElement("DateTime", action.dateTime.ToString("dd/MM/yyyy HH:mm:ss")),
                    new XElement("INOUT", action.in_out)
                );

            xDoc.Document.Root.Add(newAction);
            xDoc.Save(historicFilePath);
        }

        private void CreateXmlFile()
        {

            StreamWriter xml;
            FileStream xmlFileStream = null;
            DirectoryInfo xmlDirInfo = null;
            FileInfo xmlFileInfo;

            xmlFileInfo = new FileInfo(historicFilePath);
            xmlDirInfo = new DirectoryInfo(xmlFileInfo.DirectoryName);
            if (!xmlDirInfo.Exists) xmlDirInfo.Create();
            xmlFileStream = xmlFileInfo.Create();
            xml = new StreamWriter(xmlFileStream);
            xml.WriteLine("<?xml version=\"1.0\" encoding=\"utf-8\"?>");
            xml.WriteLine("<Register>");
            xml.WriteLine("</Register>");
            xml.Close();
        }
    }
}
