def npv(a, b, c, d, e, i):
    lst = [a, b, c, d, e]
    dcilst = []
    for num in range(len(lst)):
        dci = lst[num] / (1 + i)**(num)
        dcilst.append(dci)
    NPV = round((sum(dcilst)), 2)
    print("NPV = " + str(NPV))
    if NPV >= 0:
        print("Project made the required annual rate of return of " + str(i) + "%")
        print("Project go ahead approved")
    else:
        print("Project did not make the required annual rate of return of " + str(i) + "%")
        print("Project denied")

npv(-100, 50, 40, 30, 20, .04)