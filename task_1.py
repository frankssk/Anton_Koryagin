import time


class TrafficLight:
    def __init__(self):
        self.__color = 'Не работает'

    def running(self):
        self.__color = 'Красный'
        yield self.__color
        time.sleep(7)
        self.__color = 'Желтый'
        yield self.__color
        time.sleep(2)
        self.__color = 'Зеленый'
        yield self.__color
        time.sleep(1)


if __name__ == '__main__':
    traffic_light = TrafficLight()
    correct_order = ['Красный', 'Желтый', 'Зеленый']
    correct = 1
    while True:
        i = 1
        light_other = []
        if correct == 1:
            for light in traffic_light.running():
                light_other.append(light)
                if light_other != correct_order[:i]:
                    print('Светофор не исправен')
                    correct = 0
                    break
                else:
                    print(light)
                    i += 1
        else:
            break
