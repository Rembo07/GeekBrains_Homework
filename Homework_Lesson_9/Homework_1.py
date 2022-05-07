from time import sleep

class TrafficLight:
    def __init__(self):
        print('RED')
        sleep(7)
        print('YELLOW')
        sleep(2)
        print('GREEN')
        sleep(5)



traff = TrafficLight()
print(traff.__init__())
