input = input()

inputlist = []

topstring = []
secondstring = []
middlestring = []
fourstring = []
laststring = []

for x in input:
    inputlist.append(x)
    counter = 0

print(inputlist)

for x in range(1, len(inputlist)+1):
    if (counter + 1) % 3 == 0:
            topstring.append(".*.")
            secondstring.append(".*.*.")
            middlestring.append(f"*.{inputlist[counter]}.*")
            fourstring.append(".*.*.")
            laststring.append("..*..")
    elif (counter + 1) % 3 == 1:
            topstring.append("..#..")
            secondstring.append(".#.#.")
            middlestring.append(f"#.{inputlist[counter]}.#")
            fourstring.append("#.#.")
            laststring.append(".#..")
    elif (counter+1) % 3 == 2:
            topstring.append(".#..")
            secondstring.append(".#.#.")
            middlestring.append(f"#.{inputlist[counter]}.")
            fourstring.append(".#.#")
            laststring.append("..#.")
    counter += 1

string = ""
for x in topstring:
    string = string + x
print(topstring)
print(string)

string = ""
for x in secondstring:
    string = string + x
print(secondstring)
print(string)

string = ""
for x in middlestring:
    string = string + x
print(middlestring)
print(string)

string = ""
for x in fourstring:
    string = string + x
print(fourstring)
print(string)

string = ""
for x in laststring:
    string = string + x
print(laststring)




