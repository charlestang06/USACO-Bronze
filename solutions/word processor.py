N_K = input().split()
K = int(N_K[1])
words = input().split()
list = []

for x in words:
    list.append(x)

length = len(x)

current_line = ""
output = ""
current_line_length = 0
index = 0
for x in list:
    if index == 0:
        current_line = current_line + x
        current_line_length += len(x)
    elif current_line_length + len(x) <= K:
        current_line = current_line + " " + x
        current_line_length += len(x)
    else:
        output = output + current_line + "\n"
        current_line = ""
        current_line = current_line + x
        current_line_length = len(x)
    index += 1

output = output + current_line
print(output)



