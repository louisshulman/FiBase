def npv(a, b, c, d, e, i):
    lst = [a, b, c, d, e]
    dcilst = []
    for num in range(len(lst)):
        dci = lst[num] / (1 + i)**(num)
        dcilst.append(dci)
    NPV = sum(dcilst)
    print(dcilst)
    print(NPV)


npv(-100, 50, 40, 30, 20, .04)