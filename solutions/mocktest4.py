N = int(input())
houses = input()

for string_lengths in range(N+1, 0, -1):
    for eachstring in range(0, N - string_lengths + 1 + 1):
        if houses[eachstring:string_lengths] 
