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
if num_evens == 0:
    print(x)
    exit()

if num_evens == num_odds or num_evens == num_odds + 1:
    print(num_cows)
elif num_odds == num_evens+1:
    print(num_cows-2)
else:
    print(num_cows-1)