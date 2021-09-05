import numpy as np 
import config as conf
from interact import *
from cinema import *
print("welcome to the BookMyMovie ")
rows=int(input("enter the number of rows : "))
columns=int(input("enter the number of columns : "))
conf.seating_order=np.arange(rows*columns).reshape(rows,columns)
conf.seating_order.fill(0)
conf.rows=rows
conf.columns=columns
n=True
while(n):
    print("\n1.Show the seats \n\n2.Buy a Ticket\n\n3.Statistics\n\n4.Show booked Tickets User Info\n\n0.Exit")
    print()
    c=int(input())
    if c==1:
        show_the_seats()
    elif c==2:
        buy_ticket()
    elif c==3:
        purchased()
        percentage()
        current_income()
        total_income()
    elif c==4:
        show_user_info()
    elif c==0:
        n=False
    else:
        print("invalid option ")