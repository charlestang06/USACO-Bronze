N = int(input())
positions = []

for x in range(N):
    input_line = input().split()
    positions.append([int(input_line[0]), int(input_line[1])])

sorted_positions = sorted(positions)

minRadius = 1000000

for x in range(len(sorted_positions)-1):
    if sorted_positions[x][1] == 0 and sorted_positions[x-1][1] == 1:
        distance = abs(sorted_positions[x-1][0] - sorted_positions[x][0])
        if distance < minRadius:
            minRadius = distance
    if sorted_positions[x][1] == 0 and sorted_positions[x+1][1] == 1:
        distance = abs(sorted_positions[x][0] - sorted_positions[x+1][0])
        if distance < minRadius:
            minRadius = distance

minRadius -= 1

visited = [False] * len(sorted_positions)

counter = 0
previous = 0
for x in range(0, len(sorted_positions)):
    if x == 0:
        if sorted_positions[x][1] == 1:
            counter += 1
    elif sorted_positions[x][1] == 1:
        if abs(sorted_positions[x][0] - previous) <= minRadius:
            pass
        else:
            counter += 1
    elif sorted_positions[x][1] == 0:
        pass

    previous = sorted_positions[x][0]

print(counter)
