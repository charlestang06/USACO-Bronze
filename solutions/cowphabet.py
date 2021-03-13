letters = list(input())
heard = list(input())

counter = 0
for index in range(len(heard)):
    if index == 0:
        counter += 1
        continue
    if letters.index(heard[index]) > letters.index(heard[index-1]):
        pass
    elif letters.index(heard[index]) <= letters.index(heard[index-1]):
        counter += 1

print(counter)
