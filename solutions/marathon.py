N = int(input())

checkpoints = []
for x in range(N):
    input_ = list(map(int, input().split()))
    checkpoints.append(input_)

low = 100000000
for x in range(1, N):
    temp = checkpoints.copy()
    temp.pop(x)
    distance = 0
    position = temp[0]
    for y in range(1, N-1):
        old_x = position[0]
        old_y = position[1]
        new_x = temp[y][0]
        new_y = temp[y][1]
        distance += (abs(new_y-old_y) + abs(new_x-old_x))
        position = temp[y]
    low = min(low, distance)

print(low)