input = open("input3.txt","r").readlines()
#input = ["aabba\n","aaabbbcccdd\n"]
for x in range(0,len(input)):
    input[x] = input[x][0:-1]

# #123 @ 3,2: 5x4
#1. check boundaries of the rectangles(coords) and see if they overlap. First in X, then in Y if they do overlap in X
#2. just mark the area as overlapped and move on to #1. (dont wanna calculate the same overlapped area twice)
#3. when all are checked, calculate the overlapped area

class Point(object):
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y
parsedInput = []
for i in range(0,len(input)):
    a = input[i].split("@ ")[1]
    x0 = int(a.split(",")[0])
    b = a.split(",")[1]
    y0 = int(b.split(":")[0])
    c = b.split(": ")[1]
    x1 = int(c.split("x")[0])
    y1 = int(c.split("x")[1])
   
    pi = (Point(x0,y0),Point(x1,y1))
    seen = set()

    for j in range(i+1,len(input)):
        a = input[j].split("@ ")[1]
        x0 = int(a.split(",")[0])
        b = a.split(",")[1]
        y0 = int(b.split(":")[0])
        c = b.split(": ")[1]
        x1 = int(c.split("x")[0])
        y1 = int(c.split("x")[1])
        pj = (Point(x0,y0),Point(x1,y1))

        if(pi[0].x > pj[1].x or pi[1].x > pj[0].x):
            continue
        if (pi[0].y < pj[1].y or pi[1].y < pj[0].y):
            continue
        #They overlap!
        


 
