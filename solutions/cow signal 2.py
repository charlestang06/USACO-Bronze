row,column,multiplier = map(int, input().split())

# M X N Paper, K times amplify
start = []

for x in range(row):
    start.append(list(input()))

final_width_K = []

final_height_K = []

for i in range(row): #row
    string = ""
    for k in range(column): #letter
        letter = str(start[i][k])
        for j in range(multiplier): #multiply
            string += letter
    final_width_K.append(string)

for x in range(len(final_width_K)):
    for y in range(multiplier):
        final_height_K.append(final_width_K[x])

for x in final_height_K:
    print(x)


