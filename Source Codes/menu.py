import datetime as dt
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='BoyEasyer(12345)',database='bank')
cur = conn.cursor()
conn.autocommit = True
c = 'y'
while c == 'y':
                         print("====================================")                       
                         print("TABLE OF CONTENTS: ")
                         print('1.CREATE BANK ACCOUNT')
                         print('2.TRANSACTION')
                         print('3.CUSTOMER DETAILS')
                         print('4.TRANSACTION DETAILS')
                         print('5.DELETE ACCOUNT')
                         print('6.QUIT')
                         print("====================================")
                         print()
                         n=int(input('Enter your Choice: '))
                         print()

                         if n == 1:
                                    import random
                                    acc_no=random.randint(100000,999999)
                                    print("Your Account Number is: ",acc_no)
                                    print()
                                    acc_name=input('Enter the name of ACCOUNT HOLDER=')
                                    print()
                                    ph_no=int(input('Enter your PHONE NUMBER='))
                                    if 1000000000>ph_no or 9999999999<ph_no:
                                        print()
                                        print("====================================")
                                        print('Please Enter a Valid 10 Digit Number!!!!!')
                                        print("====================================")
                                        break
                                    print()
                                    add=(input('Enter your PLACE='))
                                    print()
                                    cr_amt=int(input('Enter your CREDIT AMOUNT(>1000)='))
                                    V_SQLInsert="INSERT  INTO customer_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
                                    if cr_amt>=1000:
                                        cur.execute(V_SQLInsert)
                                        print()
                                        print("====================================")
                                        print('Account Created Succesfully!!!!!')
                                        print("====================================")
                                    else:
                                        print("\n\n====================================")
                                        print("Please Enter An Amount>1000!!")
                                        print("====================================\n\n")
                                    
                                    conn.commit()
    

                         if n == 2:
                              acct_no=int(input('Enter Your Account Number='))
                              cur.execute('select * from customer_details where acct_no='+str (acct_no) )
                              data=(cur.fetchall())
                              count=cur.rowcount
                              conn.commit()
                              if count == 0:
                                   print("========================================================")
                                   print('NO ACCOUNT FOUND WITH THE CORRESPONDING ACCOUNT NUMBER!!')
                                   print("========================================================")
                              else:
                                   print()
                                   print('1.WITHDRAW AMOUNT')
                                   print()
                                   print('2.CREDIT AMOUNT')
                                   print()

                                   print()
                                   x=int(input('Enter your Choice: '))
                                   print()
                                   if x == 1:
                                        amt=int(input('Enter withdrawl amount: '))
                                        b=data[0][4]
                                        a=b-amt
                                        if a>=1000:
                                            cr_amt=0
                                            cur.execute('update customer_details set   cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                                            V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                                            cur.execute(  V_SQLInsert)
                                            conn.commit()
                                            print()
                                            print("====================================")
                                            print('ACCOUNT UPDATED SUCCESSFULLY!!!!!')
                                            print("====================================")
                                        else:
                                            print("====================================================================================")
                                            print("Your balance  is getting lesser than 1000 after the transaction. Please try again...")
                                            print("====================================================================================")
                                   elif x== 2:
                                         amt=int(input('Enter amount to be added: '))
                                         cr_amt=0
                                         cur.execute('update customer_details set  cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no))
                                         V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                                         cur.execute(V_SQLInsert)
                                         conn.commit()
                                         print()
                                         print("====================================")
                                         print('ACCOUNT UPDATED SUCCESSFULLY!!!!!')
                                         print("====================================")

                         if n == 3:
                              acct_no=int(input('Enter your account number: '))
                              print()
                              cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                              if cur.fetchone() is  None:
                                   print()
                                   print("====================================")
                                   print('NO ACCOUNT FOUND!!')
                                   print("====================================")
                              else:
                                   cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                                   data=cur.fetchall()
                                   for row in data:
                                        print("====================================\nACCOUNT DETAILS:")
                                        print('ACCOUNT NO=',acct_no)
                                        print()
                                        print('ACCOUNT NAME=',row[1])
                                        print()
                                        print('PHONE NUMBER=',row[2])
                                        print()
                                        print('ADDRESS=',row[3])
                                        print()
                                        print('CREDIT AMOUNT=',row[4])
                                        print("====================================")
                         if n == 4:
                             acct_no=int(input('Enter your account number: '))
                             print()
                             cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                             if cur.fetchone() is  None:
                                 print()
                                 print("====================================")
                                 print('NO ACCOUNT FOUND!!')
                                 print("====================================")
                             else:
                                 cur.execute('select * from transactions where acct_no='+str(acct_no) )
                                 data=cur.fetchall()
                                 for row in data:
                                     print("==============================")
                                     print('ACCOUNT NO: ',acct_no)
                                     print()
                                     print('DATE: ',row[1])
                                     if row[2]!=0:
                                         print()
                                         print(' WITHDRAWAL AMOUNT: ',row[2])
                                         print()
                                     else:
                                         print('AMOUNT ADDED: ',row[3])
                                         print("==============================")
                                         print()
                               

                         if n == 5:
                                  print('DELETE YOUR ACCOUNT\n')
                                  acct_no=int(input('Enter your account number='))
                                  cur.execute('delete from customer_details where acct_no='+str(acct_no) )
                                  print("====================================")
                                  print('ACCOUNT DELETED SUCCESFULLY!!!')
                                  print("====================================")  
                         if n == 6:
                              print('DO YOU WANT TO EXIT(y/n)')
                              c=input ('Enter your choice: ')
                              if c in 'yy':
                                  print("================================")
                                  print('THANK YOU PLEASE VISIT AGAIN')
                                  print("================================")
                                  quit()
     
                             

                             
                         else:
                             print("Please select a valid Input!!")
     
    
                               
                              
                              
                              

                                        
               
     


