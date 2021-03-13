N =int(input())
positions = [None, None, None, None, None, None, None, None]
possible_lists = []

restrictions = []
for x in range(N):
    input_ = input().split()
    restrictions.append([input_[0], input_[len(input_)-1]])

counter = 0


for Bessie in range(0, 8):
    positions[Bessie] = 'Bessie'

    for Buttercup in range(0, 8):

        if Buttercup == Bessie:
            continue
        positions[Buttercup] = 'Buttercup'

        for Belinda in range(0, 8):

            if Belinda == Buttercup or Belinda == Bessie:
                continue
            positions[Belinda] = 'Belinda'

            for Beatrice in range(0, 8):

                if Beatrice == Belinda or Beatrice == Buttercup or Beatrice == Bessie:
                    continue
                positions[Beatrice] = 'Beatrice'

                for Bella in range(0, 8):

                    if Bella == Beatrice or Bella == Belinda or Bella == Buttercup or Bella == Bessie:
                        continue
                    positions[Bella] = 'Bella'

                    for Blue in range(0, 8):

                        if Blue == Bella or Blue == Beatrice or Blue == Belinda or Blue == Buttercup or Blue == Bessie:
                            continue
                        positions[Blue] = 'Blue'

                        for Betsy in range(0, 8):

                            if Betsy == Blue or Betsy == Bella or Betsy == Beatrice or Betsy == Belinda or Betsy == Buttercup or Betsy == Bessie:
                                continue
                            positions[Betsy] = 'Betsy'

                            for Sue in range(0, 8):

                                if Sue == Betsy or Sue == Blue or Sue == Bella or Sue == Beatrice or Sue == Belinda or Sue == Buttercup or Sue == Bessie:
                                    continue
                                positions[Sue] = 'Sue'
                                counter += 1
                                asdfasdf = True

                                for x in restrictions:
                                    cow_one = positions.index(x[0])
                                    cow_two = positions.index(x[1])
                                    if abs(cow_one - cow_two) != 1:
                                        asdfasdf = False
                                        break

                                if asdfasdf == True:
                                    possible_lists.append(positions)




print(min(possible_lists))




