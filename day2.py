input = open("input2.txt","r").readlines()
#input = ["aabba\n","aaabbbcccdd\n"]
for x in range(0,len(input)):
    input[x] = input[x][0:-1]

numberOf2 = 0
numberOf3 = 0
for word in input:
    seen = set()
    num3 = True
    num2 = True
    for i in range(0,len(word)):
        if word[i] not in seen:
            seen.add(word[i])
            n = 1
            for j in range(i+1,len(word)):
                #print(word[i] + "==" + word[j])
                if word[i] == word[j]:
                    n += 1
            if n == 2 and num2:
                numberOf2 += 1
                num2 = False
            if n == 3 and num3:
                numberOf3 += 1
                num3 = False

print(numberOf2)
print(numberOf3)
print(numberOf2 * numberOf3)