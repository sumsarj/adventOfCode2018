input = open("input2.txt","r").readlines()
#input = ["aabba\n","aaabbbcccdd\n"]
for x in range(0,len(input)):
    input[x] = input[x][0:-1]


for i in range(0,len(input)):

    for j in range(i+1,len(input)):
        n = 0
        for g in range(0,len(input[i])):  
            if input[i][g] != input[j][g]:
                n += 1
        if n == 1:
            ret = ""
            for l in range(0,len(input[i])):
                if input[i][l] == input[j][l]:
                    ret += input[i][l]
            print(ret)



