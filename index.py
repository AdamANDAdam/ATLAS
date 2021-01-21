
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk

from tkinter import ttk
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 12)



class SeaofBTCapp(tk.Tk):
   
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "ATLAS Renewable Energy Laboratory Monash University")
        self.iconbitmap(r"C:\Users\Rahul NAmbiar\atlasnew\ATLAS\img\icon.ico")
        self.geometry("3584x2000")
        self.resizable(width=True, height=True)
        self.maxsize(3584, 2000)
        self.minsize(1500, 1000)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
    
        


        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Parameters preset",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="J-V tests",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Maximum Power Point and Stability Tracking",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        
       
    
class PageOne(tk.Frame):
    
             
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        self.var7 = tk.IntVar()
        self.var8 = tk.IntVar()
        self.var9 = tk.IntVar()
        self.var10 = tk.IntVar()
        self.var11 = tk.IntVar()
        self.var12 = tk.IntVar()
        self.var13 = tk.IntVar()
        self.var14 = tk.IntVar()
        self.var15 = tk.IntVar()
        self.var16 = tk.IntVar()
        self.var17 = tk.IntVar()
        self.var18 = tk.IntVar()
        self.var19 = tk.IntVar()
        self.var20 = tk.IntVar()
 #  radiobutton_variables       
        self.r1 = tk.IntVar()
        self.r2 = tk.IntVar()
        self.r3 = tk.IntVar()
        self.r4 = tk.IntVar()
        self.r5 = tk.IntVar()
        self.r6 = tk.IntVar()
        self.r7 = tk.IntVar()
        self.r8 = tk.IntVar()
        self.r9 = tk.IntVar()
        self.r10 = tk.IntVar()
        self.r11 = tk.IntVar()
        self.r12 = tk.IntVar()
        self.r13 = tk.IntVar()
        self.r14 = tk.IntVar()
        self.r15 = tk.IntVar()
        self.r16 = tk.IntVar()
        self.r17 = tk.IntVar()
        self.r18 = tk.IntVar()
        self.r19 = tk.IntVar()
        self.r20 = tk.IntVar()
          
# adding scroll bar 

#  parameters entry 
     
        label = tk.Label(self, text="Parameters Preset", font=('Arial',14))
        label.grid(row=0,column=0)

        button1 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=100,column=0)

        button2 = ttk.Button(self, text="Go To J-V",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=100,column=1)
        
#  cell 1
        self.label1 = tk.Label(self, text='Enter cell area 1 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=3,column=0,padx=5,pady=5)

        self.textbox1 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox1.grid(row=3,column=1)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=4,column=0,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r1,value=1)
        self.rad1.grid(row=4,column=1)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r1,value=2)
        self.rad2.grid(row=4,column=2)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=5,column=0,padx=5,pady=5)

        self.textbox2 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox2.grid(row=5,column=1)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',8))
        self.label4.grid(row=6,column=0,padx=2,pady=5)

        self.textbox3 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=12)
        self.textbox3.grid(row=6,column=1)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=7,column=0,padx=5,pady=5)

        self.textbox4 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox4.grid(row=7,column=1)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=8,column=0,padx=5,pady=5)

        self.textbox5 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox5.grid(row=8,column=1) 

#  cell 2
        
        self.label7 = tk.Label(self, text='Enter cell area 2 (cm2)',fg='black',font=('arial',12))
        self.label7.grid(row=10,column=0,padx=5,pady=5)

        self.textbox6 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox6.grid(row=10,column=1)
        
        self.label8 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label8.grid(row=11,column=0,padx=5,pady=5)
         
        
        self.rad3= tk.Radiobutton(self,text='INV',variable= self.r2,value=1)
        self.rad3.grid(row=11,column=1)
        
        self.rad4= tk.Radiobutton(self,text='PLNR',variable= self.r2,value=2)
        self.rad4.grid(row=11,column=2)
        
        
        self.label8 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label8.grid(row=12,column=0,padx=5,pady=5)

        self.textbox7 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox7.grid(row=12,column=1)
        
        
        self.label9 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label9.grid(row=13,column=0,padx=2,pady=5)

        self.textbox8 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox8.grid(row=13,column=1)
        
        
        self.labelx = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.labelx.grid(row=14,column=0,padx=5,pady=5)

        self.textbox9 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox9.grid(row=14,column=1)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=15,column=0,padx=5,pady=5)

        self.textbox10 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox10.grid(row=15,column=1, pady= 5) 

#  cell 3

         
        self.label1 = tk.Label(self, text='Enter cell area 3 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=17,column=0,padx=5,pady=5)

        self.textbox11 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox11.grid(row=17,column=1)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=18,column=0,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r3,value=1)
        self.rad1.grid(row=18,column=1)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r3,value=2)
        self.rad2.grid(row=18,column=2)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=19,column=0,padx=5,pady=5)

        self.textbox12 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox12.grid(row=19,column=1)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=20,column=0,padx=2,pady=5)

        self.textbox13 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox13.grid(row=20,column=1)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=21,column=0,padx=5,pady=5)

        self.textbox14 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox14.grid(row=21,column=1)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=22,column=0,padx=5,pady=5)

        self.textbox15 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox15.grid(row=22,column=1) 

#  cell 4 
      
        self.label1 = tk.Label(self, text='Enter cell area 4 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=25,column=0,padx=5,pady=5)

        self.textbox16 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox16.grid(row=25,column=1)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=26,column=0,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r4,value=1)
        self.rad1.grid(row=26,column=1)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r4,value=2)
        self.rad2.grid(row=26,column=2)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=27,column=0,padx=5,pady=5)

        self.textbox17 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox17.grid(row=27,column=1)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=28,column=0,padx=2,pady=5)

        self.textbox18 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox18.grid(row=29,column=1)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=30,column=0,padx=5,pady=5)

        self.textbox19 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox19.grid(row=30,column=1)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=31,column=0,padx=5,pady=5)

        self.textbox20 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox20.grid(row=31,column=1,pady=5) 

        
# cell 5 

        self.label1 = tk.Label(self, text='Enter cell area 5 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=33,column=0,padx=5,pady=5)

        self.textbox21 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox21.grid(row=33,column=1)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=34,column=0,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r5,value=1)
        self.rad1.grid(row=34,column=1)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r5,value=2)
        self.rad2.grid(row=34,column=2)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=35,column=0,padx=5,pady=5)

        self.textbox22 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox22.grid(row=35,column=1)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=36,column=0,padx=2,pady=5)

        self.textbox23 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox23.grid(row=36,column=1)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=37,column=0,padx=5,pady=5)

        self.textbox24 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox24.grid(row=37,column=1)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=38,column=0,padx=5,pady=5)

        self.textbox25 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox25.grid(row=38,column=1) 
        
        
#  cell 6 

        self.label1 = tk.Label(self, text='Enter cell area 6 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=3,column=5,padx=5,pady=5)

        self.textbox26 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox26.grid(row=3,column=6)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=4,column=5,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r6,value=1)
        self.rad1.grid(row=4,column=6)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r6,value=2)
        self.rad2.grid(row=4,column=7)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=5,column=5,padx=5,pady=5)
        
        self.textbox27= tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox27.grid(row=5,column=6)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=6,column=5,padx=2,pady=5)

        self.textbox28 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox28.grid(row=6,column=6)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=7,column=5,padx=5,pady=5)

        self.textbox29 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox29.grid(row=7,column=6)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=8,column=5,padx=5,pady=5)

        self.textbox30 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox30.grid(row=8,column=6) 
        

#  cell 7 

        self.label1 = tk.Label(self, text='Enter cell area 7 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=10,column=5,padx=5,pady=5)

        self.textbox31 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox31.grid(row=10,column=6)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=11,column=5,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r7,value=1)
        self.rad1.grid(row=11,column=6)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r7,value=2)
        self.rad2.grid(row=11,column=7)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=12,column=5,padx=5,pady=5)

        self.textbox32 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox32.grid(row=12,column=6)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=13,column=5,padx=2,pady=5)

        self.textbox33 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox33.grid(row=13,column=6)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=14,column=5,padx=5,pady=5)

        self.textbox34 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox34.grid(row=14,column=6)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=15,column=5,padx=5,pady=5)

        self.textbox35 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox35.grid(row=15,column=6) 

        
#  cell 8 

        self.label1 = tk.Label(self, text='Enter cell area 8 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=17,column=5,padx=5,pady=5)

        self.textbox36 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox36.grid(row=17,column=6)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=18,column=5,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r8,value=1)
        self.rad1.grid(row=18,column=6)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r8,value=2)
        self.rad2.grid(row=18,column=7)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=19,column=5,padx=5,pady=5)

        self.textbox37 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox37.grid(row=19,column=6)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=20,column=5,padx=2,pady=5)

        self.textbox38 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox38.grid(row=20,column=6)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=21,column=5,padx=5,pady=5)

        self.textbox39 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox39.grid(row=21,column=6)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=22,column=5,padx=5,pady=5)

        self.textbox40 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox40.grid(row=22,column=6) 

        
# cell 9 

        self.label1 = tk.Label(self, text='Enter cell area 9 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=25,column=5,padx=5,pady=5)

        self.textbox46 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox46.grid(row=25,column=6)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=26,column=5,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r9,value=1)
        self.rad1.grid(row=26,column=6)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r9,value=2)
        self.rad2.grid(row=26,column=7)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=27,column=5,padx=5,pady=5)

        self.textbox47 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox47.grid(row=27,column=6)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=28,column=5,padx=2,pady=5)

        self.textbox48 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox48.grid(row=28,column=6)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=29,column=5,padx=5,pady=5)

        self.textbox49 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox49.grid(row=29,column=6)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=30,column=5,padx=5,pady=5)

        self.textbox50 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox50.grid(row=30,column=6) 

        
#  cell 10 

        self.label1 = tk.Label(self, text='Enter cell area 10 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=32,column=5,padx=5,pady=5)

        self.textbox51 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox51.grid(row=32,column=6)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=33,column=5,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r10,value=1)
        self.rad1.grid(row=33,column=6)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r10,value=2)
        self.rad2.grid(row=33,column=7)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=34,column=5,padx=5,pady=5)

        self.textbox52 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox52.grid(row=34,column=6)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=35,column=5,padx=2,pady=5)

        self.textbox53 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox53.grid(row=35,column=6)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=36,column=5,padx=5,pady=5)

        self.textbox54 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox54.grid(row=36,column=6)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=37,column=5,padx=5,pady=5)

        self.textbox55 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox55.grid(row=37,column=6,pady=25) 


# 11-15

       #  cell 11

        self.label1 = tk.Label(self, text='Enter cell area 11 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=3,column=9,padx=5,pady=5)

        self.textbox56 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox56.grid(row=3,column=10)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=4,column=9,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r11,value=1)
        self.rad1.grid(row=4,column=10)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r11,value=2)
        self.rad2.grid(row=4,column=11)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=5,column=9,padx=5,pady=5)
        
        self.textbox57 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox57.grid(row=5,column=10)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=6,column=9,padx=2,pady=5)

        self.textbox58 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox58.grid(row=6,column=10)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=7,column=9,padx=5,pady=5)

        self.textbox59 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox59.grid(row=7,column=10)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=8,column=9,padx=5,pady=5)

        self.textbox60 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox60.grid(row=8,column=10) 
        

#  cell 12 

        self.label1 = tk.Label(self, text='Enter cell area 12 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=10,column=9,padx=5,pady=5)

        self.textbox61 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox61.grid(row=10,column=10)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=11,column=9,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r12,value=1)
        self.rad1.grid(row=11,column=10)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r12,value=2)
        self.rad2.grid(row=11,column=11)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=12,column=9,padx=5,pady=5)

        self.textbox62 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox62.grid(row=12,column=10)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=13,column=9,padx=2,pady=5)

        self.textbox63 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox63.grid(row=13,column=10)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=14,column=9,padx=5,pady=5)

        self.textbox64 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox64.grid(row=14,column=10)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=15,column=9,padx=5,pady=5)

        self.textbox65 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox65.grid(row=15,column=10) 

        
#  cell 13 

        self.label1 = tk.Label(self, text='Enter cell area 13 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=17,column=9,padx=5,pady=5)

        self.textbox66 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox66.grid(row=17,column=10)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=18,column=9,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r13,value=1)
        self.rad1.grid(row=18,column=10)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r13,value=2)
        self.rad2.grid(row=18,column=11)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=19,column=9,padx=5,pady=5)

        self.textbox67 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox67.grid(row=19,column=10)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=20,column=9,padx=2,pady=5)

        self.textbox68 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox68.grid(row=20,column=10)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=21,column=9,padx=5,pady=5)

        self.textbox69 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox69.grid(row=21,column=10)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=22,column=9,padx=5,pady=5)

        self.textbox70 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox70.grid(row=22,column=10) 

        
# cell 14

        self.label1 = tk.Label(self, text='Enter cell area 14 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=25,column=9,padx=5,pady=5)

        self.textbox71 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox71.grid(row=25,column=10)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=26,column=9,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r14,value=1)
        self.rad1.grid(row=26,column=10)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r14,value=2)
        self.rad2.grid(row=26,column=11)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=27,column=9,padx=5,pady=5)

        self.textbox72 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox72.grid(row=27,column=10)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=28,column=9,padx=2,pady=5)

        self.textbox73 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox73.grid(row=28,column=10)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=29,column=9,padx=5,pady=5)

        self.textbox74 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox74.grid(row=29,column=10)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=30,column=9,padx=5,pady=5)

        self.textbox75 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox75.grid(row=30,column=10) 

        
#  cell 15

        self.label1 = tk.Label(self, text='Enter cell area 15 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=32,column=9,padx=5,pady=5)

        self.textbox76 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox76.grid(row=32,column=10)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=33,column=9,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r15,value=1)
        self.rad1.grid(row=33,column=10)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r15,value=2)
        self.rad2.grid(row=33,column=11)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=34,column=9,padx=5,pady=5)

        self.textbox77 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox77.grid(row=34,column=10)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=35,column=9,padx=2,pady=5)

        self.textbox78 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox78.grid(row=35,column=10)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=36,column=9,padx=5,pady=5)

        self.textbox79 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox79.grid(row=36,column=10)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=37,column=9,padx=5,pady=5)

        self.textbox80 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox80.grid(row=37,column=10,pady=25)
       

# 16- 20
        
  #  cell 16

        self.label1 = tk.Label(self, text='Enter cell area 16 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=3,column=13,padx=5,pady=5)

        self.textbox81 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox81.grid(row=3,column=14)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=4,column=13,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r16,value=1)
        self.rad1.grid(row=4,column=14)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r16,value=2)
        self.rad2.grid(row=4,column=15)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=5,column=13,padx=5,pady=5)
        
        self.textbox82 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox82.grid(row=5,column=14)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=6,column=13,padx=2,pady=5)

        self.textbox83 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox83.grid(row=6,column=14)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=7,column=13,padx=5,pady=5)

        self.textbox84 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox84.grid(row=7,column=14)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=8,column=13,padx=5,pady=5)

        self.textbox85 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox85.grid(row=8,column=14) 
        

#  cell 17 

        self.label1 = tk.Label(self, text='Enter cell area 17 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=10,column=13,padx=5,pady=5)

        self.textbox86 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox86.grid(row=10,column=14)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=11,column=13,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r17,value=1)
        self.rad1.grid(row=11,column=14)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r17,value=2)
        self.rad2.grid(row=11,column=15)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=12,column=13,padx=5,pady=5)

        self.textbox87 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox87.grid(row=12,column=14)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=13,column=13,padx=2,pady=5)

        self.textbox88 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox88.grid(row=13,column=14)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=14,column=13,padx=5,pady=5)

        self.textbox89 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox89.grid(row=14,column=14)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=15,column=13,padx=5,pady=5)

        self.textbox90 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox90.grid(row=15,column=14) 

        
#  cell 18 

        self.label1 = tk.Label(self, text='Enter cell area 18 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=17,column=13,padx=5,pady=5)

        self.textbox91 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox91.grid(row=17,column=14)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=18,column=13,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r18,value=1)
        self.rad1.grid(row=18,column=14)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r18,value=2)
        self.rad2.grid(row=18,column=15)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=19,column=13,padx=5,pady=5)

        self.textbox92 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox92.grid(row=19,column=14)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=20,column=13,padx=2,pady=5)

        self.textbox93 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox93.grid(row=20,column=14)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=21,column=13,padx=5,pady=5)

        self.textbox94 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox94.grid(row=21,column=14)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=22,column=13,padx=5,pady=5)

        self.textbox95 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox95.grid(row=22,column=14) 

        
# cell 19

        self.label1 = tk.Label(self, text='Enter cell area 19 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=25,column=13,padx=5,pady=5)

        self.textbox91 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox91.grid(row=25,column=14)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=26,column=13,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r19,value=1)
        self.rad1.grid(row=26,column=14)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r19,value=2)
        self.rad2.grid(row=26,column=15)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=27,column=13,padx=5,pady=5)

        self.textbox92 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox92.grid(row=27,column=14)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=28,column=13,padx=2,pady=5)

        self.textbox93 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox93.grid(row=28,column=14)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=29,column=13,padx=5,pady=5)

        self.textbox94 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox94.grid(row=29,column=14)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=30,column=13,padx=5,pady=5)

        self.textbox95 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox95.grid(row=30,column=14) 

        
#  cell 20

        self.label1 = tk.Label(self, text='Enter cell area 20 (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=32,column=13,padx=5,pady=5)

        self.textbox96 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox96.grid(row=32,column=14)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=33,column=13,padx=5,pady=5)
         
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= self.r20,value=1)
        self.rad1.grid(row=33,column=14)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= self.r20,value=2)
        self.rad2.grid(row=33,column=15)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=34,column=13,padx=5,pady=5)

        self.textbox97 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox97.grid(row=34,column=14)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=35,column=13,padx=2,pady=5)

        self.textbox98 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox98.grid(row=35,column=14)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=36,column=13,padx=5,pady=5)

        self.textbox99 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox99.grid(row=36,column=14)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=37,column=13,padx=5,pady=5)

        self.textbox100 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5,width=5)
        self.textbox100.grid(row=37,column=14,pady=25)
       


#  right of control panel 
        
        self.label8 = tk.Label(self, text='Operating Cells',fg='black',font=('arial',12))
        self.label8.grid(row=0,column=100,padx=2,pady=20)
        
        self.label9 =tk.Label(self,text='ON/OFF',fg='dark blue',font=('arial,12'))
        self.label9.grid(row=0,column=101,padx=3,pady=20)
        
       
        
        
#get parameters 
    
        self.buttontake = ttk.Button (self, text='get values',command = self.takevalues)
        self.buttontake.grid(row = 100, column = 3, padx=10)    
        
      
#operational cells 

        self.checkbox1 = tk.Checkbutton(self, text='Cell 1', variable = self.var1)
        self.checkbox1.grid(row=2, column=100,padx=5,pady=10)
        
        self.button3 = tk.Button(self, text='On/Off', command =self.check1)
        self.button3.grid(row=2,column=101)
        
        
        self.checkbox2 = tk.Checkbutton(self,text='Cell 2', variable = self.var2)
        self.checkbox2.grid(row=3, column=100,padx=5,pady=10)
        
        self.button4 = tk.Button(self, text='On/Off', command =self.check2)
        self.button4.grid(row=3,column=101)
        
        self.checkbox3 = tk.Checkbutton(self,text='Cell 3', variable = self.var3)
        self.checkbox3.grid(row=4, column=100,padx=5,pady=10)
        
        self.button5 = tk.Button(self, text='On/Off', command =self.check3)
        self.button5.grid(row=4,column=101)
        
                               
        self.checkbox4 = tk.Checkbutton(self,text='Cell 4', variable = self.var4)
        self.checkbox4.grid(row=5, column=100,padx=5,pady=10)
        
        self.button6 = tk.Button(self, text='On/Off', command =self.check4)
        self.button6.grid(row=5,column=101)
       
                              
        self.checkbox5 = tk.Checkbutton(self,text='Cell 5', variable = self.var5)
        self.checkbox5.grid(row=6, column=100,padx=5,pady=10)
        
        self.button7 = tk.Button(self, text='On/Off', command =self.check5)
        self.button7.grid(row=6,column=101)
        
       
        self.checkbox6 = tk.Checkbutton(self,text='Cell 6', variable= self.var6)
        self.checkbox6.grid(row=7, column=100,padx=5,pady=10)
        
        self.button8 = tk.Button(self, text='On/Off', command =self.check6)
        self.button8.grid(row=7,column=101)
        
     
         
        self.checkbox7 = tk.Checkbutton(self,text='Cell 7', variable= self.var7)
        self.checkbox7.grid(row=8, column=100,padx=5,pady=10)
        
        self.button9 = tk.Button(self, text='On/Off', command =self.check7)
        self.button9.grid(row=8,column=101)
        
                               
        
        self.checkbox8 = tk.Checkbutton(self,text='Cell 8', variable= self.var8)
        self.checkbox8.grid(row=9, column=100,padx=5,pady=10)
        
        self.button10 = tk.Button(self, text='On/Off', command =self.check8)
        self.button10.grid(row=9,column=101)
        
     
        self.checkbox9 = tk.Checkbutton(self,text='Cell 9', variable= self.var9)
        self.checkbox9.grid(row=10, column=100,padx=5,pady=10)
        
        self.button11 = tk.Button(self, text='On/Off', command =self.check9)
        self.button11.grid(row=10,column=101)
        
        
        self.checkbox10 = tk.Checkbutton(self,text='Cell 10', variable=self.var10)
        self.checkbox10.grid(row=11, column=100,padx=5,pady=10)
        
        
        self.button12 = tk.Button(self, text='On/Off', command =self.check10)
        self.button12.grid(row=11,column=101)
    
                              
        
        self.checkbox11 = tk.Checkbutton(self,text='Cell 11', variable=self.var11)
        self.checkbox11.grid(row=12, column=100,padx=5,pady=10)
        
        
        self.button13 = tk.Button(self, text='On/Off', command =self.check11)
        self.button13.grid(row=12,column=101)

        
        self.checkbox12 = tk.Checkbutton(self,text='Cell 12', variable=self.var12)
        self.checkbox12.grid(row=13, column=100,padx=5,pady=10)
        
        
        self.button14 = tk.Button(self, text='On/Off', command =self.check12)
        self.button14.grid(row=13,column=101)
    
        
        self.checkbox13 = tk.Checkbutton(self,text='Cell 13', variable=self.var13)
        self.checkbox13.grid(row=14, column=100,padx=5,pady=10)
        
        
        self.button15 = tk.Button(self, text='On/Off', command =self.check13)
        self.button15.grid(row=14,column=101)
        
        
        self.checkbox14 = tk.Checkbutton(self,text='Cell 14', variable=self.var14)
        self.checkbox14.grid(row=15, column=100,padx=5,pady=10)
        
        
        self.button16 = tk.Button(self, text='On/Off', command =self.check14)
        self.button16.grid(row=15,column=101)
     
        
      
        self.checkbox15 = tk.Checkbutton(self,text='Cell 15', variable=self.var15)
        self.checkbox15.grid(row=16, column=100,padx=5,pady=10)
        
        
        self.button17 = tk.Button(self, text='On/Off', command =self.check15)
        self.button17.grid(row=16,column=101)
        
    
        self.checkbox16 = tk.Checkbutton(self,text='Cell 16', variable=self.var16)
        self.checkbox16.grid(row=17, column=100,padx=5,pady=10) 
        
        
        self.button18 = tk.Button(self, text='On/Off', command =self.check16)
        self.button18.grid(row=17,column=101)
        
        
        self.checkbox17 = tk.Checkbutton(self,text='Cell 17', variable=self.var17)
        self.checkbox17.grid(row=18, column=100,padx=5,pady=10)
        
        
        self.button19 = tk.Button(self, text='On/Off', command =self.check17)
        self.button19.grid(row=18,column=101)
     
                             
        self.checkbox18 = tk.Checkbutton(self,text='Cell 18', variable=self.var18)
        self.checkbox18.grid(row=19, column=100,padx=5,pady=10)
        
        
        self.button20 = tk.Button(self, text='On/Off', command =self.check18)
        self.button20.grid(row=19,column=101)
       
       
        self.checkbox19 = tk.Checkbutton(self,text='Cell 19', variable=self.var19)
        self.checkbox19.grid(row=20, column=100,padx=5,pady=10)
        
        
        self.button21 = tk.Button(self, text='On/Off', command =self.check19)
        self.button21.grid(row=20,column=101)
        
      
        self.checkbox20 = tk.Checkbutton(self,text='Cell 20', variable=self.var20)
        self.checkbox20.grid(row=21, column=100,padx=5,pady=10)
        
        
        self.button22 = tk.Button(self, text='On/Off', command =self.check20)
        self.button22.grid(row=21,column=101)
        
      
        
 #function to operate the cells    
    def check1(self):
        
        if self.var1.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=2,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=2,column=102,padx=15)
         print('off')
            
    def check2(self):       
        
        if self.var2.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=3,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=3,column=102,padx=15)
         print('off')
         
    def check3(self):
        
        if self.var3.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=4,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=4,column=102,padx=15)
         print('off')
         
    def check4(self):
        
        if self.var4.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=5,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=5,column=102,padx=15)
         print('off')
         
         
    def check5(self):
        
        if self.var5.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=6,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=6,column=102,padx=15)
         print('off')
         
         
    def check6(self):
        
        if self.var6.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=7,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=7,column=102,padx=15)
         print('off')
         
         
    def check7(self):
        
        if self.var7.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=8,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=8,column=102,padx=15)
         print('off')
         
    def check8(self):
        
        if self.var8.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=9,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=9,column=102,padx=15)
         print('off')
         
    def check9(self):
        
        if self.var9.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=10,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=10,column=102,padx=15)
         print('off')
         
    def check10(self):
        
        if self.var10.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=11,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=11,column=102,padx=15)
         print('off')
         
    def check11(self):
        
        if self.var11.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=12,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=12,column=102,padx=15)
         print('off')
         
    def check12(self):
        
        if self.var12.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=13,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=13,column=102,padx=15)
         print('off')
         
    def check13(self):
        
        if self.var13.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=14,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=14,column=102,padx=15)
         print('off')
         
    def check14(self):
        
        if self.var14.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=15,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=15,column=102,padx=15)
         print('off')
         
    def check15(self):
        
        if self.var15.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=16,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=16,column=102,padx=15)
         print('off')
         
    def check16(self):
        
        if self.var16.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=17,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=17,column=102,padx=15)
         print('off')
         
    def check17(self):
        
        if self.var17.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=18,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=18,column=102,padx=15)
         print('off')
         
    def check18(self):
        
        if self.var18.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=19,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=19,column=102,padx=15)
         print('off')
         
    def check19(self):
        
        if self.var19.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=20,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=20,column=102,padx=15)
         print('off')
         
    def check20(self):
        
        if self.var20.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=21,column=102,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=21,column=102,padx=15)
         print('off')
         
 #function to print the inputs        
    def takevalues(self):
        
        print(self.textbox1.get())
        print(self.textbox2.get())
        print(self.textbox3.get())
        print(self.textbox4.get())
        print(self.textbox5.get())
        print(self.textbox6.get())
        print(self.textbox7.get())
        print(self.textbox8.get())
        print(self.textbox9.get())
        print(self.textbox10.get())
        print(self.textbox11.get())
        print(self.textbox12.get())
        print(self.textbox13.get())
        print(self.textbox14.get())
        print(self.textbox15.get())
        print(self.textbox16.get())
        print(self.textbox17.get())
        print(self.textbox18.get())
        print(self.textbox19.get())
        print(self.textbox20.get())
        print(self.textbox21.get())
        print(self.textbox22.get())
        print(self.textbox23.get())
        print(self.textbox24.get())
        print(self.textbox25.get())
        print(self.textbox26.get())
        print(self.textbox27.get())
        print(self.textbox28.get())
        print(self.textbox29.get())
        print(self.textbox30.get())
        print(self.textbox31.get())
        print(self.textbox32.get())
        print(self.textbox33.get())
        print(self.textbox34.get())
        print(self.textbox35.get())
        print(self.textbox36.get())
        print(self.textbox37.get())
        print(self.textbox38.get())
        print(self.textbox39.get())
        print(self.textbox40.get())
        print(self.textbox41.get())
        print(self.textbox42.get())
        print(self.textbox43.get())
        print(self.textbox44.get())
        print(self.textbox45.get())
        print(self.textbox46.get())
        print(self.textbox47.get())
        print(self.textbox48.get())
        print(self.textbox49.get())
        print(self.textbox50.get())
        print(self.textbox51.get())
     
       
        
      
         
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
#        #fig, (ax1, ax2) = f.subplots(2)
#        #fig.suptitle('Vertically stacked subplots')
#        #ax1.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
#        #ax2.plot([1,2,3,4,5,6,7,8], -[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(521)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(522)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(522)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(523)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(524)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(525)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(526)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(527)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(528)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(529)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        a = f.add_subplot(529)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#        
        
        

        k = plt.figure(0)
        plots = []

        for i in range(5):
            for j in range(4):
                ax = plt.subplot2grid((5,4), (i,j))
                ax.scatter(range(20),range(20)+np.random.randint(-5,5,20))
                
        canvas = FigureCanvasTkAgg(k, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        

app = SeaofBTCapp()
app.mainloop()