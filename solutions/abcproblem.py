numbers = input().split()
abc = input()

for x in range(0, 3):
    numbers[x] = int(numbers[x])

numbers.sort()
# print(numbers)

output = ""

for x in range(0, 3):
    if abc[x] == 'A':
        output =  output + str(numbers[0]) + " "
    if abc[x] == 'B':
        output = output + str(numbers[1]) + " "
    if abc[x] == 'C':
        output = output + str(numbers[2]) + " "

print(output)