N = int(input())
ranges = []
for x in range(N):
    ranges.append(list(map(int, input().split())))

covered = [False for x in range(1000)]

for x in range(N):
    start = ranges[x][0]
    end = ranges[x][1]
    for y in range(start, end):
        covered[y] = True

regTime = 0
for x in covered:
    if x == True:
        regTime += 1
high = 0
for x in range(N):
    temptime = 0
    tempRange = ranges
    print(tempRange)
    tempCovered = covered
    tempRange.pop(x)
    for y in range(N-1):
        start = tempRange[y][0]
        end = tempRange[y][1]
        for z in range(start, end):
            tempCovered[z] = True
    for i in tempCovered:
        if i == True:
            temptime += 1
    high = max(high, temptime)

print(high)


