from files.config import * 
class superusers:
    def createuser(self):
        n=input("enter username :")
        p=input("enter your password :")
        userdetails[n]=p
    def checkuser(self,name,password):
        if userdetails[name]==password:
            return True
        else :
            return False
    def addquestion(self):
        print("enter the question you want to add ")
        q=input()
        temp=[]
        for i in range(4):
            print("enter the ",i+1,"option : ")
            n=input()
            temp.append(n)
        print(temp)
        crt=int(input("enter the correct answer : "))
        questions[q]=temp
        correct.append(crt)
    def evaluate(self):
            result=0
            for i,j in zip(answers,correct):
                if i==j:
                    result=result+1
            return result

