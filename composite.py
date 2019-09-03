N = int(input("Enter the N:"))
factor = 0
for i in range(0,N):
    if(N%i == 0):
        factor = i
if(factor > 1):
    print("yes")
elif(factor == 1):
    print("yes or no")
else:
    print("no")
