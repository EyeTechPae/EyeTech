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
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle7 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle8 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle9 = new System.Windows.Forms.DataGridViewCellStyle();
            this.tsmMenu = new System.Windows.Forms.MenuStrip();
            this.tsmFileExit = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
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
            this.tsmMenu.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.DataBaseGrid)).BeginInit();
            this.SuspendLayout();
            // 
            // tsmMenu
            // 
            this.tsmMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmFileExit});
            this.tsmMenu.Location = new System.Drawing.Point(0, 0);
            this.tsmMenu.Name = "tsmMenu";
            this.tsmMenu.Size = new System.Drawing.Size(695, 24);
            this.tsmMenu.TabIndex = 1;
            this.tsmMenu.Text = "File";
            // 
            // tsmFileExit
            // 
            this.tsmFileExit.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.exitToolStripMenuItem});
            this.tsmFileExit.Name = "tsmFileExit";
            this.tsmFileExit.Size = new System.Drawing.Size(37, 20);
            this.tsmFileExit.Text = "&File";
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.exitToolStripMenuItem.Text = "&New Register";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.NewRegister);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(15, 46);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(49, 13);
            this.label1.TabIndex = 30;
            this.label1.Text = "Filter by :";
            // 
            // pointsLabel
            // 
            this.pointsLabel.AutoSize = true;
            this.pointsLabel.Location = new System.Drawing.Point(554, 36);
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
            this.filtersBox.Location = new System.Drawing.Point(83, 41);
            this.filtersBox.Name = "filtersBox";
            this.filtersBox.Size = new System.Drawing.Size(173, 21);
            this.filtersBox.TabIndex = 34;
            this.filtersBox.SelectedIndexChanged += new System.EventHandler(this.filtersBox_SelectedIndexChanged);
            // 
            // pointsLabel2
            // 
            this.pointsLabel2.AutoSize = true;
            this.pointsLabel2.Location = new System.Drawing.Point(554, 58);
            this.pointsLabel2.Name = "pointsLabel2";
            this.pointsLabel2.Size = new System.Drawing.Size(10, 13);
            this.pointsLabel2.TabIndex = 41;
            this.pointsLabel2.Text = ":";
            this.pointsLabel2.Visible = false;
            // 
            // pickMin2
            // 
            this.pickMin2.Location = new System.Drawing.Point(564, 53);
            this.pickMin2.Name = "pickMin2";
            this.pickMin2.Size = new System.Drawing.Size(30, 20);
            this.pickMin2.TabIndex = 50;
            this.pickMin2.Text = "00";
            this.pickMin2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickMin2.Visible = false;
            // 
            // pickHour2
            // 
            this.pickHour2.Location = new System.Drawing.Point(523, 53);
            this.pickHour2.Name = "pickHour2";
            this.pickHour2.Size = new System.Drawing.Size(30, 20);
            this.pickHour2.TabIndex = 49;
            this.pickHour2.Text = "12";
            this.pickHour2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickHour2.Visible = false;
            // 
            // pickDate2
            // 
            this.pickDate2.Location = new System.Drawing.Point(298, 53);
            this.pickDate2.MinDate = new System.DateTime(2000, 1, 1, 0, 0, 0, 0);
            this.pickDate2.Name = "pickDate2";
            this.pickDate2.Size = new System.Drawing.Size(212, 20);
            this.pickDate2.TabIndex = 48;
            this.pickDate2.Value = new System.DateTime(2016, 1, 22, 0, 0, 0, 0);
            this.pickDate2.Visible = false;
            // 
            // pickMin
            // 
            this.pickMin.Location = new System.Drawing.Point(564, 31);
            this.pickMin.Name = "pickMin";
            this.pickMin.Size = new System.Drawing.Size(30, 20);
            this.pickMin.TabIndex = 47;
            this.pickMin.Text = "00";
            this.pickMin.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickMin.Visible = false;
            // 
            // pickHour
            // 
            this.pickHour.Location = new System.Drawing.Point(523, 31);
            this.pickHour.Name = "pickHour";
            this.pickHour.Size = new System.Drawing.Size(30, 20);
            this.pickHour.TabIndex = 46;
            this.pickHour.Text = "12";
            this.pickHour.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.pickHour.Visible = false;
            // 
            // pickDate
            // 
            this.pickDate.Location = new System.Drawing.Point(298, 31);
            this.pickDate.MinDate = new System.DateTime(2000, 1, 1, 0, 0, 0, 0);
            this.pickDate.Name = "pickDate";
            this.pickDate.Size = new System.Drawing.Size(212, 20);
            this.pickDate.TabIndex = 45;
            this.pickDate.Value = new System.DateTime(2016, 1, 22, 0, 0, 0, 0);
            this.pickDate.Visible = false;
            // 
            // licenseText
            // 
            this.licenseText.Location = new System.Drawing.Point(304, 43);
            this.licenseText.Name = "licenseText";
            this.licenseText.Size = new System.Drawing.Size(168, 20);
            this.licenseText.TabIndex = 51;
            this.licenseText.Visible = false;
            // 
            // FilterButton
            // 
            this.FilterButton.Image = ((System.Drawing.Image)(resources.GetObject("FilterButton.Image")));
            this.FilterButton.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.FilterButton.Location = new System.Drawing.Point(609, 34);
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
            this.noDataText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.noDataText.ForeColor = System.Drawing.Color.OrangeRed;
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
            dataGridViewCellStyle7.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle7.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle7.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle7.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle7.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle7.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle7.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.DataBaseGrid.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle7;
            this.DataBaseGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.DataBaseGrid.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.ColumnName,
            this.ColumnPid,
            this.ColumnUser});
            dataGridViewCellStyle8.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle8.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle8.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle8.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle8.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle8.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle8.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.DataBaseGrid.DefaultCellStyle = dataGridViewCellStyle8;
            this.DataBaseGrid.Location = new System.Drawing.Point(12, 79);
            this.DataBaseGrid.Name = "DataBaseGrid";
            this.DataBaseGrid.ReadOnly = true;
            dataGridViewCellStyle9.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle9.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle9.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle9.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle9.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle9.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle9.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.DataBaseGrid.RowHeadersDefaultCellStyle = dataGridViewCellStyle9;
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
            this.fromLabel.Location = new System.Drawing.Point(261, 34);
            this.fromLabel.Name = "fromLabel";
            this.fromLabel.Size = new System.Drawing.Size(36, 13);
            this.fromLabel.TabIndex = 55;
            this.fromLabel.Text = "From :";
            this.fromLabel.Visible = false;
            // 
            // toLabel
            // 
            this.toLabel.AutoSize = true;
            this.toLabel.Location = new System.Drawing.Point(266, 56);
            this.toLabel.Name = "toLabel";
            this.toLabel.Size = new System.Drawing.Size(26, 13);
            this.toLabel.TabIndex = 56;
            this.toLabel.Text = "To :";
            this.toLabel.Visible = false;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.Color.LightSteelBlue;
            this.ClientSize = new System.Drawing.Size(695, 436);
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
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip tsmMenu;
        private System.Windows.Forms.ToolStripMenuItem tsmFileExit;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
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
    }
}

