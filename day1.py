f=open("input.txt",'r').read().splitlines()
pos=50
pt1=0
pt2=0

#keep position in 0-99 range
def keepInRange(x):
    while x<0:
        x+=100
    while x>99:
        x-=100
    return x

# takes current position and an instruction (ex. R69) and counts how many times it passes 0
def passZero(cur,inst):
    count=0
    if inst[:1]=='L':
        for i in range(1,int(inst[1:])):
            if(keepInRange(cur-i))==0:
                count+=1
    else:
        for i in range(1,int(inst[1:])):
            if(keepInRange(cur+i))==0:
                count+=1
    return count

# runs through instrtion list running passZero function and counting the times the dial ends on 0
for i in f:
    if i[:1]=='L':
        new = pos - int(i[1:])
        pt2+=passZero(pos,i)
        pos=keepInRange(new)
    else:
        new = pos + int(i[1:])
        pt2 += passZero(pos,i)
        pos = keepInRange(new)
    if pos==0:
        pt1+=1

#pt1 is number of times ended on 0. pt2 is also that and the number of times zero is passed
print(pt1,pt1+pt2)
