# prices = {
# 'Bubblegum': '$2',
# 'Toffee': '$0.2',
# 'Ice cream': '$5',
# 'Milk chocolate': '$4',
# 'Doughnut': '$2.5',
# 'Pancake': '$3.2',
# }

# print('Prices:')
# [print(f'{item}: {price}') for item, price in prices.items()]

earnings = {
'Bubblegum': '202',
'Toffee': '118',
'Ice cream': '2250',
'Milk chocolate': '1680',
'Doughnut': '1075',
'Pancake': '80',
}

print('Earned Amount:')
[print(f"{item}: ${price}")for item, price in earnings.items()]
income = sum([int(price) for price in earnings.values()])
print(f"\nIncome: ${income}")
