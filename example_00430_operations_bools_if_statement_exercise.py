# you have 2 numbers, 5 and 10
# if the first is bigger than the second, print bigger
# if the second is bigger, print smaller
# otherwise print equal
num_one = 5
num_two = 10

if num_one > num_two:
    print('bigger')
elif num_two < num_one:
    print('smaller')
else:
    print('equal')


# you have a variable called "age"
# if age is smaller than 2, print baby
# if age is between 2 and 18, print kid
# otherwise print adult
age = 1
baby = 2
kid = 18

if age < baby:
    print('baby')
elif baby <= age < kid:
    print('kid')
else:
    print('adult')
