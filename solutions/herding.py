coordinates = input().split()
arrayofcoords = []
for x in coordinates:
    arrayofcoords.append(int(x))

distance1 = arrayofcoords[1] - arrayofcoords[0]
distance2 = arrayofcoords[2] - arrayofcoords[1]

if distance1 == 1 and distance2 == 1:
    minimum = 0
    maximum = 0
elif min(distance1, distance2) == 1 and max(distance1, distance2) == 2:
    minimum = 1
    maximum = 1
elif min(distance1, distance2) == 1:
    minimum = 2
    maximum = max(distance1, distance2) - 1
elif min(distance1, distance2) == 2:
    minimum = 1
    maximum = max(distance1, distance2) - 1
else:
    minimum = 2
    maximum = max(distance1, distance2) - 1

print(minimum)
print(maximum)

