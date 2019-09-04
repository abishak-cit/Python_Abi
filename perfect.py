import math
def isperfect(product):
    scr = math.sqrt(product)
    return ((scr-math.floor(scr))== 0)
N = int(input())
M =int(input())
product = N*M
if(isperfect(product)):
    print('yes')
else:
    print('no')
