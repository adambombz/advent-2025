f=open('input.txt','r').read().splitlines()

f=[list(i) for i in f]

pt1, pt2 = 0, 0
removed=[69]

# print(f)

def checkpos(grid, x, y):
    maxRolls=3
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx != 0 or dy != 0) and len(grid) > x + dx >=0 and len(grid[x]) > y + dy >=0:
                if grid[x+dx][y+dy]=='@':
                    count+=1
    return count<=maxRolls

def newgrid(old, r):
    for i in r:
        old[i[0]][i[1]]='.'
    return old

def printer(f):
    for i in f:
        print(i)
    print()

while len(removed)!=0:
    removed=[]
    # printer(f)
    for i in range(len(f)):
        for j in range (len(f[i])):
            if f[i][j] == '@' and checkpos(f, i, j):
                removed.append([i,j])
                if pt2==0:
                    pt1+=1
    f = newgrid(f, removed)
    pt2+=len(removed)

print("part1:",pt1,"\npart2:",pt2)