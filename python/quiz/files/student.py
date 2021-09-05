from files.config import * 
from files.superuser import *
user=superusers()
class student:
    def createstudent(self):
        username=input("enter the name :")
        studentdetails.append(username)
    def checkstudent(self,name):
         if name in studentdetails:
             return True
         else:
             return False
    def startexam(self):
        c=1
        for i,j in questions.items():
            print("question ",c,end=":")
            print(i)
            for k in range(0,4):
                print("option ",k+1,":",j[k])
            ans=int(input("enter the answer : "))
            answers.append(ans)        
    def result(self):
        result=user.evaluate()
        print("******* results ******* ")
        print("total marks : ",result,"/",len(questions))
        print("percentage :",(result/len(questions)*100.0))
        print("************************")
