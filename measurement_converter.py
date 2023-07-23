# Enter amount of lemon juice (in cups):
# 2
# Enter amount of water (in cups):
# 16
# Enter amount of agave nectar (in cups):
# 2.5
# How many servings does this make?
# 6

# Lemonade ingredients - yields 6.00 servings
# 2.00 cup(s) lemon juice
# 16.00 cup(s) water
# 2.50 cup(s) agave nectar
# (2) Prompt the user to specify the desired number of servings. Adjust the amounts of each ingredient accordingly, and then output the ingredients and serving size. (Submit for 4 points, so 6 points total).

# How many servings would you like to make?
# 48

# Lemonade ingredients - yields 48.00 servings
# 16.00 cup(s) lemon juice
# 128.00 cup(s) water
# 20.00 cup(s) agave nectar
# (3) Convert the ingredient measurements from (2) to gallons. Output the ingredients and serving size. Note: There are 16 cups in a gallon. (Submit for 2 points, so 8 points total).

# Lemonade ingredients - yields 48.00 servings
# 1.00 gallon(s) lemon juice
# 8.00 gallon(s) water
# 1.25 gallon(s) agave nectar

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingredients
print('Lemonade ingredients - yields',f'{servings:.2f}','servings')
print(f'{lemon_juice_cups:.2f}','cup(s) lemon juice')
print(f'{ water_cups:.2f}','cup(s) water')
print(f'{agave_nectar_cups:.2f}', 'cup(s) agave nectar\n')
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
desired_servings = float(input('How many servings would you like to make?\n\n'))
print('Lemonade ingredients - yields',f'{desired_servings:.2f}', 'servings')
amount = desired_servings / servings
print(f'{lemon_juice_cups * amount:.2f}','cup(s) lemon juice')
print(f'{ water_cups * amount:.2f}','cup(s) water')
print(f'{agave_nectar_cups * amount:.2f}', 'cup(s) agave nectar\n')