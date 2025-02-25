n = int(input("enter:"))
start = 1
for i in range(1,n+1):
    for j in range(0,n-i):
        print(' ',end='')
    for j in range(0,start):
        print('*',end='')
    print()
    start += 2