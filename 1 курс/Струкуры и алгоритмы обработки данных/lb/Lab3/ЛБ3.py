import math
x = float(input('¬ведите x'))
e = float(input('¬ведите погрешность e'))
while (x<=0) or (x>2) or e<=0:
    x = float(input('¬ведите x'))
    e = float(input('¬ведите e'))
s = math.log(x)
count = 0
p = 1
s1 = (x-1)
x0=(x-1)
while abs(s - s1) > e or count < 1000:
    x *= x0
    p += 1
    count += 1
    if p%2==0:
        s1 -= x / p
    else:
        s1 += x / p
print('s = ',s,'s1=',s1,'count = ', count)
    
    
    
    
