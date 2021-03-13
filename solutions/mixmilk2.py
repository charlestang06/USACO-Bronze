c1,m1 = map(int, input().split())
c2,m2 = map(int, input().split())
c3,m3 = map(int,input().split())

capacities = [c1, c2, c3]
milk = [m1, m2, m3]

for x in range(100):
    if x % 3 == 0: #1 to 2
        if milk[0] + milk[1] > capacities[1]:
            milk[0] -= capacities[1] - milk[1]
            milk[1] = capacities[1]
        else:
            milk[1] += milk[0]
            milk[0] = 0
    elif x % 3 == 1: #2 to 3
        if milk[1] + milk[2] > capacities[2]:
            milk[1] -= capacities[2] - milk[2]
            milk[2] = capacities[2]
        else:
            milk[2] += milk[1]
            milk[1] = 0
    elif x % 3 == 2: #3 to 4
        if milk[2] + milk[0] > capacities[0]:
            milk[2] -= capacities[0] - milk[0]
            milk[0] = capacities[0]
        else:
            milk[0] += milk[2]
            milk[2] = 0


for x in milk:
    print(x)