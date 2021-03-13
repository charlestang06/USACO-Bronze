line = input()
line = line.rstrip()

minimum = line[::-1]

for x in range(1, len(line)-1):
    for y in range(x+1, len(line)):
        string1 = line[:x]
        string2 = line[x:y]
        string3 = line[y:]
        reverse_str = string1[::-1] + string2[::-1] + string3[::-1]
        if reverse_str < minimum:
            minimum = reverse_str

print(minimum)
