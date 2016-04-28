namespace LicensePlateDatabase
{
    partial class SendMessageForm
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
            this.btnSendMessage = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.lblHistoricFilePath = new System.Windows.Forms.Label();
            this.txtMessage = new System.Windows.Forms.TextBox();
            this.txtType = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // btnSendMessage
            // 
            this.btnSendMessage.Location = new System.Drawing.Point(396, 12);
            this.btnSendMessage.Name = "btnSendMessage";
            this.btnSendMessage.Size = new System.Drawing.Size(64, 58);
            this.btnSendMessage.TabIndex = 39;
            this.btnSendMessage.Text = "Send Message";
            this.btnSendMessage.UseVisualStyleBackColor = true;
            this.btnSendMessage.Click += new System.EventHandler(this.btnSendMessage_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(49, 54);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 13);
            this.label1.TabIndex = 38;
            this.label1.Text = "Message Type";
            // 
            // lblHistoricFilePath
            // 
            this.lblHistoricFilePath.AutoSize = true;
            this.lblHistoricFilePath.Location = new System.Drawing.Point(36, 16);
            this.lblHistoricFilePath.Name = "lblHistoricFilePath";
            this.lblHistoricFilePath.Size = new System.Drawing.Size(78, 13);
            this.lblHistoricFilePath.TabIndex = 37;
            this.lblHistoricFilePath.Text = "Write Message";
            // 
            // txtMessage
            // 
            this.txtMessage.Location = new System.Drawing.Point(150, 12);
            this.txtMessage.Name = "txtMessage";
            this.txtMessage.Size = new System.Drawing.Size(217, 20);
            this.txtMessage.TabIndex = 36;
            // 
            // txtType
            // 
            this.txtType.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.txtType.FormattingEnabled = true;
            this.txtType.Items.AddRange(new object[] {
            "NULL",
            "INFO",
            "ALERT",
            "SERVER"});
            this.txtType.Location = new System.Drawing.Point(150, 51);
            this.txtType.Name = "txtType";
            this.txtType.Size = new System.Drawing.Size(173, 21);
            this.txtType.TabIndex = 40;
            // 
            // SendMessageForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(498, 93);
            this.Controls.Add(this.txtType);
            this.Controls.Add(this.btnSendMessage);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblHistoricFilePath);
            this.Controls.Add(this.txtMessage);
            this.Name = "SendMessageForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Send Message";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnSendMessage;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblHistoricFilePath;
        private System.Windows.Forms.TextBox txtMessage;
        private System.Windows.Forms.ComboBox txtType;
    }
}