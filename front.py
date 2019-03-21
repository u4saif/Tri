from tkinter import *

expression=""
n=1

def result(expression,n,x,t,gt):
    global win2
    global equation
    equation.set("")
    win2=Tk()
    win2.title("Result")
    win2.geometry('562x340+400+120')
    win2.iconbitmap(r'C:\Users\saif\Documents\Tri\tv.ico')
    e2=expression
    l1=Label(win2,text="Channels List:",font=('Comic Sans MS',15))
    l1.grid(row=0,column=0,sticky=W)
    l2=Label(win2,text=e2,font=('Comic Sans MS',15))
    l2.grid(row=0,column=1,sticky=W)
    st="Total Channels selected:"+str(n) 
    l3=Label(win2,text=st,font=('Comic Sans MS',15))
    l3.grid(row=1,column=0,sticky=W)
    samt="Base Cost:\n FTA \n selected Channel cost"
    
    l7=Label(win2,text=samt,font=('Comic Sans MS',15))
    l7.grid(row=2,column=0,sticky=W)
    
    amt="\n130\n"+"+"+str(x)+"\n+"+str(t)+"\nGST 18% "
    l4=Label(win2,text=amt,font=('Comic Sans MS',15))
    l4.grid(row=2,column=1,sticky=W)
    l5=Label(win2,text="------------------------------------------------------------------------")
    l5.grid(row=3,column=0,columnspan=9)
    
    l8=Label(win2,text='Grand Total : ₹',font=('Comic Sans MS',15))
    l8.grid(row=4,column=0,sticky=W)
    
    l6=Label(win2,text=gt,font=('Comic Sans MS',15))
    l6.grid(row=4,column=1,sticky=W)

    b1=Button(win2,text="close",command=close,width=25,height=3,fg="#fff",bg="red")
    b1.grid(row=6,column=0,columnspan=3)
    win2.mainloop()
def close():
    win2.destroy()

def clear(equation):
    global expression
    global n 
    
    equation.set("0")
    expression= ""
    n=1

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
            t=float(total)
            gt=((t+130+20)*0.18)+(t+130+20)
            print(list(expression))
            fta=20
            result(expression,n,fta,t,gt)
    
        elif 25<n<50:
            t=int(total)
            gt=((t+130+40)*0.18)+(t+130+40)
            print(list(expression))
            fta=40
            result(expression,n,fta,t,gt)
        elif 50<n<75:
            t=int(total)
            gt=((t+130+60)*0.18)+(t+130+60)
            print(list(expression))
            fta=60
            result(expression,n,60,t,gt)
        elif 75<n<100:
            t=int(total)
            gt=((t+130+80)*0.18)+(t+130+80)
            print(list(expression))
            fta=80
            result(expression,n,fta,t,gt)
        else:
            t=int(total)
            gt=((t+130+100)*0.18)+(t+130+100)
            print(list(expression))
            fta=100
            result(expression,n,fta,t,gt)
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
        n=1
        
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
        
def win1(gui):
    global expression 
    global n
    global equation
    global eq
    
    root=gui
    root.title("Channels Calculator")
    root.geometry("490x310+400+129")
    root.iconbitmap(r'C:\Users\saif\Documents\Tri\tv.ico')
    equation=StringVar()
    expression_field =Text(root,height=2,width=36,bd=9,state=NORMAL,font=('Comic Sans MS',15),bg='light gray',fg='#fff')
    expression_field.grid(row=0,columnspan=7,ipadx=4,padx=5,ipady=4,pady=5)
    eq=" "

#-------------------------------------------------------------------------------
    buttonSum=Button(root,text=" Sum \n All",command=lambda:equalpress(equation),
                     height=9,width=20,fg="#000",bg="light green",bd=3,relief=RAISED,
                     font = ('Sans','10','bold'))
    buttonSum.grid(row=1,column=0,rowspan=3,columnspan=3)
#---------------------------------------------------------------------------------
    buttonClear=Button(root,text="Clear all ",command=lambda:(expression_field.delete('1.0',END),clear(equation)),width=8,height=2,fg='#fff',bg='red',font=('bold'))
    buttonClear.grid(row=4,column=0)
#----------------------------------------------------------------------------------
    buttonPrevious=Button(root,text="Last Result",fg='#000',bg='#ffff66',command=lambda:press(''),height=2,font=('bold'))
    buttonPrevious.grid(row=4,column=1)
#----------------------------------------------------------------------------------    
    button1 = Button(root, text=' 1 ',command=lambda: (press(1),expression_field.insert(END,"1")), height=2, width=10,fg="#000",bg="#b3d9ff",font=('bold')) 
    button1.grid(row=1, column=4)
    button2 = Button(root, text=' 2 ',command=lambda: (press(2),expression_field.insert(END,"2")), height=2, width=8,fg="#000",bg="#b3d9ff",font=('bold')) 
    button2.grid(row=1, column=5)
    button3 = Button(root, text=' 3 ',command=lambda: (press(3),expression_field.insert(END,"3")), height=2, width=8,fg="#000",bg="#b3d9ff",font=('bold')) 
    button3.grid(row=1, column=6)
#----------------------------------------------------------------------------------
    button4 = Button(root, text=' 4 ',command=lambda: (press(4),expression_field.insert(END,"4")), height=2, width=10, fg="#000",bg="#cce6ff",font=('bold')) 
    button4.grid(row=2, column=4)
    button5 = Button(root, text=' 5 ',command=lambda: (press(5),expression_field.insert(END,"5")), height=2,width=8 ,fg="#000",bg="#cce6ff",font=('bold')) 
    button5.grid(row=2, column=5)
    button6= Button(root, text=' 6 ',command=lambda: (press(6),expression_field.insert(END,"6")), height=2,width=8 ,fg="#000",bg="#cce6ff",font=('bold')) 
    button6.grid(row=2, column=6)
#----------------------------------------------------------------------------------
    button7 = Button(root, text=' 7 ',command=lambda: (press(7),expression_field.insert(END,"7")), height=2, width=10 ,fg="#000",bg="#e6f2ff",font=('bold')) 
    button7.grid(row=3, column=4)
    button8 = Button(root, text=' 8 ',command=lambda: (press(8),expression_field.insert(END,"8")), height=2,width=8,fg="#000",bg="#e6f2ff",font=('bold')) 
    button8.grid(row=3, column=5)
    button9 = Button(root, text=' 9 ',command=lambda: (press(9),expression_field.insert(END,"9")), height=2,width=8 ,fg="#000",bg="#e6f2ff",font=('bold')) 
    button9.grid(row=3, column=6)
#---------------------------------------------------------------------------------
    buttonDot= Button(root, text=' . ',command=lambda: (press('.'),expression_field.insert(END,".")), height=2,width=8,fg="#000",bg="#66d9ff",font=('bold')) 
    buttonDot.grid(row=4, column=5)
#----------------------------------------------------------------------------------
    buttonAdd = Button(root, text='  ADD  ',command=lambda: (press('+'),expression_field.insert(END,"+")), height=2, width=10,fg="#000",bg="#66d9ff",font=('bold')) 
    buttonAdd.grid(row=4,column=3,columnspan=2,pady=5)
    button0= Button(root, text=' 0 ',command=lambda: (press(0),expression_field.insert(END,"0")), height=2,width=8, fg="#000",bg="#66d9ff",font=('bold')) 
    button0.grid(row=4, column=6)
     
#----------------------------------------------------------------------------------

    root.mainloop()
    
def press(num):
        global n
        global expression 
        global eq
        if num=="+":
            n=n+1
        else:
            pass
        # concatenation of string 
        expression = expression + str(num) 
       
        
        # update the expression by using set method 
        equation.set(expression) 
       
        eq=expression 
        print(eq)    
        return eq
if __name__=="__main__":
    root=Tk()
  #  eq=('Add Channels to the list ')
    win1(root)
