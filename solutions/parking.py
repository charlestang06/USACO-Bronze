A_B_C = input().split()
price_one = int(A_B_C[0])
price_two = int(A_B_C[1])
price_three = int(A_B_C[2])

car_one = [False] * 100
car_two = [False] * 100
car_three = [False] * 100

for x in range(1, 4):
    input_line = input().split()
    start = int(input_line[0])
    end = int(input_line[1])
    for index in range(start, end):
        if x == 1:
            car_one[index] = True
        elif x == 2:
            car_two[index] = True
        else:
            car_three[index] = True

cost = 0

for x in range(0, 100):
    if car_one[x] == True and car_two[x] == car_three[x] == False:
        cost += price_one
    elif car_two[x] == True and car_one[x] == car_three[x] == False:
        cost += price_one
    elif car_three[x] == True and car_one[x] == car_two[x] == False:
        cost += price_one
    elif car_one[x] == car_two[x] == True and car_three[x] == False:
        cost += 2 * price_two
    elif car_two[x] == car_three[x] == True and car_one[x] == False:
        cost += 2 * price_two
    elif car_one[x] == car_three[x] == True and car_two[x] == False:
        cost += 2 * price_two
    elif car_one[x] == car_two[x] == car_three[x] == False:
        cost = cost
    elif car_one[x] == car_two[x] == car_three[x] == True:
        cost += 3 * price_three

print(cost)