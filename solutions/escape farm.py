from itertools import combinations
num_cows = int(input())
cow_weights = []

for x in range(num_cows):
    cow_weights.append(int(input()))

def ifcarry(A, B):
    while A > 0 and B > 0:
        if A % 10 + B % 10 >= 10:
            return True
        else:
            A = A // 10
            B = B // 10
    return False

counter = 0
for x in range(num_cows, 1, -1):
    comb = combinations(cow_weights, x)
    for element in list(comb): #each combination
        sum = 0
        carry = False
        for weight in element: #each weight in combination5
            carry = ifcarry(sum, weight)
            if carry == True:
                break
            else:
                sum += weight
        if carry == False:
            print(x)
            exit()








