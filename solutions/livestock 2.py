from itertools import permutations
N =int(input())
positions = ['Sue', 'Betsy', 'Blue', 'Bella', 'Beatrice', 'Belinda', 'Buttercup', 'Bessie']
possible_lists = []

restrictions = []
for x in range(N):
    input_ = input().split()
    restrictions.append([input_[0], input_[len(input_)-1]])

for i in list(permutations(positions)):
    asdfasdf = True

    for x in restrictions:
        cow_one = i.index(x[0])
        cow_two = i.index(x[1])
        if abs(cow_one - cow_two) != 1:
            asdfasdf = False
            break

    if asdfasdf == True:
        possible_lists.append(i)

for x in min(possible_lists):
    print(x)



