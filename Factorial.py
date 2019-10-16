#Factorial

n=int(input("Enter the number for which factorial is needed: "))

if n==0 or n==1:
    print(1)
else:
    x=1
    for i in range(1,n+1):
        x = x*i

    print(x)

# Anonymous function

import sys

