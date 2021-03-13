bill_board = list(map(int, input().split()))
tarp = list(map(int, input().split()))


xOverlap = max(min(bill_board[2], tarp[2]) - max(bill_board[0], tarp[0]), 0)
yOverlap = max(min(bill_board[3], tarp[3]) - max(bill_board[1], tarp[1]), 0)

if xOverlap == 0 or yOverlap == 0:
    print((bill_board[2] - bill_board[0]) * (bill_board[3] - bill_board[1]))
    exit()
if xOverlap >= bill_board[2] - bill_board[0] and yOverlap >= bill_board[3] - bill_board[1]:
    print(0)
    exit()

if xOverlap < bill_board[2] - bill_board[0] and yOverlap < bill_board[3] - bill_board[1]:
    print((bill_board[2] - bill_board[0])*(bill_board[3]-bill_board[1]))
elif xOverlap >= bill_board[2] - bill_board[0] and yOverlap < bill_board[3] - bill_board[1]:
    print(xOverlap*(bill_board[3]-bill_board[1] - yOverlap))
elif yOverlap >= bill_board[3] - bill_board[1] and xOverlap < bill_board[2] - bill_board[0]:
    print(yOverlap*(bill_board[2] - bill_board[0] - xOverlap))
else:
    print((bill_board[2] - bill_board[0]) * (bill_board[3] - bill_board[1]))