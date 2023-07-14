# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import cv2 as cv
import time
from time import strftime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from subprocess import call

def imageResize(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    return img
    
def publish(FileName):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    folderName = 'Car Videos'  # Please set the folder name.
    folders = drive.ListFile(
        {
            'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
            file2.SetContentFile(FileName)
            file2.Upload()
            
#publish("output1.mp4")
print("Test")
time.sleep(500)
print("Test")
f = open("messages.txt", "w")
f.close()
videoCount = 0
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'mp4v')
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (width,  height))
start = time.time()

timeArray = ["07:00AM","08:00AM","08:10AM","08:20AM","08:30AM","08:35AM","08:40AM","08:45AM","08:50AM","08:55AM","09:00AM","09:10AM","09:12AM","09:15AM","09:20AM","09:23AM","09:25AM","09:30AM","09:39AM","09:40AM","09:43AM","09:45AM","09:47AM",
"09:50AM","10:00AM""10:10AM""10:20AM""10:30AM""10:40AM""10:50AM","11:00AM","12:00AM","01:00PM","01:10PM","01:20PM","01:27PM","01:29PM","01:30PM","01:40PM","01:50PM",
"02:00PM","03:00PM","03:10PM","03:20PM","03:30PM","03:40PM","03:50PM",
"04:10PM","04:20PM","04:30PM","04:40PM","04:50PM","05:00PM","09:05AM"]
while cap.isOpened():
    #print("test")
    #records the current time on the system clock
    end = time.time()
    if ((end - start) >= 600):
        f = open("messages.txt", "a")
        videoCount += 1
        f.write("Publishing ")
        out.release()
        #publish("output1.mp4")
        Title = "output" + str(videoCount) + ".mp4"
        f.write(Title)
        f.close()
        out = cv.VideoWriter(Title, fourcc, 20.0, (width,  height))
        time.sleep(60)
    else:
        hour = strftime("%I:%M%p")
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            f = open("messages.txt", "a")
            f.write(" exiting at 11:50 ")
            f.close()
            #print("publishing")
            #out.release()
            #publish("output.mp4")
            #os.system("pkill -o chromium")
            break
        #frame = imageResize(frame, 20)
        if count == 5:
            out.write(frame)
            count = 0
            #print(hour)
            cv.imshow("Frame",frame)
        if cv.waitKey(1) == ord('q'):#sets the speed of the video
            break
        #for x in range(len(timeArray)):
            #if hour == timeArray[x]:
        
        if hour == "02:32PM":
            f = open("messages.txt", "a")
            f.write(" exiting at 10:50 ")
            f.close()
            cap.release()
            cv.destroyAllWindows()
            time.sleep(120)
            #call("sudo shutdown -h now", shell=True)
            quit()
        count += 1
        
    
cap.release()
cv.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
