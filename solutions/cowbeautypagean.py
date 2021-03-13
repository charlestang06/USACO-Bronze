import sys
N_M = input().split()
num_rows = int(N_M[0])
num_columns = int(N_M[1])

array = []

for x in range(num_rows):
    input_ = list(input())
    array.append(input_)

def label(row, column, num):
    num = str(num)
    array[row][column] = num
    if row-1 >= 0 and array[row-1][column]=='X': #above
        label(row-1, column, num)
    if column+1<num_columns and array[row][column+1] == 'X': #right
        label(row, column+1, num)
    if row+1 < num_rows and array[row+1][column] == 'X': #bottom
        label(row+1, column, num)
    if column-1>=0 and array[row][column-1]=='X': #left
        label(row, column-1, num)
    if column+1<num_columns and array[row][column+1] == 'X': #right
        label(row, column+1, num)


counter = 1
sys.setrecursionlimit(234234)
for i in range(num_rows):
    for j in range(num_columns):
        if array[i][j] == 'X':
            label(i, j, counter)
            counter +=1

for x in range(num_rows):
    string = ''.join(array[x])
    print(string)

min_distance = num_columns + num_rows
for i in range(num_rows):
    for j in range(num_columns):
        if array[i][j] == '1':
            for a in range(num_rows):
                for b in range(num_columns):
                    if array[a][b] == '2':
                        min_distance = min(min_distance, abs(a-i)+abs(b-j)-1)

print(min_distance)


