first_rect = input().split()
for x in range(len(first_rect)):
    first_rect[x] = int(first_rect[x])

second_rect = input().split()
for x in range(len(second_rect)):
    second_rect[x] = int(second_rect[x])

x_list = [first_rect[0], first_rect[2], second_rect[0], second_rect[2]]
y_list = [first_rect[1], first_rect[3], second_rect[1], second_rect[3]]
x_min = min(x_list)
x_max = max(x_list)
y_min = min(y_list)
y_max = max(y_list)

print(max(x_max-x_min, y_max-y_min)**2)
