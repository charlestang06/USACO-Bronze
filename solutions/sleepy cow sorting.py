N = int(input())
cows = list(map(int, input().split()))


def sort_cows(arr, counter):
    if arr == sorted(arr):
        return counter
    else:
        first = arr[0]
        for x in range(1, N):
            if arr[x] < first:
                arr.insert(x+1,first)
                counter += 1
                sort_cows(arr, counter)

print(sort_cows(cows, 0))