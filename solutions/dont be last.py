#Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, and Henrietta

dict = {
    "Bessie" : 0,
    "Elsie" : 0,
    "Daisy" : 0,
    "Gertie" : 0,
    "Annabelle" : 0,
    "Maggie" : 0,
    "Henrietta" : 0}

N = int(input())
for x in range(N):
    input_ = input().split()
    cow = input_[0]
    num = int(input_[1])
    dict[cow] += num


sortedDict = sorted(dict, key=dict.get)
min = dict[sortedDict[0]]

final_cow = 'poop'
found = False
for key in sortedDict:
    if dict[key] > min and found == False:
        final_cow = key
        final_num = dict[key]
        found = True
    elif found == True:
        if dict[key] == final_num:
            print("Tie")
            exit()

if final_cow != 'poop':
    print(final_cow)
    exit()
print("Tie")

