from tkinter import *
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Banking app")
def finish_r():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_account = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="all feilds are require.")
        return
    
    for name_check in all_account:
        if name == name_check:
            notif.config(fg="red",text="account already exists")
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="account created successfully")


def register():
    global temp_age
    global temp_gender
    global temp_name
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    r_screen = Toplevel(root)
    r_screen.title("register")
    Label(r_screen,text = "Enter your details below",font = 14).grid(row=0,sticky=N,pady=10)
    Label(r_screen,text = "Name",font = 10).grid(row=1,sticky=W)
    Label(r_screen,text = "Age",font = 10).grid(row=2,sticky=W)
    Label(r_screen,text = "Gender",font = 10).grid(row=3,sticky=W)
    Label(r_screen,text = "Password",font = 10).grid(row=4,sticky=W)
    notif = Label(r_screen,font = ('Ariel',12))
    notif.grid(row=8,sticky=N,pady = 10) 


    Entry(r_screen,textvariable=temp_name).grid(row=1,column=1,padx=5)
    Entry(r_screen,textvariable=temp_age).grid(row=2,column=1,padx=5)
    Entry(r_screen,textvariable=temp_gender).grid(row=3,column=1,padx=5)
    Entry(r_screen,textvariable=temp_password,show="*").grid(row=4,column=1,padx=5)
     

    Button(r_screen,text="Register",command=finish_r).grid(row = 6,column=0)



def login_fin():
    global login_name
    all_account = os.listdir()
    login_name = l_name.get()
    login_pass = l_pass.get()

    for name in all_account:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            if login_pass == password:
                l_screen.destroy()
                account_dasshboard = Toplevel(root)
                account_dasshboard.title('dashboard')

                Label(account_dasshboard,text="ACCOUNT DASHBOARD",font = ('calibri',12)).grid(row=0,sticky=N,pady =10)
                Label(account_dasshboard,text="WELCOME "+name,font =('calibri',12)).grid(row = 1,pady = 5)

                Button(account_dasshboard,text="personal details",font=('calibri',12),width=30,command= per_details).grid(row=2,padx=10)
                Button(account_dasshboard,text="Deposit",font=('calibri',12),width=30,command=deposit).grid(row=3,padx=10)
                Button(account_dasshboard,text="Withdraw",font=('calibri',12),width=30,command=withdraw).grid(row=4,padx=10)
                Button(account_dasshboard,text="Transfer",font=('calibri',12),width=30,command=transfer).grid(row=5,padx=10)

                return

              
        else:
            l_notif.config(fg="red",text="name or password is incorrect" )
def transfer():
    def perform_transfer():
        trans_amount = float(transfer_amount.get())
        recipient = transfer_recipient.get()
        file = open(login_name,'r+')
        file_data = file.read()
        us_details = file_data.split('\n')
        us_balance = us_details[4]
        if float(us_balance) < float(trans_amount):
            transfer_notif.config(text="INsufficient balance",fg = 'red')
            return
        else:
            new_balance = float(us_balance)-float(trans_amount)
            file_data = file_data.replace(str(us_balance),str(new_balance))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close

        try:
            file =  open(recipient, 'r+')
            file_data = file.read()
            b_al = file_data.split('\n')
            re_bal = float(b_al[4])
            new_bal = re_bal + trans_amount
            file_data = file_data.replace(str(re_bal),str(new_bal))
            file.seek(0)
            file.truncate()
            file.write(file_data)
            transfer_notif.config(text="Transfer successful", fg='green')
            
        except FileNotFoundError:
            transfer_notif.config(text="Recipient does not exist", fg='red')        




    
    transfer_screen = Toplevel(root)
    transfer_screen.title("TRANSFER")

    Label(transfer_screen,text="MONEY TRANSFER",font=('calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(transfer_screen,text="amount",font=('calibri',12)).grid(row=1,sticky=N,pady=10)
    Label(transfer_screen,text="Receipient",font=('calibri',12)).grid(row=2,sticky=N,pady=10)

    transfer_notif = Label(transfer_screen, font=('calibri', 12))
    transfer_notif.grid(row=5, sticky=N, pady=10)
    transfer_recipient = StringVar()
    transfer_amount = StringVar()

    Entry(transfer_screen, textvariable=transfer_amount).grid(row=1, column=1, padx=5)
    Entry(transfer_screen, textvariable=transfer_recipient).grid(row=2, column=1, padx=5)

    Button(transfer_screen, text="Transfer", command=perform_transfer).grid(row=4, sticky=N, pady=10)





def per_details():
    file = open (login_name, 'r')
    file_data = file.read()
    user_details =  file_data.split('\n')
    details_name = user_details[0]
    details_age =  user_details [2]
    details_gender = user_details[3] 
    details_balance = user_details[4]

    personal_details_screen = Toplevel(root) 
    personal_details_screen.title('Personal Details')

    Label(personal_details_screen,text="PERSONAL DETAILS",font = ('calibri',12)).grid(row=0,sticky=N,pady =10)
    Label(personal_details_screen,text="NAME: "+details_name,font = ('calibri',12)).grid(row=1,sticky=N,pady =10)
    Label(personal_details_screen,text="AGE: "+details_age,font = ('calibri',12)).grid(row=2,sticky=N,pady =10)
    Label(personal_details_screen,text="GENDER: "+details_gender,font = ('calibri',12)).grid(row=3,sticky=N,pady =10)
    Label(personal_details_screen,text="BALANCE: "+details_balance,font = ('calibri',12)).grid(row=4,sticky=N,pady =10)


    

def deposit():
    global amount
    global deposit_notif
    global current_balance
    amount =  StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    deposit_screen = Toplevel(root)
    deposit_screen.title("DEPOSIT")
    Label(deposit_screen, text="Deposit", font=('Calibri', 12)).grid(row=0,sticky=N, pady=10)
    current_balance= Label(deposit_screen, text="Current Balance: "+details_balance, font=('Calibri',12))
    current_balance.grid(row=1,sticky=W)
    Label(deposit_screen, text="Amount: ", font= ("Calibri",12)).grid(row=2,sticky=W)
    deposit_notif= Label(deposit_screen, font=('Calibri',12))
    deposit_notif.grid(row=4, sticky=N, pady=5)
    Entry(deposit_screen, textvariable = amount).grid(row=2,column=1)
    Button(deposit_screen, text="Finish", font=("Calibri", 12), command=finish_deposit).grid(row=3,sticky=W,pady=5)
def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text="AMOUNT IS REQUIRED",fg="RED") 
        return
    if float(amount.get())  <= 0:
        deposit_notif.config(text="NEGATIVE VALUE IS NOT ACCEPTED",fg="RED")
        return
    file = open(login_name,"r+")
    file_data = file.read()
    det = file_data.split('\n')
    current_bal = det[4]
    updated_balance = current_bal
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_bal,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close

    current_balance.config(text = "CURRENT BALANCE: "+str(updated_balance),fg = "green")
    deposit_notif.config(text="BALANCE UPDATED",fg="green")

def withdraw():
    global withamount
    global withdraw_notif
    global with_current_balance
    withamount =  StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    withdraw_screen = Toplevel(root)
    withdraw_screen.title("WITHDRAW")
    Label(withdraw_screen, text="WITHDRAW", font=('Calibri', 12)).grid(row=0,sticky=N, pady=10)
    with_current_balance= Label(withdraw_screen, text="Current Balance: "+details_balance, font=('Calibri',12))
    with_current_balance.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Amount: ", font= ("Calibri",12)).grid(row=2,sticky=W)
    withdraw_notif= Label(withdraw_screen, font=('Calibri',12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)
    Entry(withdraw_screen, textvariable = withamount).grid(row=2,column=1)
    Button(withdraw_screen, text="Finish", font=("Calibri", 12), command=finish_withdraw).grid(row=3,sticky=W,pady=5)

def finish_withdraw():
    if withamount.get() == "":
        withdraw_notif.config(text="AMOUNT IS REQUIRED",fg="RED")
        return
    if float(withamount.get())  <= 0:
        withdraw_notif.config(text="NEGATIVE VALUE IS NOT ACCEPTED",fg="RED")
        return
    file = open(login_name,"r+")
    file_data = file.read()
    det = file_data.split('\n')
    current_bal = det[4]
    if float(withamount.get())> float(current_bal):
        withdraw_notif.config(text="INSUFFICIENT AMOUNT",fg ='red')
        return
    updated_balance = current_bal
    updated_balance = float(updated_balance) - float(withamount.get())
    file_data = file_data.replace(current_bal,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close

    with_current_balance.config(text = "CURRENT BALANCE: "+str(updated_balance),fg = "green")
    withdraw_notif.config(text="BALANCE UPDATED",fg="green")



def login():
    global l_name
    global l_pass
    global l_notif
    global l_screen

    l_name= StringVar()
    l_pass=StringVar()
    l_screen = Toplevel(root)
    l_screen.title("login page")

    Label(l_screen,text="Enter your details:").grid(row=0,sticky=N,pady=10)
    Label(l_screen,text="Name").grid(row=1)
    Label(l_screen,text="Password").grid(row=2)
    l_notif = Label(l_screen)
    l_notif.grid(row = 5,sticky=N,pady=10)

    Entry(l_screen,textvariable=l_name).grid(row=1,column=1,padx=5)
    Entry(l_screen,textvariable=l_pass,show='*').grid(row = 2,column=1,padx=5)

    Button(l_screen,text="login",command=login_fin).grid(row=4)



img = PhotoImage(file="Apps.png")
im=Label(image=img)
im.grid()



Label(root, text ="Your own bank", font=('calibri',22)).grid(row=0,sticky=N,pady=10)

Button(root,text="register",font=('calibri',12),width=20,command=register).grid(row=3,sticky=N,pady=10)
Button(root,text="login",font=('calibri',12),width=20,command=login).grid(row=5,sticky=N,pady=12)


root.mainloop()