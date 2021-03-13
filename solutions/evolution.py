N = int(input())

sub_populations = []

for x in range(N):
    input_ = input().split()
    if len(input_) == 1:
        sub_populations.append([])
    else:
        sub_populations.append(input_[1:])

for i in range(0, len(sub_populations)-1):
    cow1 = set(sub_populations[i])
    for j in range(i+1, len(sub_populations)):
        cow2 = set(sub_populations[j])

        if len(cow1) > 0 and len(cow2) > 0 and (cow1.issubset(cow2) or cow2.issubset(cow1)):
            if len(cow1) > len(cow2):
                diff_characteristics = cow1.difference(cow2)
            else:
                diff_characteristics = cow2.difference(cow1)
            for characteristic in diff_characteristics:
                for cow_index in range(0, len(sub_populations)):
                    if cow_index != i and cow_index != j and characteristic in sub_populations[cow_index] and not set(sub_populations[cow_index]).issuperset(cow1) and not set(sub_populations[cow_index]).issuperset(cow2):
                        print("no")
                        exit()


print("yes")
