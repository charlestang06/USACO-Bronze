N = int(input())
road = input()

for length in range(1, N+1):
    possible = True
    temp = set()
    for y in range(N-length+1):
        temp_road = str(road[y:y+length])
        if temp_road in temp:
            possible = False
            break
        else:
            temp.add(temp_road)
    if possible == True:
        print(length)
        exit()






