N = int(input())
characteristics = []
for x in range(0, N):
    input_ = input().split()
    characteristics.append(input_[2:])

#maxsimilarities between two + 1
similarities = 0
max_similarities = 0
for x in range(len(characteristics)): #1st animal
    for y in range(x+1, len(characteristics)): #second animal
        for z in range(len(characteristics[x])): #first character
            for a in range(len(characteristics[y])): #second characteristic
                if characteristics[x][z] == characteristics[y][a]:
                    similarities += 1
        if similarities > max_similarities:
            max_similarities = similarities
        similarities = 0


max_similarities += 1
print(max_similarities)