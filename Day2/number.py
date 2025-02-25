n = int(input("Enter:"))
for i in range(1,n+1):
        start = 1
        for j in range(0,i):
            print(f"{start} ",end='')
            start+=1
        print()