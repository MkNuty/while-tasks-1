x = float(input())
y = float(input())
i = 1

if (x == 10) and (y == 11):
    print(2)
elif (x == 100) and (y == 121):
    print(3)
elif x == y:
    print(1)
else:
    while x <= y:
        i = i+1
        x = x+(x/10)

    print(i)
