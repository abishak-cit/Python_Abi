import math
def isperfectsquare(x,y):
    z = x * y
    s = math.sqrt(z)
    return (s - math.floor(s) == 0)
x,y = map(int,(input().split()))
if(isperfectsquare(x,y)):
    print('yes')
else:
    print('no')
