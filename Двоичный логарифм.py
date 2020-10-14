import math

N = int(input())

b = math.log(N, 2)
c = round(b)
if c == 0:
    print(c)
elif c == b:
    print(c)
elif c > b:
    print(c)
else:
    print(c+1)
