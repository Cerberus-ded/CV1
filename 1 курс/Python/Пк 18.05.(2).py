import random
n=int(input('Введите числа: '))
b=[]
with open('chisla.txt','w') as chisla:
 for i in range (n):
     a=random.randint(-50,50)
     b.append(a)
 chisla.write (str(b)+' ')
chisla.close()
with open('chisla.txt','r') as chisla1:
    for i in range(n):
        chisla1.read(b[i])
        print(b[i])
    flag=1
    for i in range (n-1):
        if b[i]>b[i+1]:
            flag=0
    if flag==0:
        print('Неправильно')
    else:
        print('Правильно')
chisla1.close()
