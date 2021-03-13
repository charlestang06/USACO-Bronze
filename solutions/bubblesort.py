N = int(input())
order1 = []
order2 = []
order3 = []
order4 = []
order5 = []

for x in range(N):
    order1.append(int(input()))
for x in range(N):
    order2.append(int(input()))
for x in range(N):
    order3.append(int(input()))
for x in range(N):
    order4.append(int(input()))
for x in range(N):
    order5.append(int(input()))


def compare(A, B):
    counter = 0
    indexA1 = 0; indexB1 = 0; indexA2 = 0; indexB2 = 0; indexA3 = 0; indexB3 = 0; indexA4= 0; indexB4 = 0; indexA5 = 0; indexB5 = 0;
    for x in range(len(order1)):
        if order1[x] == A:
            indexA1 = x
        if order1[x] == B:
            indexB1 = x
    for x in range(len(order1)):
        if order2[x] == A:
            indexA2 = x
        if order2[x] == B:
            indexB2 = x
    for x in range(len(order1)):
        if order3[x] == A:
            indexA3 = x
        if order3[x] == B:
            indexB3 = x
    for x in range(len(order1)):
        if order4[x] == A:
            indexA4 = x
        if order4[x] == B:
            indexB4 = x
    for x in range(len(order1)):
        if order5[x] == A:
            indexA5 = x
        if order5[x] == B:
            indexB5 = x

    if indexA1 < indexB1:
        counter += 1
    if indexA2 < indexB2:
        counter += 1
    if indexA3 < indexB3:
        counter += 1
    if indexA4 < indexB4:
        counter += 1
    if indexA5 < indexB5:
        counter += 1
    return(counter >= 3)

final = order1


for x in range(len(order1)-1):
    for y in range(x+1, len(order1)):
        if compare(final[x], final[y]) == False:
            temp = final[y]
            final[y] = final[x]
            final[x] = temp

print(final)


