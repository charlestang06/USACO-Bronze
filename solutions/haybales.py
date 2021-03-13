num_piles = int(input())

hay_array = []
sum = 0
for x in range(num_piles):
    hay_array.append(int(input()))


for element in hay_array:
    sum += element


average = sum / num_piles
total_diff = 0

for element in hay_array:
    if element > average:
        total_diff += element - average

print(int(total_diff))


