#Employee Management System
import mysql.connector as sqlcon
mycon=sqlcon.connect(host='localhost',user='Arun',\
                     passwd='Anonymous123')

mycur=mycon.cursor()
#Creating database
mycur.execute('create database EMP')
mycur.execute('use EMP')

#Creating Employee Table
mycur.execute('create table employee(eno int(10) primary key,\
ename varchar(30),address varchar(35),salary varchar(10),DOB date,\
sex varchar(1))')

#Creating Table for storing password
mycur.execute('create table password(pwd varchar(15))')
mycur.execute("insert into password values('Anonymous123')")

mycon.commit()

mycon.close()

#Main Menu
def menu():
    ans='y'
    while (ans=='y' or ans=='Y'):
        print(75*'_') 
        print("\n\t              <<<<<<<MAIN MENU>>>>>>>")
        print(75*'_')
        print("                             1. Add")
        print("                             2. Update")
        print("                             3. Delete")
        print("                             4. Search")
        print("                             5. Display All")
        print("                             6. Exit")
        print(75*'_')
        choice=int(input("\nEnter your choice: "))
        if choice==1:
            adddata()
        elif choice==2:
            updatedata()
        elif choice==3:
            deldata()
        elif choice==4:
            search()
        elif choice==5:
            display()
        elif choice==6:
            print("Exiting....")
            break
        else:
            print("Wrong Input")
        ans=input("Do you want to continue(y/n): ")
    else:
        print("Thanks")
        
#Inserting data to the table
def adddata():
    try:
        eid=int(input("Employee ID:"))
        ename=input("Employee Name:")
        address=input("Address:")
        salary=int(input("Salary:"))
        DOB=input("Date of Birth(YYYY-MM-DD):")
        sex=input("Sex:")
        cursor=db.cursor()
        cursor.execute("insert into employee values({},'{}','{}',{},'{}','{}')".\
                       format(eid,ename,address,salary,DOB,sex))
        print("Record added")
    except:
        print('Error,Invalid Data!!')

#Fuction to update the details
def updatedata():
    try:
        eid=int(input("Employee ID:"))
        if checkexist(eid)==False: #Checking if Employee ID exists
            print("Employee ID does not exist")
            return 
        print("Enter the New Data")
        ename=input("Employee Name:")
        address=input("Address:")
        salary=int(input("Salary:"))
        DOB=input("Date of Birth(YYYY-MM-DD):")
        sex=input("Sex:")
        
        cursor=db.cursor()
        cursor.execute("update employee set ename='{}',address='{}',salary={},DOB='{}',\
                        sex='{}' where eno={}".format(ename,address,salary,DOB,sex,eid))
        print("Record updated")       
    except:
        print("Error,Invalid Data!!")

#Function to delete a record from the table
def deldata():
    eid=int(input('Employee ID:'))
    cursor=db.cursor()
    cursor.execute('delete from employee where eno={}'.format(eid))
    print("Record Deleted")

# Function to search the details of a student
def search():
    try:
        eid=int(input('Enter Employee ID :'))
        if checkexist(eid)==False: #Checking if Employee ID exists
            print("Employee ID does not exist")
            return
        cursor=db.cursor()
        cursor.execute('Select * from employee where eno={}'.format(eid))
        record=cursor.fetchone()
        print('\n\t EMPLOYEE DETAILS')
        print('\t',15*'-')
        print('Employee ID   :',record[0])
        print('Employee Name :',record[1])
        print('Address       :',record[2])
        print('Salary        :',record[3])
        print('Date of Birth :',record[4])
        print('Sex           :',record[5])
    except:
        print("Error!!")
          
#Function to display all data
def display():
    cursor=db.cursor()
    cursor.execute("select * from employee")
    results=cursor.fetchall() #fetch all the records
    print('\n\t ALL RECORDS')
    print('\t',12*'-')
    for record in results:
        print('Employee ID   :',record[0])
        print('Employee Name :',record[1])
        print('Address       :',record[2])
        print('Salary        :',record[3])
        print('Date of Birth :',record[4])
        print('Sex           :',record[5])
        print("_________________________")
        

#To check if Employee ID already exists...
def checkexist(eno):
    cursors=db.cursor()
    cursors.execute("select eno from employee")
    data=cursors.fetchall()
    n=len(data)
    for i in range(n):
        if data[i][0]==eno:
            return True
    return False



#main
#connection
import mysql.connector
db=mysql.connector.connect(host='localhost',user='Arun',\
                     password='Anonymous123',database='EMP')

db.autocommit=True
  
pwd=input("Password:")
cursor=db.cursor()
cursor.execute('Select pwd from password')
pwd1=cursor.fetchone()
if pwd in pwd1: #check password
    menu()
else:
    print("Wrong password")

#_____________________________________________