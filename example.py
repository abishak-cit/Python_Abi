from math import pow
number = int(input("Enter the number:"))
sum=0
while(number>0):
    number1 = number % 10
    sum = sum + pow(number1,2)
    number = number//10
print(int(sum))


 
