N_T = input().split()
N = int(N_T[0])
T = int(N_T[1])

interactions = []
input_condition = input()
conditions = list(input_condition)
conditions = [int(x) for x in conditions]

for x in range(T):
    input_line = input().split()
    input_line = [int(x) for x in input_line]
    interactions.append(input_line)

sorted_interactions = sorted(interactions)

largest_k = 0
minimum_k = T
patient_zero = 0


for cow_num in range(0, N): #zeros -- x is cow number
    temp_conditions = [0 for x in range(len(conditions))]
    temp_conditions[cow_num] = 1
    for y in range(0, len(interactions)): #loops through the process
        if cow_num == interactions[y][1]-1:
            temp_conditions[interactions[y][2]-1] = 1
        elif cow_num == interactions[y][2]-1:
            temp_conditions[interactions[y][1]-1] = 1
    if temp_conditions == conditions: #checks if condition arrays match, if so, counter + 1
        patient_zero += 1



print(patient_zero)

