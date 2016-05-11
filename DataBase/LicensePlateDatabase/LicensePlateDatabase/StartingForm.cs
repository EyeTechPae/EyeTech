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
	public partial class StartingForm : Form
	{
		Timer timer1;
		public StartingForm()
		{
			InitializeComponent();
            int count = 0;
			timer1 = new Timer();
			timer1.Interval = 600;
			timer1.Start();
			timer1.Tick += (s, e) =>
			{
                if (count == 5)
                {
                    progressBar.Value = count;
                    this.Close();
                }
                else
                {
                    count++;
                    progressBar.Value = count;
                }
			}; 
		}
	}
}
