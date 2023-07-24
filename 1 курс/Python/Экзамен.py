import random
n=int(input('Введите числа: '))
b=[]
i=0
c=[]
with open('Ex1.txt','w') as chisla:
 for i in range (n):
     a=random.randint(-999,999)
     b.append(a)
 chisla.write (str(b)+' ')
chisla.close()
with open ('Ex1.txt', 'r') as chisla2:
    for i in range (n):
        chisla2.read(b[i])
        print(b[i])
    for i in range(len(b)):
        if int(b[i])>50 and int(b[i])<350:
            c.append(b[i])
chisla2.close
print(c)
print()
print()
def counter(summa):
    count=0
    for x in range (100, 1000):
        if int(str(x)[0])+int(str(x)[1])+int(str(x)[2])==summa:
            count+=1
            print(x)
    print(str(count)+'-количество')
counter(4)
