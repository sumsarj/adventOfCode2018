
file = open("input.txt","r")
a = 0
for l in file:
    if l[0] == '+':
        a += int(l[1:])
    else:
        a -= int(l[1:])

print (a)