row_index = 1
column_index = 1
Bcolumn = 0
Brow = 0
Rcolumn = 0
Rrow = 0
Lcolumn = 0
Lrow = 0

for x in range(0, 10):
    line = input()
    linelist = list(line)
    for x in linelist:
        if x == "B":
            Bcolumn = column_index
            Brow = row_index
            column_index += 1
        elif x == "R":
            Rcolumn = column_index
            Rrow = row_index
            column_index += 1
        elif x == "L":
            Lcolumn = column_index
            Lrow = row_index
            column_index += 1
        else:
            column_index += 1
    column_index = 1
    row_index += 1

print(Bcolumn)
print(Brow)
print(Rcolumn)
print(Rrow)
print(Lcolumn)
print(Lrow)

if ((Bcolumn == Rcolumn == Lcolumn) and ((Brow < Rrow < Lrow) or (Brow > Rrow > Lrow))) or ((Brow == Rrow == Lrow) and ((Bcolumn < Rcolumn < Lcolumn) or (Bcolumn > Rcolumn > Lcolumn))):
    distance = abs(Bcolumn - Lcolumn) + abs(Brow-Lrow) + 1
    print(distance)
else:
    distance = abs(Bcolumn - Lcolumn) + abs(Brow-Lrow) - 1
    print(distance)