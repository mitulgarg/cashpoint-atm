d={'mitul7hero@gmail.com':'mitul','manoj@gmail.com':'manoj','mohammed@gmail.com':'mohammed'}

from tkinter import *
root=Tk()
#Title and background color
root.title("ATM MACHINE")
root.configure(background='#3b5998')
root.state('zoomed')
#Icon
pic=PhotoImage(file='atm-machine.png')
root.iconphoto(True,pic)
#Function
def login():
    global mail_id
    global pwd
    mail_id=e1.get()
    pwd=e2.get()
    for i in d:
        if i==mail_id and d[i]==pwd :
            callback()
    
    else:
        Fail=Label(text="Login Failed",font=("Roboto",19,'normal'),fg='#dfe3ee',background='#3b5998')
        Fail.pack()

            
def callback():
    global mail_id
    global pwd
    newWindow = Toplevel(root)
    newWindow.title("Account")
    newWindow.configure(background='#3b5998')
    newWindow.state('zoomed')
    mail_id=e1.get()
    pwd=e2.get()
    header_LABEL= Label(newWindow, text = "CASHPOINT ATM",font=("Cinzel Decorative", 45,'bold'),foreground='#dfe3ee',background='#3b5998')
    header_LABEL.pack(pady=30)
    l2=Label(newWindow,text=mail_id,font=("Cinzel Decorative", 25,'bold'),foreground='#dfe3ee',background='#3b5998')
    l2.pack()
    l3=Label(newWindow,text="Select an option to continue :-",font=("Roboto",19,'normal'),fg='#dfe3ee',background='#3b5998' )
    l3.pack(pady=10)
    Bal=Button(newWindow,text="Check Balance",font=("Roboto",19,'normal'),bg="#3b5998",fg='#dfe3ee',borderwidth=2, relief="groove",command=balance)
    Bal.pack(padx=5,pady=50)
    Withdraw=Button(newWindow,text="Withdraw",font=("Roboto",19,'normal'),bg="#3b5998",fg='#dfe3ee',borderwidth=2, relief="groove",command=withdraw)
    Withdraw.pack(padx=2,pady=5)

def balance():
    bal=0
    f=open('balance.txt','r')
    c=f.read()
    info=c.split()
    for i in range(0,len(info)):
        if info[i]==mail_id:
            bal=info[i+1]
    f.close()       
            
    newWindow2 = Toplevel(root)
    newWindow2.title("Account Balance")
    newWindow2.configure(background='#3b5998')
    newWindow2.state('zoomed')
    header_LABEL= Label(newWindow2, text = "CASHPOINT ATM",font=("Cinzel Decorative", 45,'bold'),foreground='#dfe3ee',background='#3b5998')
    header_LABEL.pack(pady=30)
    bal_output=Label(newWindow2,font=("Roboto",30,'normal'),text='Your current balance is : ₹ '+str(bal))
    bal_output.pack(pady=100)
    Button(newWindow2, text="Quit",font=("Roboto",19,'normal'),bg="#3b5998",fg='#dfe3ee',borderwidth=2, relief="groove" ,command=root.destroy).pack(pady=50) 
    
def withdraw():
    global e3
    global newWindow3
    newWindow3 = Toplevel(root)
    newWindow3.title("Withdraw Money")
    newWindow3.configure(background='#3b5998')
    newWindow3.state('zoomed')
    header_LABEL= Label(newWindow3, text = "CASHPOINT ATM",font=("Cinzel Decorative", 45,'bold'),foreground='#dfe3ee',background='#3b5998')
    header_LABEL.pack(pady=30)
    e3=Entry(newWindow3,width=35,bd=5,font="Roboto")
    e3.pack(padx=5,pady=5)
    
    button=Button(newWindow3,text="Withdraw",font=("Roboto",19,'normal'),bg="#3b5998",fg='#dfe3ee',borderwidth=2, relief="groove",command=fileedit)
    button.pack(pady=8)
    

def fileedit():
    bal=''
    f=open('balance.txt','r+')
    c=f.read()
    info=c.split()
    for i in range(0,len(info)):
        if info[i]==mail_id:
            bal=info[i+1]
            
    e_int = int(e3.get())
    remainder=int(bal)-e_int
    for i in range(0,len(info)):
        if info[i]==mail_id:
            info[i+1]=remainder
    while True:
        f.seek(0)
        for i in info:
            f.write(str(i)+' ')
        break
    
    f.close()
    label=Label(newWindow3,text="Updated balance is "+str(remainder),font=("Roboto",19,'normal'),fg='#dfe3ee',background='#3b5998')
    label.pack(pady=25)
    Button(newWindow3,font=("Roboto",19,'normal'),bg="#3b5998",fg='#dfe3ee',borderwidth=2, relief="groove", text="Quit", command=root.destroy).pack(pady=25)        
#Labels other GUI
    
header_LABEL= Label(root, text = "CASHPOINT ATM",font=("Cinzel Decorative", 45,'bold'),foreground='#dfe3ee',background='#3b5998')
header_LABEL.pack(pady=30)
label_space=Label(height=8,background='#3b5998')
label_space.pack()
login_label=Label(text="Enter Your Login Credentials:",font=("Roboto",25,'normal'),fg='#dfe3ee',background='#3b5998')
login_label.pack()
ID_label=Label(text="E-Mail",font=("Roboto",19,'normal'),fg='#dfe3ee',background='#3b5998')
ID_label.pack()
e1=Entry(root,width=35,bd=5,font="Roboto")
e1.pack(padx=5,pady=5)
password_label=Label(text="Password",font=("Roboto",19,'normal'),fg='#dfe3ee',background='#3b5998')
password_label.pack()
e2=Entry(root,width=35,bd=5,font="Roboto")
e2.pack(padx=5,pady=5)
button=Button(text="Login",font=("Roboto",19,'normal'),bg="#3b5998",fg='#dfe3ee',borderwidth=2, relief="groove",command=login)
button.pack(pady=8)












root.mainloop()
