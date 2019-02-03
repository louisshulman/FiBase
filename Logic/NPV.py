from Financial import finance
lst = []
a = finance.npv(10000, 500, .02, 8)
print(a)

def NCI(a, b, c, d):
    ave = float((a + b + c + d) / 4)
    return ave

def NPV(ico, r, n, a, b, c, d):
    dum = float(NCI(a, b, c, d))
    lol = finance.npv(ico, dum, r, n)
    print(lol)

print(NPV(10000, .02, 5, 100, 200, 300, 50))

