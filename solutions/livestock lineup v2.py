import itertools
N = int(input())
pairs = []
for x in range(N):
    input_ = input().split()
    pairs.append([input_[0], input_[len(input_)-1]])

random = ['Beatrice', 'Sue', 'Belinda', 'Bessie', 'Betsy', 'Blue', 'Bella', 'Buttercup']
perm = list(itertools.permutations(random))
possible_list = []

for x in range(len(perm)):
    possible = True
    temp = perm[x]
    for y in range(len(pairs)):
        pair = pairs[y]
        first = pair[0]
        second = pair[1]
        if temp.index(first) + 1 == temp.index(second) or temp.index(first) - 1 == temp.index(second):
            continue
        else:
            possible = False
            break
    if possible == True:
        possible_list.append(temp)

minimum = min(possible_list)
for x in minimum:
    print(x)