N = int(input())
gear_sizes = input().split()
for x in range(0, len(gear_sizes)):
    gear_sizes[x] = int(gear_sizes[x])


for x in range(1, len(gear_sizes)):
    numerator = gear_sizes[0]
    denominator = gear_sizes[x]
    #GCF
    smaller = min(numerator, denominator)
    for y in range(int(smaller), 1, -1):
        if numerator % y  == denominator % y == 0:
            numerator = int(numerator / y)
            denominator = int(denominator / y)
            break

    print(str(int(numerator)) + "/" + str(int(denominator)))