import math

def percentage(marks,max_marks):
    percent=(sum(marks)/(max_marks*len(marks)))*100
    return percent

def contribution(marks):
    result=[]
    for i in marks:
        result.append(round(i*0.3,2))
    return result

def grade_point(total):
    if total>=90:
        return 10
    elif total>=80:
        return 9
    elif total>=70:
        return 8
    elif total>=60:
        return 7
    elif total>=50:
        return 6
    elif total>=45:
        return 5
    else:
        return 0

def min_total_for_grade(gp):
    thresholds={10:90,9:80,8:70,7:60,6:50,5:45,0:0}
    return thresholds.get(gp,0)

def analysis(listofsubjects,en,cat1marks,cat2marks,teemarks):
    listsum=[]
    for i in range(len(listofsubjects)):
        total=0
        if en>=1:
            total+=cat1marks[i]
        if en>=2:
            total+=cat2marks[i]
        if en>=3:
            total+=teemarks[i]
        listsum.append(total)
    si=listsum.index(max(listsum))
    wi=listsum.index(min(listsum))
    print(f"Strongest subject: {listofsubjects[si]} (total marks: {listsum[si]})")
    print(f"Weakest subject: {listofsubjects[wi]} (total marks: {listsum[wi]})")

def sgpa_calculator(listofsubjects,creditlist,cat1marks,cat2marks,teemarks,internalmarks):
    cat1_contrib=contribution(cat1marks)
    cat2_contrib=contribution(cat2marks)
    tee_contrib=contribution(teemarks)
    totalpoints=0
    totalcredits=0
    for i in range(len(listofsubjects)):
        subjecttotal=cat1_contrib[i]+cat2_contrib[i]+tee_contrib[i]+internalmarks[i]
        gp=grade_point(subjecttotal)
        print(f"{listofsubjects[i]}: Total = {subjecttotal:.2f}, Grade Point = {gp}")
        totalpoints+=gp*creditlist[i]
        totalcredits+=creditlist[i]
    sgpa=totalpoints/totalcredits
    print(f"\nSGPA for this semester: {sgpa:.2f}")
    return sgpa

def target_sgpa(listofsubjects,en,cat1marks,cat2marks):
    if en==3:
        print("All exams have already been conducted. Use SGPA calculator (choice 4) instead.")
        return
    target=float(input("Enter your target SGPA: "))
    required_gp=math.ceil(target)
    if required_gp>10:
        print("Target SGPA is not achievable.")
        return
    needed_total=min_total_for_grade(required_gp)
    if en==1:
        pending=[("CAT2",50,15),("TEE",100,30),("Internal Assessment",40,40)]
    else:
        pending=[("TEE",100,30),("Internal Assessment",40,40)]
    total_pending_weight=sum(weight for (_,_,weight) in pending)
    for i in range(len(listofsubjects)):
        fixed=0
        if en>=1:
            fixed+=cat1marks[i]*0.3
        if en>=2:
            fixed+=cat2marks[i]*0.3
        remaining_needed=needed_total-fixed
        print(f"\n{listofsubjects[i]}:")
        if remaining_needed<=0:
            for (name,raw_max,weight) in pending:
                print(f"  {name}: 0 out of {raw_max} needed (already on track)")
        elif remaining_needed<=total_pending_weight:
            p=remaining_needed/total_pending_weight
            for (name,raw_max,weight) in pending:
                needed_raw=p*raw_max
                print(f"  {name}: Score at least {needed_raw:.2f} out of {raw_max}")
        else:
            print("  Target SGPA is not achievable for this subject.")