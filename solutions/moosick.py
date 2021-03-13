N = int(input())
notes = []
for x in range(N):
    notes.append(int(input()))

chord = []
C = int(input())
for x in range(C):
    chord.append(int(input()))
chord.sort()

counter = 0
indices = []
chord_bool = False
for x in range(N-C+1):
    #take three, sort, check if chord, then plug in index (+1)
    temp_notes = [notes[x+n] for n in range(C)]
    temp_notes.sort()
    for y in range(0, C-1):
        if temp_notes[y+1] - temp_notes[y] == chord[y+1] - chord[y]:
            pass
        else:
            chord_bool = False
            break
        chord_bool = True
    if chord_bool == True or C==1:
        indices.append(x+1)
        counter += 1

print(counter)
for x in indices:
    print(x)




