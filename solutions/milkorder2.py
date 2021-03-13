N_K = input().split()
numberOfCows = int(N_K[0])
numerOfCowsInSeq = int(N_K[1])
numberOfDemandings = int(N_K[2])
sequence = input().split()
cowsorders = []

# initialize cow order list with all 0
for i in range(0, numberOfCows):
    cowsorders.append(0)

# Process demanding cows into order list
for x in range(0, numberOfDemandings):
    cowIndex_order = input().split()
    cowsorders[int(cowIndex_order[1]) - 1] = int(cowIndex_order[0])

availableSpot = len(cowsorders) - 1
for index in range(len(sequence) - 1, -1, -1):
    inserted = False
    for x in range(0, availableSpot):
        if cowsorders[x] == int(sequence[index]):
            inserted = True
            availableSpot = x - 1
            break;
    if not inserted:
        while cowsorders[availableSpot] != 0:  # this spot is not available
            availableSpot -= 1
        cowsorders[availableSpot] = int(sequence[index])  # insert into available rightmost spot
        availableSpot -= 1

cow1position = 0
for x in range(0, len(cowsorders)):
    if cowsorders[x] == 1:
        cow1position = x
        break
if cow1position == 0:
    for x in range(0, len(cowsorders)):
        if cowsorders[x] == 0:
            cow1position = x
            break

print(cow1position+1)