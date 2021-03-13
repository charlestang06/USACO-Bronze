one = int(input())
two = int(input())
three = int(input())
four = int(input())
five = int(input())
six = int(input())
seven = int(input())
eight = int(input())
nine = int(input())
ten = int(input())

list = []
one = one % 42
list.append(one)

two = two % 42
if two not in list:
    list.append(two)

three = three % 42
if three not in list:
    list.append(three)

four = four % 42
if four not in list:
    list.append(four)

five = five % 42
if five not in list:
    list.append(five)

six = six % 42
if six not in list:
    list.append(six)

seven = seven % 42
if seven not in list:
    list.append(seven)

eight = eight % 42
if eight not in list:
    list.append(eight)

nine = nine % 42
if nine not in list:
    list.append(nine)

ten = ten % 42
if ten not in list:
    list.append(ten)

print(list)
count = len(list)
print(count)

