import config as conf 
def show_the_seats():
    seating_order=conf.seating_order
    rows=conf.rows
    columns=conf.columns
    print(" ",end=" ")
    for i in range(1,columns+1):
        print(i,end=" ")
    print()
    for i in range(rows):
        print(i+1,end=" ")
        for j in range(columns):
            if(seating_order[i][j]==0):
                print('S',end=" ")
            else:
                print('B',end=" ")
        print("")
def buy_ticket():
    rows=conf.rows
    columns=conf.columns
    seating_order=conf.seating_order
    if conf.tickets==conf.rows*conf.columns:
        print("HouseFull !!!")
    else:
        print("to book a ticket please enter the row and the column")
        r=int(input("enter the row : "))
        c=int(input("enter the column "))
        if r>rows or c>columns or r<1 or c<1:
            print("invalid row or column ")
        else:
            if seating_order[r-1][c-1]==1:
                print("the seat you have selected is already booked ")
                print("please select another seat ")
            else:
                ticket_price=0
                name=input("enter the name : ")
                age=int(input("enter the age : "))
                gender=input("enter the gender (Male or Female or Other) : ")
                phone=input("enter the phone number : ")
                seating_order[r-1][c-1]=1
                print("seat has been successfully booked ")
                if rows*columns > 60:
                    if r<=rows//2:
                        ticket_price=10
                    else:
                        ticket_price=8
                else:
                        ticket_price=10
                        cal=((r-1)*columns)+c
                        li=[name,age,gender,phone,ticket_price]
                        conf.details[cal]=li
                        print("name : ",name)
                        print("age : ",age)
                        print("gender : ",gender)
                        print("Phone :",phone)
                        print("ticket number :",cal,"ticket price : ",ticket_price)
                        conf.seating_order=seating_order
                        conf.tickets+=1            
def show_user_info():
    seating_order=conf.seating_order
    columns=conf.columns
    r=int(input("enter the row : "))
    c=int(input("enter the column : "))
    if seating_order[r-1][c-1]==0:
        print("the seat is not booked ")
    else:
        cal=((r-1)*columns)+c
        li=conf.details[cal]
        print("name: ",li[0])
        print("age: ",li[1])
        print("gender: ",li[2])
        print("Phone :",li[3])
        print("ticket number :",cal,"ticket price : ",li[4])                          