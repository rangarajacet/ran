r=int(input("Enter upper limit: "))
for n in range(2,r+1):
    k=0
    for i in range(2,n//2+1):
        if(n%i==0):
            k=k+1
    if(k<=0):
        print(n)
