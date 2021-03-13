N = int(input())
max_guesses_correct = 0
guesses_correct = 0

swap_a = []
swap_b = []
guess_array = []

for x in range(N):
    temp_list = input().split()
    swap_a.append(int(temp_list[0]))
    swap_b.append(int(temp_list[1]))
    guess_array.append(int(temp_list[2]))

main_array = [True, False, False]
guesses_1 = 0
for x in range(N):
    placeholder = main_array[swap_a[x]-1]
    main_array[swap_a[x]-1] = main_array[swap_b[x]-1]
    main_array[swap_b[x]-1] = placeholder
    if main_array[guess_array[x]-1] == True:
        guesses_1 += 1

main_array = [False, True, False]
guesses_2 = 0
for x in range(N):
    placeholder = main_array[swap_a[x]-1]
    main_array[swap_a[x]-1] = main_array[swap_b[x]-1]
    main_array[swap_b[x]-1] = placeholder
    if main_array[guess_array[x]-1] == True:
        guesses_2 += 1

main_array = [False, False, True]
guesses_3 = 0
for x in range(N):
    placeholder = main_array[swap_a[x]-1]
    main_array[swap_a[x]-1] = main_array[swap_b[x]-1]
    main_array[swap_b[x]-1] = placeholder
    if main_array[guess_array[x]-1] == True:
        guesses_3 += 1

max_guesses_correct = max(guesses_1, guesses_2, guesses_3)
print(max_guesses_correct)