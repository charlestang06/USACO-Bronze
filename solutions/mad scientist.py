N = int(input())
string = list(input())
final = list(input())

counter = 0
first_index = 0
last_index = 0

for x in range(N-1):
    if string[x] != final[x] and x > first_index:
        last_index = x
        if string[x+1] != final[x+1]:
            continue
        else:
            for y in range(first_index, last_index+1):
                if string[y] == 'H': string[x] = 'G'
                else: string[y] = 'H'
            counter += 1
        first_index = 0
    elif string[x] != final[x] and first_index==0:
        first_index = x
        if string[x+1] == final[x+1]:
            for y in range(first_index, last_index+1):
                if string[y] == 'H': string[x] = 'G'
                else: string[y] = 'H'
            counter += 1
        continue
    else:
        first_index = 0

print(counter)