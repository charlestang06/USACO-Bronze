input = input()
input.split()

stringtop = []
stringsecond = []
stringmiddle = []
stringfourth = []
stringbottom = []

counter = 0
if len(input) == 1:
    stringtop.append("..#..")
    stringsecond.append(".#.#.")
    stringmiddle.append(f"#.{input[counter]}.#")
    stringfourth.append(".#.#.")
    stringbottom.append("..#..")
    string = ""
    for x in stringtop:
        string += x
    print(string)

    string = ""
    for x in stringsecond:
        string += x
    print(string)

    string = ""
    for x in stringmiddle:
        string += x
    print(string)

    string = ""
    for x in stringfourth:
        string += x
    print(string)

    string = ""
    for x in stringbottom:
        string += x
    print(string)
    exit()

for x in range(1, len(input)+1):
    if counter == 0:
        stringtop.append("..#.")
        stringsecond.append(".#.#")
        stringmiddle.append(f"#.{input[counter]}.")
        stringfourth.append(".#.#")
        stringbottom.append("..#.")

    elif counter == len(input) - 1:
        if (counter+1) % 3 == 0:
            stringtop.append("..*..")
            stringsecond.append("*.*.")
            stringmiddle.append(f"*.{input[counter]}.*")
            stringfourth.append(".*.*.")
            stringbottom.append("..*..")
        elif (counter+1) % 3 == 1:
            stringtop.append(".#..")
            stringsecond.append(".#.#.")
            stringmiddle.append(f".{input[counter]}.#")
            stringfourth.append("#.#.")
            stringbottom.append(".#..")
        else:
            stringtop.append("..#..")
            stringsecond.append(".#.#.")
            stringmiddle.append(f"#.{input[counter]}.#")
            stringfourth.append(".#.#.")
            stringbottom.append("..#..")
    elif (counter+1) % 3 == 0:
        stringtop.append("..*..")
        stringsecond.append("*.*")
        stringmiddle.append(f"*.{input[counter]}.*")
        stringfourth.append(".*.*.")
        stringbottom.append("..*..")
    elif (counter+1) % 3 == 2:
        stringtop.append("..#.")
        stringsecond.append(".#.#.")
        stringmiddle.append(f"#.{input[counter]}.")
        stringfourth.append(".#.#")
        stringbottom.append("..#.")
    elif (counter+1) % 3 == 1:
        stringtop.append(".#.")
        stringsecond.append(".#.#")
        stringmiddle.append(f".{input[counter]}.")
        stringfourth.append("#.#")
        stringbottom.append(".#.")
    counter += 1

string = ""
for x in stringtop:
    string += x
print(string)

string = ""
for x in stringsecond:
    string += x
print(string)

string = ""
for x in stringmiddle:
    string += x
print(string)

string = ""
for x in stringfourth:
    string += x
print(string)

string = ""
for x in stringbottom:
    string += x
print(string)
