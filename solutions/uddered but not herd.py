cowphabet = list(input())
string = list(input())

counter = 0
for x in range(len(string)):
    if x == 0:
        counter += 1
    else:
        if cowphabet.index(string[x]) <= cowphabet.index(string[x-1]):
            counter += 1
        else:
            continue

print(counter)