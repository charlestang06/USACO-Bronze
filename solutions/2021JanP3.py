N = int(input())
cow_heights = input().split()
stall_heights = input().split()
final = [False for x in range(N)]

cow_heights.sort()
stall_heights.sort()

product = 1

for cow_index in range(len(cow_heights)-1, -1, -1):
    counter = 0
    cow = cow_heights[cow_index]
    for stall_index in range(len(stall_heights)-1, -1, -1):
        stall = stall_heights[stall_index]
        if cow <= stall and final[stall_index] == False:
            counter += 1
    product *= counter
    final[cow_index] = True

print(product)

