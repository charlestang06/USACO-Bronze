N_K = input().split()
K = int(N_K[0])
N = int(N_K[1])

rankings = []
for x in range(K):
    input_line = input().split()
#   for y in range(0, len(input_line)):
#        input_line[y] = int(input_line[y])
    rankings.append(input_line)

consistent_pairs = 0


for first_cow in range(0, N-1): #cow number
    for second_cow in range(1, N): #compared cow number
        condition = True
        first_cow_num = rankings[0][first_cow]
        second_cow_num = rankings[0][second_cow]
        for contest in range(1, K):
            first_cow_ind = rankings[contest].index(str(first_cow_num))
            second_cow_ind = rankings[contest].index(str(second_cow_num))
            if first_cow_ind < second_cow_ind:
                continue
            else:
                condition = False
                break

        if condition == True:
            consistent_pairs += 1



print(consistent_pairs)
