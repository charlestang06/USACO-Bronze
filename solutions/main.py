x = input().split()

N = int(x[0])
K = int(x[1])
add = 2
integers = []
for y in range(int(x[0])-1):
    integers.append(add)
    add += 1

counter = 0
for a in range(len(integers)):
    first = integers[0]
    for z in integers:
        print(integers)
        if int(z) % int(first) == 0:
            integers.remove(z)
            counter += 1
            if counter == int(K):
                print(z)
                exit()










