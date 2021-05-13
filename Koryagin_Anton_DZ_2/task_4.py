position_name = ['инженер-конструктор Игорь',
                 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй',
                 'директор аэлита']
i = 0
print(id(position_name))  # показываю что новый список не создавал
while i < len(position_name):
    position_name[i] = position_name[i].split(' ')
    name = ''.join(position_name[i][-1:]).capitalize()
    print(f'Привет, {name} !')
    i = i + 1

print(id(position_name))  # показываю что новый список не создавал
