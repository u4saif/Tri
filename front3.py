from tkinter import *

expression=""
n=1

def press(num):
    global n
    global expression 
    if num=="+":
        n=n+1
    else:
        pass
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
    print(n)
def result(expression,n,x,t,gt):
    win2=Tk()
    win2.title("Result")
    win2.geometry('580x280+400+120')
    l1=Label(win2,text="Channel cost:",font=('Comic Sans MS',15))
    l1.grid(row=0,column=0,sticky=W)
    l2=Label(win2,text=expression,font=('Comic Sans MS',15))
    l2.grid(row=0,column=1,sticky=W)
    st="Total Channels selected:"+str(n) 
    l3=Label(win2,text=st,font=('Comic Sans MS',15))
    l3.grid(row=1,column=0,sticky=W)
    amt="130\n"+"+"+str(x)+"\n+"+str(t)+"\nGST 18% "
    l4=Label(win2,text=amt,font=('Comic Sans MS',15))
    l4.grid(row=2,column=1,sticky=W)
    l5=Label(win2,text="-----------------------------------------")
    l5.grid(row=3,column=0,columnspan=2)
    l6=Label(win2,text=gt,font=('Comic Sans MS',15))
    l6.grid(row=4,column=1,sticky=W)
    
    b1=Button(win2,text="close",command=close)
    b1.grid(row=2,column=2,width=10,height=10)
    root.mainloop()

def equalpress(equation):
      # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
        global n
        print(expression)
        gt=1  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
        
        if n<25:
            t=int(total)
            gt=((t+130+20)*0.18)+(t+130+20)
            print(list(expression))
            equation.set(gt) 
            result(expression,n,20,t,gt)
    
        elif 25<n<50:
            t=int(total)
            gt=((t+130+40)*0.18)+(t+130+20)
            print(list(expression))
  
            equation.set(gt)
        elif 50<n<75:
            t=int(total)
            gt=((t+130+60)*0.18)+(t+130+20)
            print(list(expression))
  
            equation.set(gt)
        elif 75<n<100:
            t=int(total)
            gt=((t+130+40)*0.18)+(t+130+20)
            print(list(expression))
  
            equation.set(gt)
        else:
            t=int(total)
            gt=((t+130+40)*0.18)+(t+130+20)
            print(list(expression))
  
            equation.set(gt)
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
        n=1
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
        
if __name__=="__main__":
    root=Tk()
    root.title("Tria Calculator")
    root.geometry("360x350+400+129")
    
    equation=StringVar()
    expression_field =Entry(root, textvariable=equation,width=29,font=('Comic Sans MS',15))
    expression_field.grid(row=0,columnspan=7)
    equation.set('Add Channel list to calculate') 
#-------------------------------------------------------------------------------
    buttonSum=Button(root,text=" Sum \n All",command=lambda:equalpress(equation),height=8,width=15,fg="#fff",bg="#9CE1CA")
    buttonSum.grid(row=1,column=0,rowspan=3,columnspan=3)
#----------------------------------------------------------------------------------    
    button1 = Button(root, text=' 1 ',command=lambda: press(1), height=2, width=10) 
    button1.grid(row=1, column=4)
    button2 = Button(root, text=' 2 ',command=lambda: press(2), height=2, width=10) 
    button2.grid(row=1, column=5)
    button3 = Button(root, text=' 3 ',command=lambda: press(3), height=2, width=10) 
    button3.grid(row=1, column=6)
#----------------------------------------------------------------------------------
    button4 = Button(root, text=' 4 ',command=lambda: press(4), height=2, width=10) 
    button4.grid(row=2, column=4)
    button5 = Button(root, text=' 5 ',command=lambda: press(5), height=2, width=10) 
    button5.grid(row=2, column=5)
    button6= Button(root, text=' 6 ',command=lambda: press(6), height=2, width=10) 
    button6.grid(row=2, column=6)
#----------------------------------------------------------------------------------
    button7 = Button(root, text=' 7 ',command=lambda: press(7), height=2, width=10) 
    button7.grid(row=3, column=4)
    button8 = Button(root, text=' 8 ',command=lambda: press(8), height=2, width=10) 
    button8.grid(row=3, column=5)
    button9 = Button(root, text=' 9 ',command=lambda: press(9), height=2, width=10) 
    button9.grid(row=3, column=6)
#----------------------------------------------------------------------------------
    buttonAdd = Button(root, text='  ADD  ',command=lambda: press('+'), height=2, width=21) 
    buttonAdd.grid(row=4,column=3,columnspan=3,pady=5)
    button0= Button(root, text=' 0 ',command=lambda: press(0), height=2, width=10) 
    button0.grid(row=4, column=6)
     
#----------------------------------------------------------------------------------

    root.mainloop()
