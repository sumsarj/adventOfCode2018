input = open("input3.txt","r").readlines()
#input = ["aabba\n","aaabbbcccdd\n"]
for x in range(0,len(input)):
    input[x] = input[x][0:-1]


#1. check boundaries of the rectangles(coords) and see if they overlap. First in X, then in Y if they do overlap in X
#2. just mark the area as overlapped and move on to #1. (dont wanna calculate the same overlapped area twice)
#3. when all are checked, calculate the overlapped area