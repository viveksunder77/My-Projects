from files.superuser import *
from files.config import * 
from files.student import *
superuser=superusers()
st=student()
n=True
print("**************welcome to quiz**************")
while(n):
    print("1.create a super user \n2.super user login\n3.register a student \n4.student login\n5.check result\n6.exit ")
    choice=int(input("enter your choice :"))
    if choice==1:
        superuser.createuser()
    elif choice==2:
        username=input("enter the username : ")
        password=input("enter the password :")
        status=superuser.checkuser(username,password)
        if status:
            print("welcome superuser :",username)
            m=True
            while(m):
                print("1.add a question\n2.evaluate\n3.go back")
                choice2=int(input("enter your choice :"))
                if choice2==1:
                    superuser.addquestion()
                elif choice2==2:
                    superuser.evaluate()
                elif choice2==3:
                    m=False
                else:
                    print("invalid option ")
    elif choice==3:
        st.createstudent()
    elif choice==4:
        nam=input("enter the student name : ")
        if st.checkstudent(nam):
            print("to start the exam please enter your details :")
            print("****best of luck ****")
            st.startexam()
    elif choice==5:
        superuser.evaluate()
        st.result()
    elif choice==6:
        print("*** exiting the appliction ***")
        n=False
    else:
        print("invalid option try again ")



