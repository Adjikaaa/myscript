
k = 11

f = open("keys.log", "r")

res = []
for line in f:
    lst = (line.strip()).split("  ")
    lst = lst[0].split(" ")
    sub = []
    for l in lst:
        a = int(l)    
        if abs(a) in [k,k+1,k+2,k+3]:
            sub.append(a)
    if sub not in res:
        res.append(sub)


for i in range(len(res)):
    print(res[i])            

print(len(res))