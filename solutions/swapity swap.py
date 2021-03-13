N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])

A_range = input().split()
Astart = int(A_range[0])
Aend = int(A_range[1])

B_range = input().split()
Bstart = int(B_range[0])
Bend = int(B_range[1])

numbers = []
for x in range(0, N):
    numbers.append(x+1)


first_numbers = numbers
counter = 0
for x in range(100000):
    #Aflip
    numbers = numbers[:Astart-1] + numbers[Astart-1:Aend][::-1] + numbers[Aend:]
    #Bflip
    numbers = numbers[:Bstart-1] + numbers[Bstart-1:Bend][::-1] + numbers[Bend:]
    counter += 1
    if numbers == first_numbers:
        break

times = K % counter
numbers = first_numbers

for x in range(times):
    #Aflip
    numbers = numbers[:Astart-1] + numbers[Astart-1:Aend][::-1] + numbers[Aend:]
    #Bflip
    numbers = numbers[:Bstart-1] + numbers[Bstart-1:Bend][::-1] + numbers[Bend:]
    counter += 1

for x in numbers:
    print(x)