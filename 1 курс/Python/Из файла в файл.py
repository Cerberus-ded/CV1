import random
n=int(input('Введите числа: '))
k=2
b=[]
with open('task.txt','w') as chisla:
 for i in range (n):
    a=random.randint(1,20)
    chisla.write (str(a)+' ')
    b.append(a)
chisla.close()    
with open ('task1.txt','w') as chisla1:
    for i in (b):
       if i%2==0:
         chisla1.write(str(i)+' ')
chisla1.close()
       
