from tkinter import *


class Main():
    
    def __init__(self,parent):
        self.parent=parent
        self.parent.title("Rate Calculator")
        self.parent.geometry("400x320+420+150")
        self.amt=StringVar()
        self.gamt=StringVar()
        self.t=StringVar()
        self.p=StringVar()
        self.widgets()
        
        
    def widgets(self):
        
        frame1=Frame(self.parent)
        self.frame1=frame1
        
        Entry(frame1,textvariable=self.p,width=56).grid(row=0,columnspan=3,sticky=W)
        Entry(frame1,textvariable=self.gamt,width=12).grid(row=1,column=1,columnspan=2,sticky=W)
        Button(frame1,text=" ADD ",width=15,height=2,command=self.add).grid(row=1,column=2,columnspan=3,pady=5,sticky=W)
        Button(frame1,text=" calculate ",width=15,height=3,command=self.cal).grid(row=2,columnspan=2,pady=5)
        Button(frame1,text=" Close ",width=15,height=3,command=self.close).grid(row=2,column=2,columnspan=3,pady=5)
        frame1.pack(padx=1,pady=1)
    
    
    
    def add(self):
        tt=[]
        self.t=self.gamt.get()
        tt.append(self.t)
        self.p.set(tt)
        self.frame1.pack_forget()
        self..delete(0,END)
        self.widgets()
        
        
        
        print(self.t)
    def cal(self):
        pass
    def close(self):
        self.parent.destroy()
        
if __name__=="__main__":
    root=Tk()
    Main(root)
    root.mainloop()
   
