#SOURCE CODE FOR BANKING TRANSACTIONS
print("\t\t$$$$\tBank Of Ghaziabad\t$$$$")
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="BoyEasyer(12345)")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
#creating required tables 
mycursor.execute("create table if not exists bank_master(acno char(6) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
mycursor.execute("create table if not exists banktrans(acno char (6),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
while(True):
    print("Please note an accounnt becomes mature once a payment(Deposit/Withdrawal) is executed from an account.")
    print("Also note that mature accounts are undeletable as per the rules of Government.")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Display account information")
    print("5. Delete An Account")
    print("6. Exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        import random
        print("All information prompted are mandatory to be filled")
        print("The Account Number Is Generated Randomly...")
        acno=random.randint(10000,99999)
        print("Your Account Number is:",acno)
        name=input("Enter Name(Limit 35 Characters): ")
        city=str(input("Enter City Name: "))
        mn=str(input("Enter Mobile Number: "))
        balance=0
        mycursor.execute("insert into bank_master values('"+str(acno)+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
        mydb.commit()
        print("Account is successfully created!!!")
        
        
#PROCEDURE FOR UPDATIONG DETAILS AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
    elif(ch==2):
        acno=str(input("Enter account number: "))
        dp=int(input("Enter amount to be deposited: "))
        dot=str(input("Enter date of Transaction: (YYYY-MM-DD) "))
        ttype="d"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("Money deposited successully!!!")
        
        
#PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT
    elif(ch==3):
        acno=str(input("Enter account number: "))
        wd=int(input("Enter amount to be withdrawn: "))
        dot=str(input("enter date of transaction: (YYYY-MM-DD) "))
        ttype="w"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
        print("Amount Withdrawn successfully!!")
        mydb.commit()
        
#PROCEDURE FOR DISPLAYING THE ACCOUNT OF THE ACCOUNT HOLDER AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif(ch==4):
        print("Press 1 To See The Sample Account.")
        acno=str(input("Enter account number: "))
        lst=["Account Number:","Account Name:", "City Name:", "Mobile Number:"]
        mycursor.execute("select * from bank_master where acno= '"+acno+"'")
        flag=0
        k=0
        for i in mycursor:
            for j in i:
                if k==len(i)-1:
                    break
                else:
                    print(lst[k], j)
                k=k+1
            flag=1
        print("\n")
        if flag==0:
            print("No Record Found!!")
        
        
#DELETING A RECORD IF IT EXISTS
    elif ch==5:
        ac=str(input("Enter The Account Number You Want To Get Deleted: "))
        mycursor.execute("delete from bank_master where acno= '"+ac+"'")
        print("Record Deleted Succesfully!")
        
    else:
        print("The set of rules provided to me says me to quit...")    
        exit()
        
        
