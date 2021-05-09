temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(temperature))  # показываю что новый список не создавал
i = 0
while i < len(temperature):
    if temperature[i].isdigit() or temperature[i][1:].isdigit():
        if temperature[i][0] == '+' or temperature[i][0] == '-':
            temper = temperature[i][0]
            temperature[i] = temper + temperature[i][1:].zfill(2)
        temperature[i] = temperature[i].zfill(2)
        temperature.insert(i, '"')
        temperature.insert(i + 2, '"')
        i = i + 2
    i = i + 1
print(id(temperature))  # показываю что новый список не создавал
i = 0
while i < len(temperature):
    if temperature[i].isdigit() or temperature[i][1:].isdigit():
        temperature[i] = temperature[i - 1] + temperature[i] + temperature[i + 1]
        temperature.pop(i + 1)
        temperature.pop(i - 1)
    i = i + 1
output = ' '.join(temperature)
print(id(temperature))  # показываю что новый список не создавал
print(output)
