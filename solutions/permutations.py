input = list(input())

def toString(List):
    return ''.join(List)


def permutation(List, f, l):
    if f == l:
        print(toString(List))
    else:
        for x in range(f, l+1):
            List[f], List[x] = List[x], List[f]
            permutation(List, f+1, l)
            List[f], List[x] = List[x], List[f]

permutation(input, 0, len(input)-1)
