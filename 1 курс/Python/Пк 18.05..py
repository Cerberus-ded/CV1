def check_num(num, next_is_negative):
    if next_is_negative and num < 0:
        return True
    elif not next_is_negative and num > 0:
        return True
    return False

def is_alternates(l):
    next_is_negative = l[0] > 0

    for i in range(1, len(l)):
        num = l[i]
        if not check_num(num, next_is_negative):
            return False
           
        next_is_negative = not next_is_negative
         
    return True

l = [6, -2, 8, -1, 5, -3, 22]
b=(is_alternates(l))
print(is_alternates(l)) 

if b==False:
    p=1
    for i in range (len (l)):
        if l[i]<0:
            p=p*l[i]
    print(p)
    
else:
    p=0
    for i in range (len (l)):
        if l[i]>0:
            p=p+l[i]
    print(p)
    
