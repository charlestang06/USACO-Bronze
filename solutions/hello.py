strlen=int(input())
origString = input()

for checkStrLenLimit in range(strlen-1, -1 ,-1):
    for checkStrstart in range(0, strlen - checkStrLenLimit):
        checkSubString = origString[checkStrstart:checkStrstart + checkStrLenLimit]
        if checkSubString in origString[checkStrstart+1:]:
            print(checkStrLenLimit+1)
            exit()
