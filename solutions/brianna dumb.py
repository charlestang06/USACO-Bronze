def ifcarry(A, B):
    while A > 0 and B > 0:
        if A % 10 + B % 10 >= 10:
            return True
        else:
            A = A // 10
            B = B // 10

    return False



