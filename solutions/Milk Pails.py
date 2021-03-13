X,Y,M = map(int, input().split())
high = 0

for x in range(M//X):
    sum = 0
    sum += X*x
    while sum+Y <= M:
        sum += Y
    high = max(high, sum)

print(high)
