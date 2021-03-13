import math

number_cows = int(input())
cow_x = []
cow_y = []
index_array = [int(i) for i in range(1, number_cows+1)]

for x in range(number_cows):
    input_line = input().split()
    cow_x.append(int(input_line[0]))
    cow_y.append(int(input_line[1]))

min_distance = 1000000
temp_index = 0

for x in range(0, len(index_array)-1):
    if len(index_array) > 1:
        for test_cow in range(0, len(index_array)-1):
            if test_cow == x:
                pass
            else:
                temp_distance = math.sqrt((cow_y[x] - cow_y[test_cow]) * (cow_y[x] - cow_y[test_cow]) + ((cow_x[x] - cow_x[test_cow]) * (cow_x[x] - cow_x[test_cow])))
                if temp_distance < min_distance:
                    min_distance = temp_distance
                    temp_index = test_cow

    cow_x.pop(temp_index - 1)
    cow_y.pop(temp_index - 1)
    index_array.pop(temp_index - 1)

print(index_array[0])

