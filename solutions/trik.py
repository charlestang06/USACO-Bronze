chars = input()
chars_list = []
for x in chars:
    chars_list.append(x)

ball_position = [True, False, False]

for x in chars_list:
    if x == 'A':
        placeholder = ball_position[0]
        ball_position[0] = ball_position[1]
        ball_position[1] = placeholder
    elif x == 'B':
        placeholder = ball_position[1]
        ball_position[1] = ball_position[2]
        ball_position[2] = placeholder
    else:
        placeholder = ball_position[0]
        ball_position[0] = ball_position[2]
        ball_position[2] = placeholder

print(ball_position.index(True) + 1)