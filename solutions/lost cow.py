x,y = map(int, input().split())

old_position = x
position = x

counter = 1
total_dist = 0

for z in range(100):
    if z%2 == 0:
        position = x + counter
        total_dist += abs(position - old_position)
        counter *= 2
        old_position = position
        if position >= y and y >= x:
            print(total_dist - (position-y))
            exit()
    if z%2 == 1:
        position = x - counter
        total_dist += abs(position - old_position)
        counter *= 2
        old_position = position
        if position <= y and y <= x:
            print(total_dist - abs(position-y))
            exit()




