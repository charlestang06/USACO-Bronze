N_M = input().split()
N = int(N_M[0])
M = int(N_M[1])

pastures = [0 for i in range(N)]
pastures[0] = 1

condition1 = []
condition2 = []

for x in range(M):
    input_line = input().split()
    condition1.append(int(input_line[0]))
    condition2.append(int(input_line[1]))


for x in range(1, N): #pastures
    seed_number = 1

    for i in range(0, len(condition1)):
        if x == condition1[i] and pastures[condition2[i]-1] == seed_number:
            seed_number += 1
        elif x == condition2[i] and pastures[condition1[i] - 1] == seed_number:
            seed_number += 1

    pastures[x] = seed_number

string = ""
for x in pastures:
    string = string + str(x)

print(pastures)


