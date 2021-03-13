num_cows = int(input())

cow_ids = input().split()

for x in range(len(cow_ids)):
    cow_ids[x] = int(cow_ids[x])

final_list = []

isOdd = False
areEvens = False

for cow in cow_ids:
    if isOdd == False:
        for cow in cow_ids:
            if cow % 2 == 0:
                final_list.append(cow)
                cow_ids.remove(cow)
                isOdd = True
                areEvens = True
                break
        if areEvens == False:
            final_list.append(cow_ids[0] + cow_ids[1])
            cow_ids.pop(0)
            cow_ids.pop(0)
    elif isOdd == True:
        for cows in cow_ids:
            if cow % 2 == 1:
                final_list.append(cow)
                cow_ids.remove(cow)
                isOdd = False


print(len(final_list))





