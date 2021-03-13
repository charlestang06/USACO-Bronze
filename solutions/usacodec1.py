numbers = input().split()

for x in range(len(numbers)):
    numbers[x] = int(numbers[x])



for a in range(0, len(numbers)-2):
    for b in range(a+1, len(numbers)-1):
        for c in range(b+1, len(numbers)):
            A = numbers[a]
            B = numbers[b]
            C = numbers[c]
            if (A+B) in numbers and (A+C) in numbers and (B+C) in numbers and (A+B+C) in numbers:
                numbers_ = [A, B, C]
                numbers_.sort()
                print(f"{numbers_[0]}, {numbers_[1]}, {numbers[2]}")
                exit()




