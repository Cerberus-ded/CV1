import random
X = [[random.randint(-10,10) for j in range(4)] for i in range(5)]
Y = [[random.randint(-10,10) for j in range(4)] for i in range(5)]
xmax=-11
ymax=-11
x_coord=[]
y_coord=[]
for i in range(5):
    for j in range(4):
        if xmax < X[i][j]:
            xmax = X[i][j]
            x_coord.append(j)
            x_coord.append(i)
        if ymax < Y[i][j]:
            ymax = Y[i][j]
            y_coord.append(j)
            y_coord.append(i)
print('матрица Х')
for i in range(5):
    for j in range(4):
        print(X[i][j], end = ' ')
    print()
print('матрица Y')
for i in range(5):
    for j in range(4):
        print(Y[i][j], end = ' ')
    print()


X[x_coord[len(x_coord)-1]][x_coord[len(x_coord)-2]] = ymax
Y[y_coord[len(y_coord)-1]][y_coord[len(y_coord)-2]] = xmax

for i in range(5):
    for j in range(4):
        if X[i][j] < 0:
            X[i][j] = xmax

print('изменённая матрица Х')
for i in range(5):
    for j in range(4):
        print(X[i][j], end = ' ')
    print()
print('изменённая матрица Y')
for i in range(5):
    for j in range(4):
        print(Y[i][j], end = ' ')
    print()