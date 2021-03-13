N,K = map(int, input().split())
diamonds = []
for x in range(N):
    diamonds.append(int(input()))

high = 0

for x in range(N):
    temp = []
    temp.append(diamonds[x])
    for y in range(N):
        possible = True
        if x == y:
            continue
        else:
            for z in temp:
                if abs(z-diamonds[y]) <= K:
                    continue
                else:
                    possible = False
                    break
            if possible == True:
                temp.append(diamonds[y])

    high = max(high, len(temp))
print(high)