nlst = [-20000, 7000, 5000, 8000, 9000]
def npv(i):
    lst = nlst
    dcilst = []
    for num in range(len(lst)):
        if num == 0:
            dci = round((lst[0]), 2 )
        else:
            dci = round(lst[num] / ((1 + i)**(num)), 2)
        print(dci)
        dcilst.append(dci)
    print(dcilst)
    NPV = round((sum(dcilst)), 2)
    print("NPV = " + str(NPV))
    if NPV >= 0:
        print("Project made the required annual rate of return of " + str(i) + "%")
        print("Project go ahead approved")
    else:
        print("Project did not make the required annual rate of return of " + str(i) + "%")
        print("Project denied")

print(npv(0.08))
