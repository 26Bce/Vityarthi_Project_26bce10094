import input_handler
import calculations
import display

exam=["cat1","cat2","tee"]

while True:
    n=int(input("Enter number of subjects in semester: "))
    if n>0:
        break
    else:
        print("Number of subjects should be greater than 0. Please try again.")

listofsubjects, creditlist = input_handler.get_subjects(n)

en=int(input("How many exams have been conducted so far? (1/2/3)\n1. CAT1\n2. CAT2\n3. TEE\n"))

cat1marks=[]
cat2marks=[]
teemarks=[]

if en==1:
    cat1marks=input_handler.get_cat1(listofsubjects)
elif en==2:
    cat1marks=input_handler.get_cat1(listofsubjects)
    cat2marks=input_handler.get_cat2(listofsubjects)
elif en==3:
    cat1marks=input_handler.get_cat1(listofsubjects)
    cat2marks=input_handler.get_cat2(listofsubjects)
    teemarks=input_handler.get_tee(listofsubjects)
else:
    print("Invalid input. Please try again.")

internalmarks=None

while True:
    print("Enter choice: \n1. Display marks\n2. Display percentage \n3. Marks contribution in semester\n4. Calculate SGPA(Based on absolute grading)\n5. Analysis\n6. Marks required for target SGPA\n7. Exit")
    choice=int(input())
    if choice==1:
        display.display(listofsubjects,en,cat1marks,cat2marks,teemarks)
    elif choice==2:
        for i in range(1,en+1):
            if i==1:
                print(f"Percentage in CAT1: {calculations.percentage(cat1marks,50):.2f}%")
            elif i==2:
                print(f"Percentage in CAT2: {calculations.percentage(cat2marks,50):.2f}%")
            elif i==3:
                print(f"Percentage in TEE: {calculations.percentage(teemarks,100):.2f}%")
    elif choice==3:
        for i in range(1,en+1):
            if i==1:
                print(f"Contribution of CAT1: {calculations.contribution(cat1marks)}")
            elif i==2:
                print(f"Contribution of CAT2: {calculations.contribution(cat2marks)}")
            elif i==3:
                print(f"Contribution of TEE: {calculations.contribution(teemarks)}")
    elif choice==4:
        if en==3:
            if internalmarks is None:
                internalmarks=input_handler.get_internal(listofsubjects)
            calculations.sgpa_calculator(listofsubjects,creditlist,cat1marks,cat2marks,teemarks,internalmarks)
        else:
            print("SGPA can be calculated only after all semester exams are conducted.")
    elif choice==5:
        calculations.analysis(listofsubjects,en,cat1marks,cat2marks,teemarks)
    elif choice==6:
        calculations.target_sgpa(listofsubjects,en,cat1marks,cat2marks)
    elif choice==7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
