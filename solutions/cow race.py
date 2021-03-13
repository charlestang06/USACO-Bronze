Bposition = []
Eposition = []

N,M = map(int, input().split())
bRun =[]
eRun = []

for x in range(N):
    input_ = list(map(int, input().split()))
    bRun.append(input_)
for x in range(M):
    input_ = list(map(int, input().split()))
    eRun.append(input_)


total = 0
for x in range(N):
    speed = bRun[x][0]
    time = bRun[x][1]
    for y in range(time):
        total += speed
        Bposition.append(total)
total = 0
for x in range(M):
    speed = eRun[x][0]
    time = eRun[x][1]
    for y in range(time):
        total += speed
        Eposition.append(total)



counter = 0
eGreater = True
bGreater = True
for x in range(len(Bposition)):
    if x == 0:
        if Bposition[x] > Eposition[x]:
            bGreater = True
            eGreater = False
        elif Eposition[x]>Bposition[x]:
            bGreater = False
            eGreater = True
    else:
        if Bposition[x] > Eposition[x] and bGreater == False and eGreater == True:
            counter += 1
            bGreater = True
            eGreater = False
        elif Eposition[x] > Bposition[x] and bGreater == True and eGreater == False:
            counter += 1
            bGreater = False
            eGreater = True

print(counter)