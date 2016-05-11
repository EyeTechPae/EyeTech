namespace LicensePlateDatabase
{
    partial class MainForm
    {
        /// <summary>
        /// Variable del diseñador requerida.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén utilizando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben eliminar; false en caso contrario, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido del método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle1 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle2 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle3 = new System.Windows.Forms.DataGridViewCellStyle();
            this.tsmMenu = new System.Windows.Forms.MenuStrip();
            this.tsmFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.updateToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.closeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.helpToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutLicensePlateDatabaseToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.label1 = new System.Windows.Forms.Label();
            this.pointsLabel = new System.Windows.Forms.Label();
            this.filtersBox = new System.Windows.Forms.ComboBox();
            this.pointsLabel2 = new System.Windows.Forms.Label();
            this.pickMin2 = new System.Windows.Forms.TextBox();
            this.pickHour2 = new System.Windows.Forms.TextBox();
            this.pickDate2 = new System.Windows.Forms.DateTimePicker();
            this.pickMin = new System.Windows.Forms.TextBox();
            this.pickHour = new System.Windows.Forms.TextBox();
            this.pickDate = new System.Windows.Forms.DateTimePicker();
            this.licenseText = new System.Windows.Forms.TextBox();
            this.FilterButton = new System.Windows.Forms.Button();
            this.noDataText = new System.Windows.Forms.Button();
            this.DataBaseGrid = new System.Windows.Forms.DataGridView();
            this.ColumnName = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnPid = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnUser = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.fromLabel = new System.Windows.Forms.Label();
            this.toLabel = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.updatingBox = new System.Windows.Forms.PictureBox();
            this.tsmMenu.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.DataBaseGrid)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.updatingBox)).BeginInit();
            this.SuspendLayout();
            // 
            // tsmMenu
            // 
            this.tsmMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmFileExit,
            this.helpToolStripMenuItem});
            this.tsmMenu.Location = new System.Drawing.Point(0, 0);
            this.tsmMenu.Name = "tsmMenu";
            this.tsmMenu.Size = new System.Drawing.Size(695, 24);
            this.tsmMenu.TabIndex = 1;
            this.tsmMenu.Text = "File";
            // 
            // tsmFileExit
            // 
            this.tsmFileExit.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.updateToolStripMenuItem,
            this.closeToolStripMenuItem});
            this.tsmFileExit.Name = "tsmFileExit";
            this.tsmFileExit.Size = new System.Drawing.Size(37, 20);
            this.tsmFileExit.Text = "&File";
            // 
            // updateToolStripMenuItem
            // 
            this.updateToolStripMenuItem.Name = "updateToolStripMenuItem";
            this.updateToolStripMenuItem.Size = new System.Drawing.Size(138, 22);
            this.updateToolStripMenuItem.Text = "Update data";
            this.updateToolStripMenuItem.Click += new System.EventHandler(this.updateToolStripMenuItem_Click);
            // 
            // closeToolStripMenuItem
            // 
            this.closeToolStripMenuItem.Name = "closeToolStripMenuItem";
            this.closeToolStripMenuItem.Size = new System.Drawing.Size(138, 22);
            this.closeToolStripMenuItem.Text = "Close";
            this.closeToolStripMenuItem.Click += new System.EventHandler(this.CloseApp);
            // 
            // helpToolStripMenuItem
            // 
            this.helpToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aboutLicensePlateDatabaseToolStripMenuItem});
            this.helpToolStripMenuItem.Name = "helpToolStripMenuItem";
            this.helpToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.helpToolStripMenuItem.Text = "Help";
            // 
            // aboutLicensePlateDatabaseToolStripMenuItem
            // 
            this.aboutLicensePlateDatabaseToolStripMenuItem.Name = "aboutLicensePlateDatabaseToolStripMenuItem";
            this.aboutLicensePlateDatabaseToolStripMenuItem.Size = new System.Drawing.Size(226, 22);
            this.aboutLicensePlateDatabaseToolStripMenuItem.Text = "About LicensePlate Database";
            this.aboutLicensePlateDatabaseToolStripMenuItem.Click += new System.EventHandler(this.About);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(15, 51);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(49, 13);
            this.label1.TabIndex = 30;
            this.label1.Text = "Filter by :";
            // 
            // pointsLabel
            // 
            this.pointsLabel.AutoSize = true;
            this.pointsLabel.Location = new System.Drawing.Point(471, 40);
            this.pointsLabel.Name = "pointsLabel";
            this.pointsLabel.Size = new System.Drawing.Size(10, 13);
            this.pointsLabel.TabIndex = 31;
            this.pointsLabel.Text = ":";
            this.pointsLabel.Visible = false;
            // 
            // filtersBox
            // 
            this.filtersBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.filtersBox.FormattingEnabled = true;
            this.filtersBox.Items.AddRange(new object[] {
            "Date",
            "License Plate",
            "Show All"});
            this.filtersBox.Location = new System.Drawing.Point(69, 48);
            this.filtersBox.Name = "filtersBox";
            this.filtersBox.Size = new System.Drawing.Size(99, 21);
            this.filtersBox.TabIndex = 34;
            this.filtersBox.SelectedIndexChanged += new System.EventHandler(this.filtersBox_SelectedIndexChanged);
            // 
            // pointsLabel2
            // 
            this.pointsLabel2.AutoSize = true;
            this.pointsLabel2.Location = new System.Drawing.Point(471, 62);
            this.pointsLabel2.Name = "pointsLabel2";
            this.pointsLabel2.Size = new System.Drawing.Size(10, 13);
            this.pointsLabel2.TabIndex = 41;
            this.pointsLabel2.Text = ":";
            this.pointsLabel2.Visible = false;
            // 
            // pickMin2
            // 
            this.pickMin2.Location = new System.Drawing.Point(481, 58);
            this.pickMin2.Name = "pickMin2";
            this.pickMin2.Size = new System.Drawing.Size(30, 20);
            this.pickMin2.TabIndex = 50;
            this.pickMin2.Text = "00";
            this.pickMin2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickMin2.Visible = false;
            // 
            // pickHour2
            // 
            this.pickHour2.Location = new System.Drawing.Point(440, 58);
            this.pickHour2.Name = "pickHour2";
            this.pickHour2.Size = new System.Drawing.Size(30, 20);
            this.pickHour2.TabIndex = 49;
            this.pickHour2.Text = "12";
            this.pickHour2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickHour2.Visible = false;
            // 
            // pickDate2
            // 
            this.pickDate2.Location = new System.Drawing.Point(215, 58);
            this.pickDate2.MinDate = new System.DateTime(2000, 1, 1, 0, 0, 0, 0);
            this.pickDate2.Name = "pickDate2";
            this.pickDate2.Size = new System.Drawing.Size(212, 20);
            this.pickDate2.TabIndex = 48;
            this.pickDate2.Value = new System.DateTime(2016, 1, 22, 0, 0, 0, 0);
            this.pickDate2.Visible = false;
            // 
            // pickMin
            // 
            this.pickMin.Location = new System.Drawing.Point(481, 36);
            this.pickMin.Name = "pickMin";
            this.pickMin.Size = new System.Drawing.Size(30, 20);
            this.pickMin.TabIndex = 47;
            this.pickMin.Text = "00";
            this.pickMin.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickMin.Visible = false;
            // 
            // pickHour
            // 
            this.pickHour.Location = new System.Drawing.Point(440, 36);
            this.pickHour.Name = "pickHour";
            this.pickHour.Size = new System.Drawing.Size(30, 20);
            this.pickHour.TabIndex = 46;
            this.pickHour.Text = "12";
            this.pickHour.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickHour.Visible = false;
            // 
            // pickDate
            // 
            this.pickDate.CalendarTitleBackColor = System.Drawing.Color.LightSkyBlue;
            this.pickDate.Location = new System.Drawing.Point(215, 36);
            this.pickDate.MinDate = new System.DateTime(2000, 1, 1, 0, 0, 0, 0);
            this.pickDate.Name = "pickDate";
            this.pickDate.Size = new System.Drawing.Size(212, 20);
            this.pickDate.TabIndex = 45;
            this.pickDate.Value = new System.DateTime(2016, 1, 22, 0, 0, 0, 0);
            this.pickDate.Visible = false;
            // 
            // licenseText
            // 
            this.licenseText.Location = new System.Drawing.Point(214, 48);
            this.licenseText.Name = "licenseText";
            this.licenseText.Size = new System.Drawing.Size(168, 20);
            this.licenseText.TabIndex = 51;
            this.licenseText.Visible = false;
            // 
            // FilterButton
            // 
            this.FilterButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.FilterButton.Image = ((System.Drawing.Image)(resources.GetObject("FilterButton.Image")));
            this.FilterButton.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.FilterButton.Location = new System.Drawing.Point(530, 39);
            this.FilterButton.Name = "FilterButton";
            this.FilterButton.Size = new System.Drawing.Size(68, 35);
            this.FilterButton.TabIndex = 52;
            this.FilterButton.Text = "Filter";
            this.FilterButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.FilterButton.UseVisualStyleBackColor = true;
            this.FilterButton.Click += new System.EventHandler(this.FilterButton_Click);
            // 
            // noDataText
            // 
            this.noDataText.BackColor = System.Drawing.Color.LightSteelBlue;
            this.noDataText.Enabled = false;
            this.noDataText.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.noDataText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.noDataText.ForeColor = System.Drawing.Color.Tomato;
            this.noDataText.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.noDataText.Location = new System.Drawing.Point(205, 180);
            this.noDataText.Name = "noDataText";
            this.noDataText.Size = new System.Drawing.Size(280, 106);
            this.noDataText.TabIndex = 54;
            this.noDataText.Text = "No actions during this period";
            this.noDataText.UseVisualStyleBackColor = false;
            this.noDataText.Visible = false;
            // 
            // DataBaseGrid
            // 
            this.DataBaseGrid.AllowUserToAddRows = false;
            this.DataBaseGrid.AllowUserToDeleteRows = false;
            this.DataBaseGrid.AllowUserToOrderColumns = true;
            this.DataBaseGrid.AllowUserToResizeRows = false;
            this.DataBaseGrid.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.DataBaseGrid.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            dataGridViewCellStyle1.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle1.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle1.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle1.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle1.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle1.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.DataBaseGrid.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle1;
            this.DataBaseGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.DataBaseGrid.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.ColumnName,
            this.ColumnPid,
            this.ColumnUser});
            dataGridViewCellStyle2.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle2.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle2.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle2.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle2.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle2.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.DataBaseGrid.DefaultCellStyle = dataGridViewCellStyle2;
            this.DataBaseGrid.Location = new System.Drawing.Point(12, 87);
            this.DataBaseGrid.MultiSelect = false;
            this.DataBaseGrid.Name = "DataBaseGrid";
            this.DataBaseGrid.ReadOnly = true;
            dataGridViewCellStyle3.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle3.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle3.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle3.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle3.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle3.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.DataBaseGrid.RowHeadersDefaultCellStyle = dataGridViewCellStyle3;
            this.DataBaseGrid.Size = new System.Drawing.Size(671, 345);
            this.DataBaseGrid.TabIndex = 53;
            // 
            // ColumnName
            // 
            this.ColumnName.HeaderText = "Date";
            this.ColumnName.Name = "ColumnName";
            this.ColumnName.ReadOnly = true;
            // 
            // ColumnPid
            // 
            this.ColumnPid.HeaderText = "License Plate";
            this.ColumnPid.Name = "ColumnPid";
            this.ColumnPid.ReadOnly = true;
            // 
            // ColumnUser
            // 
            this.ColumnUser.HeaderText = "In/Out";
            this.ColumnUser.Name = "ColumnUser";
            this.ColumnUser.ReadOnly = true;
            // 
            // fromLabel
            // 
            this.fromLabel.AutoSize = true;
            this.fromLabel.Location = new System.Drawing.Point(178, 39);
            this.fromLabel.Name = "fromLabel";
            this.fromLabel.Size = new System.Drawing.Size(36, 13);
            this.fromLabel.TabIndex = 55;
            this.fromLabel.Text = "From :";
            this.fromLabel.Visible = false;
            // 
            // toLabel
            // 
            this.toLabel.AutoSize = true;
            this.toLabel.Location = new System.Drawing.Point(183, 61);
            this.toLabel.Name = "toLabel";
            this.toLabel.Size = new System.Drawing.Size(26, 13);
            this.toLabel.TabIndex = 56;
            this.toLabel.Text = "To :";
            this.toLabel.Visible = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(620, 27);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(56, 58);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 57;
            this.pictureBox1.TabStop = false;
            // 
            // updatingBox
            // 
            this.updatingBox.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("updatingBox.BackgroundImage")));
            this.updatingBox.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.updatingBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.updatingBox.Location = new System.Drawing.Point(186, 189);
            this.updatingBox.Name = "updatingBox";
            this.updatingBox.Size = new System.Drawing.Size(318, 97);
            this.updatingBox.TabIndex = 58;
            this.updatingBox.TabStop = false;
            this.updatingBox.UseWaitCursor = true;
            this.updatingBox.Visible = false;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.LightSteelBlue;
            this.ClientSize = new System.Drawing.Size(695, 445);
            this.Controls.Add(this.updatingBox);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.toLabel);
            this.Controls.Add(this.fromLabel);
            this.Controls.Add(this.noDataText);
            this.Controls.Add(this.DataBaseGrid);
            this.Controls.Add(this.FilterButton);
            this.Controls.Add(this.licenseText);
            this.Controls.Add(this.pickMin2);
            this.Controls.Add(this.pickHour2);
            this.Controls.Add(this.pickDate2);
            this.Controls.Add(this.pickMin);
            this.Controls.Add(this.pickHour);
            this.Controls.Add(this.pickDate);
            this.Controls.Add(this.pointsLabel2);
            this.Controls.Add(this.filtersBox);
            this.Controls.Add(this.pointsLabel);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tsmMenu);
            this.MainMenuStrip = this.tsmMenu;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "LicensePlate Database";
            this.tsmMenu.ResumeLayout(false);
            this.tsmMenu.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.DataBaseGrid)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.updatingBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip tsmMenu;
        private System.Windows.Forms.ToolStripMenuItem tsmFileExit;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label pointsLabel;
        private System.Windows.Forms.ComboBox filtersBox;
        private System.Windows.Forms.Label pointsLabel2;
        private System.Windows.Forms.TextBox pickMin2;
        private System.Windows.Forms.TextBox pickHour2;
        private System.Windows.Forms.DateTimePicker pickDate2;
        private System.Windows.Forms.TextBox pickMin;
        private System.Windows.Forms.TextBox pickHour;
        private System.Windows.Forms.DateTimePicker pickDate;
        private System.Windows.Forms.TextBox licenseText;
        private System.Windows.Forms.Button FilterButton;
        private System.Windows.Forms.Button noDataText;
        private System.Windows.Forms.DataGridView DataBaseGrid;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnName;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnPid;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnUser;
        private System.Windows.Forms.Label fromLabel;
        private System.Windows.Forms.Label toLabel;
        private System.Windows.Forms.ToolStripMenuItem closeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem helpToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutLicensePlateDatabaseToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.ToolStripMenuItem updateToolStripMenuItem;
        private System.Windows.Forms.PictureBox updatingBox;
    }
}

