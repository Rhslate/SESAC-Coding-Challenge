#r = row
#c = column
#p = princess
#m = bot

def nextMove(N,r,c,grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'p':
                p, m = i, j

def UP():
    print("UP")
def DOWN():
    print("DOWN")
def LEFT():
    print("LEFT")
def RIGHT():
    print("RIGHT")

def r():
    print(r)
def c():
    print(c)

if r > p:
    nextMove: "UP"
if r <p:
    nextMove: "DOWN"
if c > m:
    nextMove: "LEFT"
if c < m:
    nextMove: "RIGHT"

nextMove(N,r,c,grid)

