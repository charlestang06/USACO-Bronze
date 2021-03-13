N = input()
A = input()
B = input()

listA = []
for x in range(0, len(A)-1):
    listA.append(A[x])

listB = []
for x in range(0, len(B) -1):
    listB.append(B[x])

counter = 0
isequal = True

for x in range(0, int(N)-1):
    if isequal == True:
        if str(listA[x]) != str(listB[x]):
            isequal = False
            counter += 1
    elif isequal == False:
        if str(listA[x]) != str(listB[x]):
            pass
        elif str(listA[x]) == str(listB[x]):
            isequal = True

print(counter)








