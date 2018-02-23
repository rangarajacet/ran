lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for n in range(lower,upper+1):
    if(n%2!=0):
        print(n)
