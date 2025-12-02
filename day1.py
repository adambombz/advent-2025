f=open("input.txt",'r').read().splitlines()
pos=50
pt1=0
pt2=0

def keepInRange(x):
    while x<0:
        x+=100
    while x>99:
        x-=100
    # print("passed:",passed)
    return x

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

for i in f:
    print(pt2, pos, i)
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

print(pt1,pt1+pt2)