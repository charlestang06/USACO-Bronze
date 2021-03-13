N = int(input())
daisy = list(map(int, input().split()))

counter = N
pairs = []
for i in range(0, N-1):
    first = daisy[i]
    for j in range(i+1, N):
        second = daisy[j]
        totalPetals = 0
        petals = []
        for x in range(i, j+1):
            totalPetals += daisy[x]
            petals.append(daisy[x])
        if totalPetals/(j-i+1) in petals:
            counter += 1

print(counter)

