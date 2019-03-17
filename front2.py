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
    
def equalpress(equation):
      # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
        global n
        
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
        
      
        print(list(expression))
  
        equation.set(total) 
  
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
    root.geometry("400x380+400+129")
    
    equation=StringVar()
    expression_field =Entry(root, textvariable=equation,width=65)
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
