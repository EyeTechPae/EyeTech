namespace LicensePlateDatabase
{
    partial class NewRegisterForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtLicensePlate = new System.Windows.Forms.TextBox();
            this.lblHistoricFilePath = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.btnAddRegister = new System.Windows.Forms.Button();
            this.txtInOut = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // txtLicensePlate
            // 
            this.txtLicensePlate.Location = new System.Drawing.Point(145, 31);
            this.txtLicensePlate.Name = "txtLicensePlate";
            this.txtLicensePlate.Size = new System.Drawing.Size(217, 20);
            this.txtLicensePlate.TabIndex = 3;
            // 
            // lblHistoricFilePath
            // 
            this.lblHistoricFilePath.AutoSize = true;
            this.lblHistoricFilePath.Location = new System.Drawing.Point(31, 35);
            this.lblHistoricFilePath.Name = "lblHistoricFilePath";
            this.lblHistoricFilePath.Size = new System.Drawing.Size(71, 13);
            this.lblHistoricFilePath.TabIndex = 5;
            this.lblHistoricFilePath.Text = "License Plate";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(44, 73);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(46, 13);
            this.label1.TabIndex = 6;
            this.label1.Text = "IN/OUT";
            // 
            // btnAddRegister
            // 
            this.btnAddRegister.Location = new System.Drawing.Point(391, 31);
            this.btnAddRegister.Name = "btnAddRegister";
            this.btnAddRegister.Size = new System.Drawing.Size(64, 58);
            this.btnAddRegister.TabIndex = 7;
            this.btnAddRegister.Text = "Add Register";
            this.btnAddRegister.UseVisualStyleBackColor = true;
            this.btnAddRegister.Click += new System.EventHandler(this.AddRegister);
            // 
            // txtInOut
            // 
            this.txtInOut.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.txtInOut.FormattingEnabled = true;
            this.txtInOut.Items.AddRange(new object[] {
            "IN",
            "OUT"});
            this.txtInOut.Location = new System.Drawing.Point(145, 70);
            this.txtInOut.Name = "txtInOut";
            this.txtInOut.Size = new System.Drawing.Size(173, 21);
            this.txtInOut.TabIndex = 35;
            // 
            // NewRegisterForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(497, 118);
            this.Controls.Add(this.txtInOut);
            this.Controls.Add(this.btnAddRegister);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblHistoricFilePath);
            this.Controls.Add(this.txtLicensePlate);
            this.Name = "NewRegisterForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "New Register";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtLicensePlate;
        private System.Windows.Forms.Label lblHistoricFilePath;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnAddRegister;
        private System.Windows.Forms.ComboBox txtInOut;
    }
}