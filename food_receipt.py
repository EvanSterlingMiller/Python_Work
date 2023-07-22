# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')


# (1) Prompt the user to input a food item name, price, and quantity. Output an itemized receipt. (Submit for 2 points)

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00
# (2) Extend the program to prompt the user for a second item. Output an itemized receipt. (Submit for 2 points, so 4 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00


# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# 4 ice cream @ $2.50 = $10.00
# Total cost: $20.00
# (3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost. Output the total cost, the cost of gratuity, and the grand total. (Submit for 3 points, so 7 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00


# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# 4 ice cream @ $2.50 = $10.00
# Total cost: $20.00

# 15% gratuity: $3.00
# Total with tip: $23.00

item_name = input('Enter food item name:\n')
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n\n'))
receipt1 = item_price * item_quantity
print('RECEIPT')
print(item_quantity, item_name, '@',f'${item_price:.2f}', '=',f'${receipt1:.2f}')
print('Total cost:', f'${receipt1:.2f}\n\n')


item_name2 = input('Enter second food item name:\n')
item_price2 = float(input('Enter item price:\n'))
item_quantity2 = int(input('Enter item quantity:\n\n'))
receipt2 = item_price2 * item_quantity2
print('RECEIPT')
print(item_quantity, item_name, '@',f'${item_price:.2f}', '=',f'${receipt1:.2f}')
print(item_quantity2, item_name2, '@',f'${item_price2:.2f}', '=',f'${receipt2:.2f}')
receipt3 = receipt2 + receipt1
print('Total cost:', f'${receipt3:.2f}\n')

gratuity = 0.15 * receipt3
print('15% gratuity:', f'${gratuity:.2f}')
receipt4 = receipt3 + gratuity
print('Total with tip:', f'${receipt4:.2f}')