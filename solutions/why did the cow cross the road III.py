num_cows = int(input())

array = []

for x in range(num_cows):
    array.append(list(map(int, input().split())))

array.sort()

time  = 0
for x in range(num_cows):
    if array[x][0] <= time:
        time += array[x][1]
    elif array[x][0] > time:
        diff = array[x][0] - time
        time += diff + array[x][1]
print(time)