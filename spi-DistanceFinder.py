from time import sleep
from widgetlords.pi_spi import *
import cv2 as cv
import time

init()
inputs = Mod8AI()
sixTeeninches = 2.6192138671875
distanceRatio = 0.026902173913043476
distanceRatio = distanceRatio/2
time.sleep(500)
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'mp4v')
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (width,  height))
f = open("Distances", "a")
f.write("(")
count = 0

while True:
	A1 = inputs.read_single(0)
	A2 = inputs.read_single(1)
	A3 = inputs.read_single(2)
	A4 = inputs.read_single(3)
	A5 = inputs.read_single(4)
	A6 = inputs.read_single(5)
	A7 = inputs.read_single(6)
	A8 = inputs.read_single(7)
	
	ret, frame = cap.read()
    # if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		out.release()
		break
    
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
	if(count < 10):
		f.write(str(distance) + ", ")
		count += 1
	else:
		f.write(str(distance) + ", \n")
		count = 0
	if cv.waitKey(1) == ord('q'):#sets the speed of the video
		break
	sleep(2)
	
cap.release()
cv.destroyAllWindows()
