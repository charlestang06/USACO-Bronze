N_C = input().split()
N = int(N_C[0])
C = int(N_C[1])
nums = input().split()
for x in range(0, len(nums)):
    nums[x] = int(nums[x])

nums_dict = {}

for element in nums:
    if element not in nums_dict:
        nums_dict[element] = 1
    else:
        nums_dict[element] += 1

output = ""
for w in sorted(nums_dict, key=nums_dict.get, reverse=True):
    for x in range(nums_dict[w]):
        output = output + str(w) + " "

print(output)