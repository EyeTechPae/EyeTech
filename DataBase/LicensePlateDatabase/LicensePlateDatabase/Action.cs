using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LicensePlateDatabase
{
    class Action
    {
        public String licensePlate;
        public DateTime dateTime;
        public String in_out;

        public Action(String licensePlate, String in_out)
		{
			this.licensePlate = licensePlate;
            this.dateTime = DateTime.Now;
            this.in_out = in_out;
		}
    }
}
