num_cows = int(input())

cow_ids = input().split()

for x in range(len(cow_ids)):
    cow_ids[x] = int(cow_ids[x])

def numEvens(list):
    counter = 0
    for number in list:
        if number % 2 == 0:
            counter += 1
    return counter


def numOdds(list):
    counter = 0
    for number in list:
        if number % 2 == 1:
            counter += 1
    return counter

num_evens = numEvens(cow_ids)
num_odds = numOdds(cow_ids)

if num_odds == 0:
    print(1)
    exit()

if num_evens == num_odds:
    print(num_cows)
    exit()

groups = 0

isEven = True
for x in range(num_cows):
    if isEven == True:
        if num_evens >= 1:
            num_evens -= 1
            groups += 1
            isEven = False
        elif num_odds >= 2:
            num_odds -= 2
            groups += 1
            isEven = False
        else:
            if num_odds == 1:
                print(groups)
                exit()
    else:
        if num_odds == 2 and num_evens == 0:
            print(groups)
            exit()
        if num_odds == 1 and num_evens == 0:
            print(groups-2)
            exit()
        if num_odds >= 1:
            num_odds -= 1
            groups += 1
            isEven = True

print(groups)


