import config as conf 
def purchased():
    print("number of tickets purchased :")
    print("tickets: ",len(conf.details))
def percentage():
    percent=(len(conf.details)/(conf.rows*conf.columns))*100
    print("percentage:{:.2f}%".format(percent))
def current_income():
    curincome=0
    for i,j in conf.details.items():
        curincome=curincome+j[4]
    print("current income : ",curincome)
def total_income():
    total=0
    if conf.rows*conf.columns>60:
       total=(total+(conf.rows//2)*10*conf.columns)
       total=(total+(conf.rows-conf.rows//2)*8*conf.columns)
    else:
        total=conf.rows*conf.columns*10
    print("total income : ",total)