N_M_K = input().split()
Number_of_cows = int(N_M_K[0])
M_cows_arranged = int(N_M_K[1])
K_cows_demanding = int(N_M_K[2])

inequality = input().split()
for x in inequality:
    x = int(x)

positions = []

for x in range(Number_of_cows):
    positions.append(None)

for x in range(K_cows_demanding):
    temp_input = input().split()
    index = int(temp_input[1]) - 1
    positions[index] = int(temp_input[0])

for x in range(len(inequality)-1, -1, -1):
    if (int(inequality[x]) in positions) and positions[int(positions.index(int(inequality[x])))-1] == None:
        positions[positions.index(int(inequality[x])) - 1 ] = int(inequality[x-1])
        y = 0
        while inequality[x-1-y] not in positions and positions[positions.index(inequality[x-1])-y-1]:
            positions[positions.index(x-1)-y-1] = inequality[x-y-1]
            y += 1


counter = 1
for x in positions:
    if x == None:
        break
    counter += 1

print(counter)
