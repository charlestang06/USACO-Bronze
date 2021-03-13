list = []

for x in range(10):
    number = int(input())
    remainder = number % 42
    if remainder not in list:
        list.append(remainder)

print(len(list))



