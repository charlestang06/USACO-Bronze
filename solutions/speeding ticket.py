N,M = map(int, input().split())

limits = []
len_limit = []

speeds = []
len_speed = []

for x in range(N):
    input_ = list(map(int, input().split()))
    limits.append(input_[1])
    len_limit.append(input_[0])

for x in range(M):
    input_ = list(map(int, input().split()))
    speeds.append(input_[1])
    len_speed.append(input_[0])


total_limits = []
counter = 0
for x in limits:
    for y in range(len_limit[counter]):
        total_limits.append(x)
    counter += 1

total_speed = []
counter = 0
for x in speeds:
    for y in range(len_speed[counter]):
        total_speed.append(x)
    counter += 1

max_diff = 0
for x in range(100):
    max_diff = max(max_diff, total_speed[x] - total_limits[x])

print(max_diff)


