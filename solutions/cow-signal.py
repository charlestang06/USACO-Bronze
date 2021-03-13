M,N,K = map(int, input().split())

final = ['' for x in range(M)]

for x in range(0, M):
    input_ = list(input())
    for y in input_:
        for z in range(K):
            final[x] += y

new_final = []
for element in final:
    for i in range(K):
        new_final.append(element)


for element in new_final:
    print(element)