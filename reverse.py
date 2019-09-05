#input of num
num = int(input())
#initial value of reverse
reverse_num = 0
#conditon for entry using while loop
while(num>0):
  #remainder of the given no
  remainder = num % 10
  # formula of the reverse
  reverse_num = (reverse_num * 10) + remainder
  #floor division of the num
  num = num//10
#display the reverse
print(reverse_num)
