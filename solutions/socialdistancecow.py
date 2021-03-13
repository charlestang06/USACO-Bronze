N = int(input())
cows = input()
cowlist = list(cows)

min_gap = N
second_max_gap = 0
max_gap = 0
counter = 0
last_cow_counter = 0

for x in cowlist:
    if x == '1':
        current_gap = counter - last_cow_counter
        last_cow_counter = counter
        if current_gap != 0:
            min_gap = min(min_gap, current_gap)
        if current_gap > max_gap:
            second_max_gap = max_gap
            max_gap = current_gap
        elif current_gap > second_max_gap:
            second_max_gap = current_gap
    counter += 1

counter -= 1
current_gap = counter - last_cow_counter
min_gap = min(min_gap, current_gap)
if current_gap > max_gap:
    second_max_gap = max_gap
    max_gap = current_gap
elif current_gap > second_max_gap:
    second_max_gap = current_gap

print(min_gap)
print(second_max_gap)
print(max_gap)
print(last_cow_counter)

if max_gap == 0:
    minimum_gap = N - 1
elif second_max_gap == 0:
    minimum_gap = max_gap//3
elif max_gap // 3 >= second_max_gap // 2:
    minimum_gap = min(max_gap//3, min_gap)
else:
    minimum_gap = min(max_gap//2, second_max_gap //2, min_gap)

print(minimum_gap)