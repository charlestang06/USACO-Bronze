R_C = input().split()
R = int(R_C[0])
C = int(R_C[1])

competition = []
distance = [] #by number/index
distance_to_ranking = []
for x in range(0, C):
    distance_to_ranking.append(0)
    distance.append(0)


for x in range(0, R):
    temp_input = input()
    competition.append(temp_input)

for x in competition:
    for y in range(C-2, 2, -1):
        if x[y] != '.':
            distance[int(x[y]) - 1] = int(C - y - 1)
            distance_to_ranking[C-y-1] = 1
            break

ranking =1
for x in range(0, C):
    if distance_to_ranking[x] == 1:
        distance_to_ranking[x] = ranking
        ranking +=1

for x in range(0, 9):
    print (distance_to_ranking[distance[x]])