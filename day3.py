input = open("input3.txt","r").readlines()
#input = ["aabba\n","aaabbbcccdd\n"]
for x in range(0,len(input)):
    input[x] = input[x][0:-1]


