n = int(input('Enter:'))
t = 2*n-1
for i in range(1,2*n+1):
        if i<=n:
            for j in range(0,n-i):
                print(' ',end='')
            for j in range(0,2*i-1):
                print('*',end='')
            print()
        else:
            d = i-n
            for j in range(0,d-1):
                print(' ',end='')
            for j in range(0,t):
                print('*',end='')
            t -= 2
            print()
           