characters = []
input_line = input()
for x in input_line:
    characters.append(x)

characters.append('Z')

counter = len(characters) - 1

for x in range(0, len(characters)-1):
    if characters[x] == 'c' and characters[x+1] == '=':
        counter -= 1
    elif characters[x] == 'c' and characters[x+1] == '-':
        counter -= 1
    elif characters[x] == 'd' and characters[x+1] == 'z' and characters[x+2] == '=':
        counter -= 1
    elif characters[x] == 'd' and characters[x+1] == '-':
        counter -= 1
    elif characters[x] == 'l' and characters[x+1] == 'j':
        counter -= 1
    elif characters[x] == 'n' and characters[x+1] == 'j':
        counter -= 1
    elif characters[x] == 's' and characters[x+1] == '=':
        counter -= 1
    elif characters[x] == 'z' and characters[x+1] == '=':
        counter -= 1

print(counter)