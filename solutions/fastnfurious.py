K_N = input().split()
length_race = int(K_N[0])
N = int(K_N[1])
max_speeds = []
final_times = []

for x in range(N):
    input_ = input()
    max_speeds.append(int(input_))

final_times = []

for max_speed in range(0, len(max_speeds)):
    time_counter = 0
    distance_traveled = 0
    speed = 1
    while distance_traveled < length_race:
        distance_traveled += speed
        time_counter += 1
        if distance_traveled < length_race and speed >= max_speeds[max_speed]:
            distance_traveled += speed
            time_counter += 1
        elif speed < max_speeds[max_speed]:
            pass
        else:
            break
        speed += 1

    final_times.append(time_counter)

for x in final_times:
    print(x)


