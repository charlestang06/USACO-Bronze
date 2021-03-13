N = int(input())
road_ends = []
barns_list = []



for x in range(0, N):
    barns_list.append(x)

for x in range(0, N):
    road_ends.append(-1)

for x in range(0, N-1):
    temp_list = input().split()
    road_ends[int(temp_list[1])-1] = int(temp_list[0])-1

for x in range(0, N):
    wasthere = []
    for y in range(0, N):
        wasthere.append(False)
    index = x
    while wasthere[index] == False and road_ends[index] != -1:
        wasthere[index] = True
        index = road_ends[index]
    wasthere[index] = True
    if False not in wasthere:
            print(x+1)
            exit()

print(-1)



