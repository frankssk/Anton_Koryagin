class Road:
    _MASS_TO_1CM = 25
    _width = 1
    _length = 1
    _thickness = 1

    def __init__(self, width, length, thickness):
        self._width = width
        self._length = length
        self._thickness = thickness

    def mass_calculation(self):
        mass = (self._width * self._length * self._MASS_TO_1CM * self._thickness) / 1000
        return mass


if __name__ == '__main__':
    print('Программа расчета веса асфальта')
    width = int(input('Введите ширину:\n'))
    length = int(input('Введите длинну:\n'))
    thickness = int(input('Введите толщину:\n'))
    road = Road(width, length, thickness)
    mass = road.mass_calculation()
    print(f'при ширине {width} м. длинне {length} м. и толщине {thickness} см. масса асфальта составляет {mass} т.')
