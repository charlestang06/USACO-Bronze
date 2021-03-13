N = int(input())
indexes = list(map(int, input().split()))
final = [0 for x in range(N)]
id = input().split()

for x in range(N):
    final[indexes[x]-1] = id[x]

for x in final:
    print(x)