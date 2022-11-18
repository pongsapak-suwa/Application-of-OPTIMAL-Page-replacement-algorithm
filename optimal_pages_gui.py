import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from tkinter.filedialog import askopenfile

import numpy
import pandas as pd

root = tk.Tk()
root.geometry("900x540")
root.minsize(900,540)
root.maxsize(900,540)


def search_file():
        fileopen = askopenfile()
        lable_search = Label(text = fileopen ).pack()

root.title('Application-of-OPTIMAL-Page-replacement-algorithm')

head_text = tk.Label(root,text="Application-of-OPTIMAL-Page-replacement-algorithm")
head_text.grid(row=0,column=1)
my_font1=('times', 12, 'bold')
l1 = tk.Label(root,text='Read File & create DataFrame',width=30 )
l1.grid(row=1,column=1,sticky="E")
l2 = tk.Label(root,text='Number of pages',width=30 )
l2.grid(row=2,column=0,sticky="E")
search_buttom = tk.Button(root, text='Browse File', width=15,command = lambda:upload_file())
search_buttom.grid(row=1,column=0,sticky="W")
t1=Entry(root,width=40)
t1.grid(row=2,column=1,sticky="E")




def upload_file():
    l3 = tk.Label(root,text='                                      ',width=30 )
    l3.grid(row=1,column=2,sticky="E")  
     
    f_types = [('CSV files',"*.csv"),('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    l1.config(text=file) # display the path 

    df = pd.read_csv('PR1.csv' ,header=None).to_numpy()

    #print("Enter the number of frames: ")
    #num_pages =  int(input())
    run_buttom = tk.Button(root, text='run', width=15 ,command = lambda:ago(df,t1))
    run_buttom.grid(row=1,column=3,sticky="E")
    def ago(df,t1):
        a=int(t1.get())
        pages = []
        for pnum in list(df):
            pages.append(pnum)

        totality_pages = len(pages)
        frams = []
        total_frams = []
        page_falt = []
        num_falt = 0
        num_pages = a
        max_fram = 0
        frams = [None for i in range(num_pages)]
        check_optimal = [None for i in range(num_pages)]
        for i in range(0,totality_pages):
            if pages[i] not in frams:
                page_falt.append("Miss")
                num_falt+=1
                if None not in frams:
                    for j in range(len(frams)):
                        if frams[j] not in pages[i+1:]:
                            frams[j] = pages[i]
                            break
                        else:
                            check_optimal[j] = pages[i+1:].index(frams[j])
                    if pages[i] not in frams:
                        frams[check_optimal.index(max(check_optimal))] = pages[i]
                else:
                    frams[max_fram] = pages[i]
                    max_fram += 1
                
            else:
                page_falt.append("Hit")
                
            total_frams.append([])
            for t in list(frams):
                total_frams[-1].append(t)
        l5 = tk.Label(root,text='pages falut  = ',width=30 )
        l5.grid(row=3,column=0,sticky="E")
        l4 = tk.Label(root,text= num_falt ,width=30 )
        l4.grid(row=3,column=1,sticky="W")

        frame_out = Frame(root)
        frame_out.grid(row=4,column=1, columnspan = 2,sticky="W")
        scroll = Scrollbar(frame_out)
        scroll.pack(side=RIGHT, fill=Y)
        output = ttk.Treeview(frame_out,yscrollcommand=scroll.set)
        scroll.config(command=output.yview)
        output['columns'] = ('pages','pages fault','frams')
        output.column("#0", width=0,  stretch=NO)
        output.column("pages",anchor=CENTER, width=80,minwidth=80)
        output.column("pages fault",anchor=CENTER, width=80,minwidth=80)
        output.column("frams",anchor=CENTER, width=220,minwidth=220)

        output.heading("#0", text="",  anchor=CENTER)
        output.heading("pages",text="pages", anchor=CENTER)
        output.heading("pages fault",text="pages fault?", anchor=CENTER)
        output.heading("frams",text="frams", anchor=CENTER)
        output.tag_configure('blue', background= 'blue' ) 
        output.tag_configure('white', background= 'white')
        r = 'blue'
        for x in range(0,totality_pages):
            if r == 'white':
                r = 'blue'
            else:
                r = 'white'
            output.insert('','end',iid=x,values=(pages[x][0],page_falt[x],total_frams[x]),tags= ('blue',"white"))
            output.pack()
        



root.mainloop()