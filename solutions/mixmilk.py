capacity = []
current_amount = []
for x in range(0, 3):
    inputnumber = input().split()
    capacity.append(int(inputnumber[0]))
    current_amount.append(int(inputnumber[1]))

for x in range(0, 100):
    if (current_amount[x%3] + current_amount[(x+1) % 3]) <= capacity[(x+1)%3]:
        current_amount[(x+1) % 3] += current_amount[x % 3]
        current_amount[x % 3] = 0
    else:
        space = capacity[(x+1) % 3] - current_amount[(x+1) % 3]
        current_amount[(x + 1) % 3] = capacity[(x+1) % 3]
        current_amount[x % 3] -= space

for x in current_amount:
    print(x)
