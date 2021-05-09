prices = [10.5, 15.5, 9, 55.18, 71, 3.45, 25.95, 32.4, 45, 11]
print(prices)
print(id(prices))  # показываю что новый список не создавал
prices.sort()
print(id(prices))  # показываю что новый список не создавал
prices_reverse = sorted(prices, reverse=True)
print(id(prices_reverse))  # показываю что новый список создаван
i = 0
while i < len(prices):
    prices[i] = str(float(prices[i]))
    prices[i] = prices[i].split('.')
    prices[i][1] = prices[i][1].zfill(2)
    prices[i] = str(f'{prices[i][0]} рублей {prices[i][1]} копеек')
    i = i + 1
output = ', '.join(prices)
output_five_up = ', '.join(prices[-5:])
print(output)  # по возврастанию
print(output_five_up)  # 5 самых дорогих по возврастанию
i = 0
while i < len(prices_reverse):
    prices_reverse[i] = str(float(prices_reverse[i]))
    prices_reverse[i] = prices_reverse[i].split('.')
    prices_reverse[i][1] = prices_reverse[i][1].zfill(2)
    prices_reverse[i] = str(f'{prices_reverse[i][0]} рублей {prices_reverse[i][1]} копеек')
    i = i + 1
output_reverse = ', '.join(prices_reverse)
print(output_reverse)  # по убыванию
