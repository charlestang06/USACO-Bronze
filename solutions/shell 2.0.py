N = int(input())
case_1 = [True, False, False]
count_1 = 0
case_2 = [False, True, False]
count_2 = 0
case_3 = [False, False, True]
count_3 = 0

for x in range(N):
    input_ = list(map(int, input().split()))

    a = input_[0] - 1
    b = input_[1] - 1
    g = input_[2] - 1

    #case 1
    temp = case_1[a]
    case_1[a] = case_1[b]
    case_1[b] = temp
    if case_1[g] == True:
        count_1 += 1

    #case 2
    temp = case_2[a]
    case_2[a] = case_2[b]
    case_2[b] = temp
    if case_2[g] == True:
        count_2 += 1

    #case 3
    temp = case_3[a]
    case_3[a] = case_3[b]
    case_3[b] = temp
    if case_3[g] == True:
        count_3 += 1

print(max(count_1, count_2, count_3))