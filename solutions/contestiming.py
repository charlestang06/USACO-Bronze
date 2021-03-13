#1 convert minutes then minutes, base November 11
# outer loop base 2, inner loop base 3
#sort
D_H_M = input().split()
D = (int(D_H_M[0]) - 11)*60*24
H = int(D_H_M[1])*60
M = int(D_H_M[2])

Start = 671 #11:11
Taken_min = D + H + M
if Start > Taken_min:
    print(-1)
else:
    print(abs(Start-Taken_min))
