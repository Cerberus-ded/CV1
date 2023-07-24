import random
pins=[]
nums=[]
count1, count2, count3, count4 = 0, 0, 0, 0
n = int(input('Количество сотрудников: '))
alph='123456789qwertyuiopasdfghjklzxcvbnm'
for x in range(1,n+1):
    pin=''
    for y in range(4):
        pin+=alph[random.randint(0,34)]
    pins.append(pin)
    nums.append(str(x))

for x in range(n):
    print(pins[x], f'[{nums[x]}]')
                
pohozh=[]
def numcheck(nums):
    global pohozh
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            count=0
            if len(nums[x])==len(nums[y]):
                for z in range(len(nums[x])):
                    if nums[x][z] != nums[y][z]:
                        count+=1
                if count == 1:
                    pohozh.append( f'{str(x+1)} {str(y+1)}'.split() )    
            elif abs(len(nums[y])-len(nums[x]))<=1:
                if len(nums[y])>len(nums[x]):
                    for z in range(len(nums[x])):
                        if nums[x][z] != nums[y][z]:
                            count+=1
                            if count==1:
                                break
                    if count==0:
                        pohozh.append( f'{str(x+1)} {str(y+1)}'.split() )
                    else:
                        count=0
                        for z in range(len(nums[x])):
                            if nums[x][z] != nums[y][z+1]:
                                count+=1
                                if count==1:
                                    break
                        if count==0:
                            pohozh.append( f'{str(x+1)} {str(y+1)}'.split() )
                        
numcheck(nums)
#for i in range(len(pohozh)):
    #print(pohozh[i])

for x in range(len(pohozh)):
    count=0
    for y in range(4):
        if pins[int(pohozh[x][0])-1][y] != pins[int(pohozh[x][1])-1][y]:
            count+=1
    if count==1:
        count1+=1
    elif count==2:
        count2+=1
    elif count==3:
        count3+=1
    elif count==4:
        count4+=1
    
        
print('различаются в 1 позиции: ' + str(count1))
print('различаются в 2 позициях:  ' + str(count2))
print('различаются в 3 позициях: ' + str(count3))
print('различаются в 4 позициях: ' + str(count4))
