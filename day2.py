#horribly inefficient program

f=open('input.txt','r').read().split(',')
pt1=0
pt2=0
items=[]

#parse into nested list (keeping as strings for this problem)
for i in f:
    items.append(i.split('-'))

#pt2 function horribly designed
def checkItem(numstr):
    total=0
    check=True
    check2=False
    #first loop is for divisions of how long a number could be (ex. 123456 could be devised by 1, 2, 3 for this problem)
    for i in range(1,len(numstr)):
        #check2 is to break out if the comparison string repeated adds to the entire number (ex. '67' repeated 3 times matches the whole number of '676767')
        if check2:
            break
        check2 = False
        item = numstr[:i]
        #start count at 1 to account for the existing instance of the repeated sequence
        count=1
        #for loop to start looking at the next numbers after said division, then jumping by said division
        for j in range(i, len(numstr),i):
            #if it fails it breaks out
            if item != numstr[j:j+i]:
                # print('discredited')
                check=False
                break
            #adds a count for totalling if the sequence repeats and checks if the entire number has been made up
            else:
                count+=1
                #didn't know you could multiply strings to have them repeat
                if count*numstr[j:j+i]==numstr:
                    check2=True
                    break
        #scoring using count to reconstruct the original invalid ID
        if check:
            out=""
            for _ in range(count):
                out+=item
            total+=int(out)
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
