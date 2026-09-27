def display(listofsubjects,en,cat1marks,cat2marks,teemarks):
    print("|".join(listofsubjects))
    for i in range(1,en+1):
        if i==1:
            print("|".join(str(mark) for mark in cat1marks))
        elif i==2:
            print("|".join(str(mark) for mark in cat2marks))
        elif i==3:
            print("|".join(str(mark) for mark in teemarks))
