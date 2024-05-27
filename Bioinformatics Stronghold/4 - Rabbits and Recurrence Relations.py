acount = 0 # Num adult pairs
bcount = 1 # Num baby pairs
total = 0 # Total rabbit pairs
n = 32 # Number of cycles
k = 4 # Number of pairs birthed by adult pair per cycle

for i in range(n):
    if i > 0: 
        babiesMatured = bcount
        bcount = acount * k
        acount += babiesMatured
        total = acount + bcount
    print("Num Adult Pairs: " + str(acount) + ", Num Baby Pairs: " + str(bcount) + ", Total Pairs: " + str(total))