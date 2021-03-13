N,M = map(int, input().split())
spotty = []
plain = []

for x in range(N):
    spotty.append(list(input()))
for y in range(N):
    plain.append(list(input()))

counter = 0
for column in range(M):
    disjoint = True
    temp_spotty = []
    temp_plain = []
    for i in range(N):
        temp_spotty.append(spotty[i][column])
        temp_plain.append(plain[i][column])
    for x in temp_spotty:
        if x in temp_plain:
            disjoint = False
            break
    if disjoint == True:
        counter += 1

print(counter)


