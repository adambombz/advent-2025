#horribly inefficient program

f=open('input.txt','r').read().split(',')
pt1=0
pt2=0
items=[]

#parse into nested list (keeping as strings for this problem)
for i in f:
    items.append(i.split('-'))

#pt2
def checkItem(numstr):
    total=0
    check=False
    #first loop is for divisions of how long a number could be (ex. 123456 could be devised by 1, 2, 3 digits for this problem)
    for i in range(1,len(numstr)):
        #check is to break out if the comparison string repeated adds to the entire number (ex. 67 3 times is 676767)
        if check:
            break
        item = numstr[:i]
        count=1
        for j in range(i, len(numstr),i):
            if item != numstr[j:j+i]:
                break
            else:
                count+=1
                if count*numstr[j:j+i]==numstr:
                    check=True
                    break
        if check:
            total+=int(numstr)
    return total

#iterate through ranges, then through all the numbers in said range. pt1 solution is included as it's only needed to compare the front and back of the number. pt2 uses the function
for i in items:
    for num in range(int(i[0]),int(i[1])+1):
        #back to string for this problem
        numstr=str(num)
        #compare front half and right half and add to pt1 if same
        if numstr[:int(len(numstr) / 2)] == numstr[int(len(numstr)/ 2):]:
            pt1+=int(numstr[:int(len(numstr) / 2)]+numstr[:int(len(numstr) / 2)])
        pt2+=checkItem(numstr)

print(pt1, pt2)

