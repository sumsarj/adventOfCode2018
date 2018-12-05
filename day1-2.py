b = 0
a = 0
seen = set()
uniq = []
b = True
while b:
 
    file = open("input.txt","r")
    for l in file:
        if l[0] == '+':
            a += int(l[1:])
        else:
            a -= int(l[1:])
        if a not in seen:
            seen.add(a)
            
        else:
            print(a)
            b = False
            break

 