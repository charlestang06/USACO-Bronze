N_L = input().split()
Number_lights = int(N_L[0])
Length = int(N_L[1])

time = 0
last_distance = 0

for x in range(Number_lights):
    information = input().split()
    time += int(information[0]) - last_distance
    remainder = time % (int(information[1]) + int(information[2]))
    if remainder < int(information[1]):
        time += int(information[1]) - remainder
    last_distance = int(information[0])

time += Length - last_distance

print(time)