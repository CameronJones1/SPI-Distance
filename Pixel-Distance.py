from time import sleep
from widgetlords.pi_spi import *
import cv2 as cv
from ultralytics import YOLO
from gpiozero import LED
from time import sleep

def ObjectDetect(frame,pixelToDistanceRatio,Distance,led):
	YoloModelPath = os.path.join('.', 'train10', 'weights', 'last.pt')
	YoloModel = YOLO(YoloModelPath)
	class_name_dict = {0: 'Wheel Wash'}
	Results = YoloModel(frame)[0]
	for result in Results.boxes.data.tolist():
		x1, y1, x2, y2, score, class_id = result
		if score > 0.7:
			cv.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
			cv.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                           cv.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv.LINE_AA)
			PixelDist = x2-x1
			numPixelsAtDist = (PixelDist,Distance)
			pixelToDistanceRatio.append(numPixelAtDist)
			led.on()
	return frame,pixelToDistanceRatio
        #print(consecutive_Frame_Count)
        
init()
inputs = Mod8AI()
led = LED(23)
sixTeeninches = 2.6192138671875
distanceRatio = 0.026902173913043476
distanceRatio = distanceRatio/2
pixelToDistanceRatio = []        
cap = cv.VideoCapture(0)
while cap.isOpened():
	ret, frame = cap.read()
	frame = imageResize(frame, 20)
	cv.imshow("Frame", frame)
        # if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	A1 = inputs.read_single(0)
	A2 = inputs.read_single(1)
	A3 = inputs.read_single(2)
	A4 = inputs.read_single(3)
	A5 = inputs.read_single(4)
	A6 = inputs.read_single(5)
	A7 = inputs.read_single(6)
	A8 = inputs.read_single(7)
		
	print(A7)
	if voltage > .05:
		voltage = 4096/3.3
		voltage = A7/voltage
		print("The voltage is " + str(voltage))
		print("The voltage is " + str(voltage) + " miliamps")
		print("")
		distance = (voltage-sixTeeninches)/distanceRatio
		print(distance)
		distance = 16-distance
		print(str(distance) + " inches")
		frame = ObjectDetect(frame=frame,pixelToDistanceRatio=pixelToDistanceRatio,Distance=distance,led=led)
		cv.imshow('frame', frame)
		if cv.waitKey(1) == ord('q'):  # sets the speed of the video
			cap.release()
			cv.destroyAllWindows()
			break
		sleep(2)
		led.off()
		sleep(2)
cap.release()
cv.destroyAllWindows()
