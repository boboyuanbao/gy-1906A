#for a in range (100):
    if (a % 2 == 0 and a!=0):
        print(a)


#for i in range (9):
    for a in range (9):
        if(a <= i):
            print(i+1,'x', a+1,'=',(i+1)*(a+1),"\t",end='')
    print()
#for i in range (1,10):
    for a in range (1,1+i):
        print(i,"X",a,'=','i*a','\t',end='')
    print()

for i in range(2,100):
    n=2
    for j in range (2,i+1):
        if(i%n == 0):
            break
        n = n+1
    if (n == 1):
        print(i)
