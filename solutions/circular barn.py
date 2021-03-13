num_rooms = int(input())
r_size = [int(input()) for x in range(num_rooms)]

min_dist = 1000000000

for x in range(num_rooms):
    total_distance = 0
    starting = r_size[x]
    temp_rooms = r_size
    if x != 0:
        temp_rooms = temp_rooms[x:] + temp_rooms[0:x]
    for x in range(len(temp_rooms)):
        total_distance += (x) * temp_rooms[x]

    min_dist = min(total_distance, min_dist)

print(min_dist)