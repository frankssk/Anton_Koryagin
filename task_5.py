class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    @staticmethod
    def draw():
        print('Pen')


class Pencil(Stationery):
    @staticmethod
    def draw():
        print('Pencil')


class Handle(Stationery):
    @staticmethod
    def draw():
        print('Handle')
