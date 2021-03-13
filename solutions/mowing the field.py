N = int(input())
directions = []
for x in range(N):
    input_ = input().split()
    directions.append([input_[0], int(input_[1])])


path = []
path.append([0, 0])
current = [0, 0]
max_grow = 100000000



for x in range(len(directions)):
    if directions[x][0] == 'N':
        num_moves = directions[x][1]
        for j in range(num_moves):
            current[1] += 1
            for i in range(len(path)-1, -1, -1):
                if path[i] == current:
                    max_grow = min(max_grow, len(path)-1-i)
                    break
            path.append(current)
    elif directions[x][0] == 'E':
        num_moves = directions[x][1]
        for j in range(num_moves):
            current[0] += 1
            for i in range(len(path)-1, -1, -1):
                if path[i] == current:
                    max_grow = min(max_grow, len(path)-1-i)
                    break
            path.append(current)
    elif directions[x][0] == 'S':
        num_moves = directions[x][1]
        for j in range(num_moves):
            current[1] -= 1
            for i in range(len(path)-1, -1, -1):
                if path[i] == current:
                    max_grow = min(max_grow, len(path)-1-i)
                    break
            path.append(current)
    elif directions[x][0] == 'W':
        num_moves = directions[x][1]
        for j in range(num_moves):
            current[0] -= 1
            for i in range(len(path)-1, -1, -1):
                if path[i] == current:
                    max_grow = min(max_grow, len(path)-1-i)
                    break
            path.append(current)

if max_grow == 100000000:
    print('-1')
else:
    print(max_grow)
