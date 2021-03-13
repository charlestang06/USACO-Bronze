# outer loop base 2, inner loop base 3

base_2_N = input()
base_3_N = input()

def convert(n):
    n = int(n)
    base_3 = []
    if n < 3:
        return str(n)
    while n // 3 > 0:
        base_3.append(str(n%3))
        n //= 3
    base_3.append(str(n))
    base_3 = base_3[::-1]
    number = ''.join(base_3)
    return number


for x in range(len(base_2_N)):
    temp_base_2_N = []
    for z in range(len(base_2_N)): #list
        temp_base_2_N.append(base_2_N[z])
    if base_2_N[x] == '1':
        temp_base_2_N[x] = '0'
    else:
        temp_base_2_N[x] = '1'
    temp_base_2_N = ''.join(temp_base_2_N)
    N = str(int(temp_base_2_N, 2))
    N = convert(N)
    counter = 0

    if len(base_3_N) == len(N)+1:
        N = '0' + N
    elif abs(len(base_3_N)-len(N)) >= 2:
        continue
    elif len(base_3_N)+1 == len(N):
        continue

    for y in range(len(N)):
        if base_3_N[y] == N[y]:
            continue
        else:
            counter += 1
    if counter == 1:
        print(int(N, 3))
        exit()



