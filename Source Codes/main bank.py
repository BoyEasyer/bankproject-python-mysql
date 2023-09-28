import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='BoyEasyer(12345)',database='bank')
cur = conn.cursor()
print("====================================")
print('WELCOME TO BANK OF GHAZIABAD')
print("====================================")
import datetime as dt
print("Current Time:-",dt.datetime.now())
print("====================================")
print("MAIN MENU: ")
print('1.REGISTER')
print('2.LOGIN')
print("====================================")



n=int(input('Enter your choice: '))
print()

if n== 1:
     name=input('Enter a Username: ')
     print()
     passwd=int(input('Enter a 4 Digit Password: '))
     print()

     V_SQLInsert="INSERT  INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print("====================================")
     print('User created succesfully')
     print("====================================")
     import menu

if  n==2 :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your 4 DIGIT Password='))
     V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print("====================================")
          print('Invalid username or password')
          print("====================================")
     else:
          print("Wrong Input! Please restart the program to try again...")
          
     
     
