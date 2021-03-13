input_1 = input().split()
input_2 = input().split()


dog_data = []
people_data = []
for x in input_1:
    dog_data.append(int(x))

for x in input_2:
    people_data.append(int(x))

dog1totalcycle = int(dog_data[0]) + int(dog_data[1]) #total cycle
dog2totalcycle = int(dog_data[2]) + int(dog_data[3])

postmandog1 = int(people_data[0]) % dog1totalcycle
postmandog2 = int(people_data[0]) % dog2totalcycle
M1 = int(people_data[1]) % dog1totalcycle
M2 = int(people_data[1]) % dog2totalcycle
G1 = int(people_data[2]) % dog1totalcycle
G2 = int(people_data[2]) % dog2totalcycle

Pbark = []
if postmandog1 == 0 or postmandog1 > int(dog_data[0]):
    Pbark.append(False)
elif postmandog1 <= dog_data[0]:
    Pbark.append(True)

if postmandog2 == 0 or postmandog2 > int(dog_data[2]):
    Pbark.append(False)
elif postmandog2 <= dog_data[2]:
    Pbark.append(True)

Mbark = []
if M1 == 0 or M1 > dog_data[0]:
    Mbark.append(False)
elif M1 <= dog_data[0]:
    Mbark.append(True)

if M2 == 0 or M2 > dog_data[2]:
    Mbark.append(False)
elif M2 <= dog_data[2]:
    Mbark.append(True)

Gbark = []
if G1 == 0 or G1 > dog_data[0]:
    Gbark.append(False)
elif G1 <= dog_data[0]:
    Gbark.append(True)

if G2 == 0 or G2 > dog_data[2]:
    Gbark.append(False)
elif G2 <= dog_data[2]:
    Gbark.append(True)

if Pbark[0] == True and Pbark[1] == True:
    print("both")
elif Pbark[0] == False and Pbark[1] == True:
    print("one")
elif Pbark[0] == True and Pbark[1] == False:
    print("one")
elif Pbark[0] == False and Pbark[1] == False:
    print("none")

if Mbark[0] == True and Mbark[1] == True:
    print("both")
elif Mbark[0] == False and Mbark[1] == True:
    print("one")
elif Mbark[0] == True and Mbark[1] == False:
    print("one")
elif Mbark[0] == False and Mbark[1] == False:
    print("none")

if Gbark[0] == True and Gbark[1] == True:
    print("both")
elif Gbark[0] == False and Gbark[1] == True:
    print("one")
elif Gbark[0] == True and Gbark[1] == False:
    print("one")
elif Gbark[0] == False and Gbark[1] == False:
    print("none")


