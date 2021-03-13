buck1 = [int(x) for x in input().split()]
buck2 = [int(x) for x in input().split()]
milk1 = 1000
milk2 = 1000

outs = {}
def moveFrom(fromMilk, toMilk, fromBuck, toBuck, iters):
    if iters == 4:
        outs[fromMilk] = True
        return

    for i in range(len(fromBuck)):
        rem = fromBuck.pop(i)
        if fromMilk >= rem:
            toBuck.append(rem)
            fromMilk -= rem
            toMilk += rem

            moveFrom(toMilk, fromMilk, toBuck, fromBuck, iters + 1)

            toBuck.pop(len(toBuck) - 1)
            fromMilk += rem
            toMilk -= rem
        fromBuck.insert(i, rem)

moveFrom(milk1, milk2, buck1, buck2, 0)
print(len(outs))
