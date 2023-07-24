import random
a=[[random.randint(1, 50) for j in range (5)]for i in range(5)]
b=[[random.randint(1, 50) for j in range (5)]for i in range(5)]
amin, bmin=999, 999
print()
for i in range(5):
    for j in range(5):
        print(a[i][j], end=' ')
    print()
print()
for i in range(5):
    for j in range(5):
        print(b[i][j], end=' ')
    print()

for i in range(5):
    for j in range(5):
        if a[i][j]<amin:
            amin=a[i][j]
        if b[i][j]<bmin:
            bmin=b[i][j]
for i in range(5):
    for j in range(5):
        if a[i][j]==amin:
            dyn1=j

for x in range(5):
    for y in range(5):
        if b[x][y]==bmin:
            dyn2=y


for i in range(5):
    a[i][dyn1], b[i][dyn2] = b[i][dyn2], a[i][dyn1]
    
print()
for i in range(5):
    for j in range(5):
        print(a[i][j], end=' ')
    print()
    
print()
for i in range(5):
    for j in range(5):
        print(b[i][j], end=' ')
    print()
