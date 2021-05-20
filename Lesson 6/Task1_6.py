import time

class TrafficLight:
    #color = ["Красный","Желтый","Зеленый"]

    def running(self):
        __color = ["Красный", "Желтый", "Зеленый"]
        while True:
            print("\033[31m{}".format(__color[0]))
            time.sleep(7)
            print("\033[33m{}".format(__color[1]))
            time.sleep(2)
            print("\033[32m{}".format(__color[2]))
            time.sleep(5)
            print("\033[33m{}".format(__color[1]))
            time.sleep(2)
a = TrafficLight()
a.running()