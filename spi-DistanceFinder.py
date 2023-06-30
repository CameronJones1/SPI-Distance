from time import sleep
from widgetlords.pi_spi import *

init()
inputs = Mod8AI()
sixTeeninches = 2.6192138671875
distanceRatio = 0.026902173913043476
distanceRatio = distanceRatio/2

while True:
    A1 = inputs.read_single(0)
    A2 = inputs.read_single(1)
    A3 = inputs.read_single(2)
    A4 = inputs.read_single(3)
    A5 = inputs.read_single(4)
    A6 = inputs.read_single(5)
    A7 = inputs.read_single(6)
    A8 = inputs.read_single(7)
    
    print(A7)
    voltage = 4096/3.3
    voltage = A7/voltage
    print("The voltage is " + str(voltage))
    print("The voltage is " + str(voltage) + " miliamps")
    print("")
    distance = (voltage-sixTeeninches)/distanceRatio
    print(distance)
    distance = 16-distance
    print(str(distance) + " inches")    
    sleep(2)
