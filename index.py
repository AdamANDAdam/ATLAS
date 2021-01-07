
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
        self.geometry("1400x1200")
        self.resizable(width=False, height=False)
        self.maxsize(1400, 1200)
        self.minsize(1400, 1200)
        
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
        
        global r
        
        global var
        
        
        
        
        
    
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
        
          
        
        
# parameters entry
     
        label = tk.Label(self, text="Parameters Preset", font=('Arial',14))
        label.grid(row=0,column=0)

        button1 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=20,column=0)

        button2 = ttk.Button(self, text="Go To J-V",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=20,column=1)
    
        self.label1 = tk.Label(self, text='Enter cell area (cm2)',fg='black',font=('arial',12))
        self.label1.grid(row=3,column=0,padx=5,pady=10)

        self.textbox1 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5)
        self.textbox1.grid(row=3,column=1)
        
        self.label2 = tk.Label(self, text='Device type',fg='black',font=('arial',12))
        self.label2.grid(row=4,column=0,padx=5,pady=10)
         
        r = int()
        
        self.rad1= tk.Radiobutton(self,text='INV',variable= r,value=1)
        self.rad1.grid(row=4,column=1)
        
        self.rad2= tk.Radiobutton(self,text='PLNR',variable= r,value=2)
        self.rad2.grid(row=4,column=2)
        
        
        self.label3 = tk.Label(self, text='Start Voltage',fg='black',font=('arial',12))
        self.label3.grid(row=5,column=0,padx=5,pady=10)

        self.textbox2 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5)
        self.textbox2.grid(row=5,column=1)
        
        
        self.label4 = tk.Label(self, text='End Voltage',fg='black',font=('arial',12))
        self.label4.grid(row=6,column=0,padx=2,pady=10)

        self.textbox3 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5)
        self.textbox3.grid(row=6,column=1)
        
        
        self.label5 = tk.Label(self, text='Increment step',fg='black',font=('arial',12))
        self.label5.grid(row=7,column=0,padx=5,pady=10)

        self.textbox4 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5)
        self.textbox4.grid(row=7,column=1)
        
        
        self.label6 = tk.Label(self, text='Setlling time',fg='black',font=('arial',12))
        self.label6.grid(row=8,column=0,padx=5,pady=10)

        self.textbox5 = tk.Entry(self,fg='black',font=('bold',11),borderwidth=5)
        self.textbox5.grid(row=8,column=1)
        
        
        self.label8 = tk.Label(self, text='Operating Cells',fg='black',font=('arial',12))
        self.label8.grid(row=0,column=7,padx=2,pady=10)
        
        self.label9 =tk.Label(self,text='ON/OFF',fg='dark blue',font=('arial,12'))
        self.label9.grid(row=0,column=8,padx=3,pady=10)
        
       
        
        
#get parameters 
    
        self.buttontake = ttk.Button (self, text='get values',command = self.takevalues)
        self.buttontake.grid(row = 20, column = 3, padx=10)    
        
      
#operational cells 

        self.checkbox1 = tk.Checkbutton(self, text='Cell 1', variable = self.var1)
        self.checkbox1.grid(row=2, column=7,padx=5,pady=10)
        
        self.button3 = tk.Button(self, text='On/Off', command =self.check1)
        self.button3.grid(row=2,column=8)
        
        
        self.checkbox2 = tk.Checkbutton(self,text='Cell 2', variable = self.var2)
        self.checkbox2.grid(row=3, column=7,padx=5,pady=10)
        
        self.button4 = tk.Button(self, text='On/Off', command =self.check2)
        self.button4.grid(row=3,column=8)
        
        self.checkbox3 = tk.Checkbutton(self,text='Cell 3', variable = self.var3)
        self.checkbox3.grid(row=4, column=7,padx=5,pady=10)
        
        self.button5 = tk.Button(self, text='On/Off', command =self.check3)
        self.button5.grid(row=4,column=8)
        
                               
        self.checkbox4 = tk.Checkbutton(self,text='Cell 4', variable = self.var4)
        self.checkbox4.grid(row=5, column=7,padx=5,pady=10)
        
        self.button6 = tk.Button(self, text='On/Off', command =self.check4)
        self.button6.grid(row=5,column=8)
       
                              
        self.checkbox5 = tk.Checkbutton(self,text='Cell 5', variable = self.var5)
        self.checkbox5.grid(row=6, column=7,padx=5,pady=10)
        
        self.button7 = tk.Button(self, text='On/Off', command =self.check5)
        self.button7.grid(row=6,column=8)
        
       
        self.checkbox6 = tk.Checkbutton(self,text='Cell 6', variable= self.var6)
        self.checkbox6.grid(row=7, column=7,padx=5,pady=10)
        
        self.button8 = tk.Button(self, text='On/Off', command =self.check6)
        self.button8.grid(row=7,column=8)
        
     
         
        self.checkbox7 = tk.Checkbutton(self,text='Cell 7', variable= self.var7)
        self.checkbox7.grid(row=8, column=7,padx=5,pady=10)
        
        self.button9 = tk.Button(self, text='On/Off', command =self.check7)
        self.button9.grid(row=8,column=8)
        
                               
        
        self.checkbox8 = tk.Checkbutton(self,text='Cell 8', variable= self.var8)
        self.checkbox8.grid(row=9, column=7,padx=5,pady=10)
        
        self.button10 = tk.Button(self, text='On/Off', command =self.check8)
        self.button10.grid(row=9,column=8)
        
     
        self.checkbox9 = tk.Checkbutton(self,text='Cell 9', variable= self.var9)
        self.checkbox9.grid(row=10, column=7,padx=5,pady=10)
        
        self.button11 = tk.Button(self, text='On/Off', command =self.check9)
        self.button11.grid(row=10,column=8)
        
        
        self.checkbox10 = tk.Checkbutton(self,text='Cell 10', variable=self.var10)
        self.checkbox10.grid(row=11, column=7,padx=5,pady=10)
        
        
        self.button12 = tk.Button(self, text='On/Off', command =self.check10)
        self.button12.grid(row=11,column=8)
    
                              
        
        self.checkbox11 = tk.Checkbutton(self,text='Cell 11', variable=self.var11)
        self.checkbox11.grid(row=12, column=7,padx=5,pady=10)
        
        
        self.button13 = tk.Button(self, text='On/Off', command =self.check11)
        self.button13.grid(row=12,column=8)

        
        self.checkbox12 = tk.Checkbutton(self,text='Cell 12', variable=self.var12)
        self.checkbox12.grid(row=13, column=7,padx=5,pady=10)
        
        
        self.button14 = tk.Button(self, text='On/Off', command =self.check12)
        self.button14.grid(row=13,column=8)
    
        
        self.checkbox13 = tk.Checkbutton(self,text='Cell 13', variable=self.var13)
        self.checkbox13.grid(row=14, column=7,padx=5,pady=10)
        
        
        self.button15 = tk.Button(self, text='On/Off', command =self.check13)
        self.button15.grid(row=14,column=8)
        
        
        self.checkbox14 = tk.Checkbutton(self,text='Cell 14', variable=self.var14)
        self.checkbox14.grid(row=15, column=7,padx=5,pady=10)
        
        
        self.button16 = tk.Button(self, text='On/Off', command =self.check14)
        self.button16.grid(row=15,column=8)
     
        
      
        self.checkbox15 = tk.Checkbutton(self,text='Cell 15', variable=self.var15)
        self.checkbox15.grid(row=16, column=7,padx=5,pady=10)
        
        
        self.button17 = tk.Button(self, text='On/Off', command =self.check15)
        self.button17.grid(row=16,column=8)
        
    
        self.checkbox16 = tk.Checkbutton(self,text='Cell 16', variable=self.var16)
        self.checkbox16.grid(row=17, column=7,padx=5,pady=10) 
        
        
        self.button18 = tk.Button(self, text='On/Off', command =self.check16)
        self.button18.grid(row=17,column=8)
        
        
        self.checkbox17 = tk.Checkbutton(self,text='Cell 17', variable=self.var17)
        self.checkbox17.grid(row=18, column=7,padx=5,pady=10)
        
        
        self.button19 = tk.Button(self, text='On/Off', command =self.check17)
        self.button19.grid(row=18,column=8)
     
                             
        self.checkbox18 = tk.Checkbutton(self,text='Cell 18', variable=self.var18)
        self.checkbox18.grid(row=19, column=7,padx=5,pady=10)
        
        
        self.button20 = tk.Button(self, text='On/Off', command =self.check18)
        self.button20.grid(row=19,column=8)
       
       
        self.checkbox19 = tk.Checkbutton(self,text='Cell 19', variable=self.var19)
        self.checkbox19.grid(row=20, column=7,padx=5,pady=10)
        
        
        self.button21 = tk.Button(self, text='On/Off', command =self.check19)
        self.button21.grid(row=20,column=8)
        
      
        self.checkbox20 = tk.Checkbutton(self,text='Cell 20', variable=self.var20)
        self.checkbox20.grid(row=21, column=7,padx=5,pady=10)
        
        
        self.button22 = tk.Button(self, text='On/Off', command =self.check20)
        self.button22.grid(row=21,column=8)
        
      
        
 #function to operate the cells    
    def check1(self):
        
        if self.var1.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=2,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=2,column=10,padx=15)
         print('off')
            
    def check2(self):       
        
        if self.var2.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=3,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=3,column=10,padx=15)
         print('off')
         
    def check3(self):
        
        if self.var3.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=4,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=4,column=10,padx=15)
         print('off')
         
    def check4(self):
        
        if self.var4.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=5,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=5,column=10,padx=15)
         print('off')
         
         
    def check5(self):
        
        if self.var5.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=6,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=6,column=10,padx=15)
         print('off')
         
         
    def check6(self):
        
        if self.var6.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=7,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=7,column=10,padx=15)
         print('off')
         
         
    def check7(self):
        
        if self.var7.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=8,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=8,column=10,padx=15)
         print('off')
         
    def check8(self):
        
        if self.var8.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=9,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=9,column=10,padx=15)
         print('off')
         
    def check9(self):
        
        if self.var9.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=10,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=10,column=10,padx=15)
         print('off')
         
    def check10(self):
        
        if self.var10.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=11,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=11,column=10,padx=15)
         print('off')
         
    def check11(self):
        
        if self.var11.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=12,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=12,column=10,padx=15)
         print('off')
         
    def check12(self):
        
        if self.var12.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=13,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=13,column=10,padx=15)
         print('off')
         
    def check13(self):
        
        if self.var13.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=14,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=14,column=10,padx=15)
         print('off')
         
    def check14(self):
        
        if self.var14.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=15,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=15,column=10,padx=15)
         print('off')
         
    def check15(self):
        
        if self.var15.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=16,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=16,column=10,padx=15)
         print('off')
         
    def check16(self):
        
        if self.var16.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=17,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=17,column=10,padx=15)
         print('off')
         
    def check17(self):
        
        if self.var17.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=18,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=18,column=10,padx=15)
         print('off')
         
    def check18(self):
        
        if self.var18.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=19,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=19,column=10,padx=15)
         print('off')
         
    def check19(self):
        
        if self.var19.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=20,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=20,column=10,padx=15)
         print('off')
         
    def check20(self):
        
        if self.var20.get()==1:   
         self.label10 = tk.Label(self, text='ON',fg='green')
         self.label10.grid(row=21,column=10,padx=15)
         print('on')
        else:
         self.label10 = tk.Label(self,text='OFF',fg='red')
         self.label10.grid(row=21,column=10,padx=15)
         print('off')
         
 #function to print the inputs        
    def takevalues(self):
        
        print(self.textbox1.get())
        print(self.textbox2.get())
        print(self.textbox3.get())
        print(self.textbox4.get())
        print(self.textbox5.get())
        
       
    
         
     
       
        
      
         
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