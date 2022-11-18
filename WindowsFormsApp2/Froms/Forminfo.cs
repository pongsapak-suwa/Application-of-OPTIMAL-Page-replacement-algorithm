using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static IronPython.Modules.PythonWeakRef;

namespace WindowsFormsApp2.Froms
{
    public partial class Forminfo : Form
    {
        int DistanceUnit = 1;
        int lef = 1;
        public Forminfo(IList<object> pages, IList<object> page_falt, IList<object> total_frams)
        {
            InitializeComponent();
            if (pages != null)
            {

                for (int i = 0; i < pages.Count; i++)
                {
                    //https://www.youtube.com/watch?v=_kkw5AnSUf0
                    // Panel new_panel = new Panel();


                    Label lbl_page = new Label();
                    this.Controls.Add(lbl_page);
                    lbl_page.Top = DistanceUnit * 87;
                    lbl_page.Left = 85;
                    lbl_page.Size = new Size(50, 35);
                    lbl_page.ForeColor = Color.DarkBlue;
                    lbl_page.BackColor = Color.LightBlue;
                    lbl_page.Text = pages[i].ToString();
                    lbl_page.TextAlign = ContentAlignment.MiddleCenter;

                    Label lbl_f = new Label();
                    this.Controls.Add(lbl_f);
                    lbl_f.Top = (DistanceUnit * 87) - 15;
                    lbl_f.Left = 155;
                    lbl_f.Size = new Size(110, 55);
                    lbl_f.ForeColor = Color.Red;
                    if(page_falt[i].ToString() == "fault")
                    {
                        lbl_f.Text = "page " + (page_falt[i].ToString());
                    }
                    else
                    {
                        lbl_f.Text = page_falt[i].ToString();
                    }
                    lbl_f.TextAlign = ContentAlignment.MiddleCenter;

                    IList<object> frams = (IList<object>)total_frams[i];
                    for (int j = 0; j < frams.Count; j++) 
                        { 
                        Label lbl_fame = new Label();
                        this.Controls.Add(lbl_fame);
                        lbl_fame.Top = DistanceUnit * 87;
                        lbl_fame.Left = 275 + (j*55);
                        lef = 135 + (j * 55);
                        lbl_fame.Size = new Size(50, 35);
                        lbl_fame.ForeColor = Color.DarkBlue;
                        lbl_fame.BackColor = Color.LightBlue;
                        if (frams[j] != null)
                        {
                            lbl_fame.Text = frams[j].ToString();
                        }
                        else
                        {
                            lbl_fame.Text = "None";
                        }
                        lbl_fame.TextAlign = ContentAlignment.MiddleCenter;
                    }
                    Label lbl_b = new Label();
                    this.Controls.Add(lbl_b);
                    lbl_b.Top = DistanceUnit * 87;
                    lbl_b.Left = 215;
                    lbl_b.Size = new Size(lef, 35);
                    lbl_b.BackColor = Color.White;
                    


                    DistanceUnit = DistanceUnit + 1;

                    //label1.Text = page_falt[i].ToString();
                }
            }
        }

    }
}
