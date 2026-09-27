def get_subjects(n):
    while True:
        listofsubjects=input(f'Enter {n} subjects name seprated by "," :').split(",")
        if len(listofsubjects) == n:
            break
        else:
            print(f"Please enter exactly {n} subjects.")
    creditlist=[]
    print("Enter credit value for each subject")
    for i in listofsubjects:
        while True:
            try:
                c=int(input(f'{i} :'))
                if c>0:
                    break
                else:
                    print("Credit value should be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        creditlist.append(c)
    return listofsubjects, creditlist

def get_cat1(listofsubjects):
    cat1marks=[]
    print("Enter CAT1 marks out of 50")
    for i in listofsubjects:
        while True:
            try:
                mark=int(input(f'{i} :'))
                if 0 <= mark <= 50:
                    break
                else:
                    print("Please enter a valid mark between 0 and 50.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        cat1marks.append(mark)
    return cat1marks

def get_cat2(listofsubjects):
    cat2marks=[]
    print("Enter CAT2 marks out of 50")
    for i in listofsubjects:
        while True:
            try:
                mark=int(input(f'{i} :'))
                if 0 <= mark <= 50:
                    break
                else:
                    print("Please enter a valid mark between 0 and 50.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        cat2marks.append(mark)
    return cat2marks

def get_tee(listofsubjects):
    teemarks=[]
    print("Enter TEE marks out of 100")
    for i in listofsubjects:
        while True:
            try:
                mark=int(input(f'{i}  :'))
                if 0 <= mark <= 100:
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        teemarks.append(mark)
    return teemarks

def get_internal(listofsubjects):
    internalmarks=[]
    print("Enter Internal Assessment marks out of 40 for the whole semester")
    for i in listofsubjects:
        while True:
            try:
                mark=int(input(f'{i} :'))
                if 0 <= mark <= 40:
                    break
                else:
                    print("Please enter a valid mark between 0 and 40.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        internalmarks.append(mark)
    return internalmarks
