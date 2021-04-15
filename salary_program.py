#IS 51 Test1 by Christopher Marshall
# calculate the value of option 1

option_1 = 10 * 100

# calculate the value of option 2

i = 0
d = 1
option_2 = 0

while i < 10:
    i = i + 1
    option_2 = option_2 + d
    d = d * 2

# compare the values and print the result

if option_1 > option_2:
    print("Option 1 is better")
elif option_2 > option_1:
    print("Option 2 is better")
else:
    print("Option 1 and Option 2 pays the same")
