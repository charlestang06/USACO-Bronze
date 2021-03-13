N = int(input())
type = []
lower_bound = []
upper_bound = []
for x in range(N):
    x = input().split()
    type.append(x[0])
    lower_bound.append(int(x[1]))
    upper_bound.append(int(x[2]))

counter = 0
minimumnone = 100
maximumnone = 0
for x in type:
    if x == 'none':
        if counter <= minimumnone:
            minimumnone = counter
        if counter >= maximumnone:
            maximumnone = counter
    counter += 1

upper_bound_after = 0
lower_bound_after = 0

lower_bound_before = 0
upper_bound_before = 0


for x in range(maximumnone, -1, -1): #before
    if x == maximumnone:
        lower_bound_before = lower_bound[maximumnone]
        upper_bound_before = upper_bound[maximumnone]
    if type[x] == 'on':
        upper_bound_before -= lower_bound[x]
        lower_bound_before -= upper_bound[x]
    elif type[x] == 'off':
        upper_bound_before += upper_bound[x]
        lower_bound_before += lower_bound[x]
    elif type[x] == 'none':
        #find intersection of the things
        if lower_bound[x] > lower_bound_before:
            lower_bound_before = lower_bound[x]
        if upper_bound[x] < upper_bound_before:
            upper_bound_before = upper_bound[x]
#    if lower_bound_before < 0:
#        lower_bound_before = 0
#    if upper_bound_before < 0:
#        upper_bound_before = 0


print(str(lower_bound_before) + " " + str(upper_bound_before))

for x in range(minimumnone, N): #after
    if x == minimumnone:
        lower_bound_after = lower_bound[minimumnone]
        upper_bound_after = upper_bound[minimumnone]
    elif type[x] == 'on':
        upper_bound_after += upper_bound[x]
        lower_bound_after += lower_bound[x]
    elif type[x] == 'off':
        upper_bound_after -= lower_bound[x]
        lower_bound_after -= upper_bound[x]
    elif type[x] == 'none':
        #find intersection of the things
        if lower_bound[x] > lower_bound_after:
            lower_bound_after = lower_bound[x]
        if upper_bound[x] < upper_bound_after:
            upper_bound_after = upper_bound[x]
#    if lower_bound_after < 0:
#        lower_bound_after = 0
#    if upper_bound_after < 0:
#        upper_bound_after = 0

print(str(lower_bound_after) + " " + str(upper_bound_after))