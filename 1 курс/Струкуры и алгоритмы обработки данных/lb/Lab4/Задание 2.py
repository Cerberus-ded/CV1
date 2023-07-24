import random
X = [[random.randint(-10,10) for j in range(6)] for i in range(5)]
count = []
for j in range(6):
    count.append(0)
    for i in range(5):
        if X[i][j] % 2 == 1:
            count[j] += 1
print('матрица')
for i in range(5):
    for j in range(6):
        print(X[i][j], end = ' ')
    print()
print(count)