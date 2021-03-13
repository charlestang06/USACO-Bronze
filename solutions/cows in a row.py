N = int(input())
IDs = []
uniques = []

for x in range(N):
    IDs.append(int(input()))

for x in IDs:
    if x not in uniques:
        uniques.append(x)

high = 0
for x in uniques:
    temp = IDs.copy()
    for y in temp:
        if y == x:
            temp.remove(y)
    counter = 1
    for z in range(len(temp)):
        if z == 0:
            continue
        elif temp[z] == temp[z-1]:
            counter += 1
        else:
            high = max(high, counter)
            counter = 1

print(high)
