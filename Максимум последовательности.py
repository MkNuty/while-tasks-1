i = int(input())
z = 0
u = i

while i != 0:
    if max(u, i) > z:
        z = max(u,i)
        u = i
    i = int(input())
    
print(z)
