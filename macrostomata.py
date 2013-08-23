from time import localtime, strftime
import serial
import dropbox
import os
import subprocess
import sys

""" Configurations for python script that takes photos in background and uploads them to Dropbox """
iterations = 4  # How many images the camera will take
period = 5      # How many seconds in between images

# 3 sensors
bedroomWindow = 0
frontDoor = 0
BalconyDoor = 0

# 3 sensors last state
bedroomWindowLS = 0
frontDoorLS = 0
BalconyDoorLS = 0

# default dataState
dataState = 0b0000

# start serial
ser=serial.Serial('/dev/ttyUSB0', 57600)

# open file for authorized app token
textFile = open("dropbox_access_token.txt", "r")
access_token = textFile.readline().rstrip('\t').rstrip('\n')
textFile.close()

# read serial data from JeeLink
def readSerial():
    global dataState
    recievedData = ser.readline()
    # if received successfully, pull out button state
    # if not, read next line
    if (recievedData.find("OK") == 0):
        dataState = int(recievedData[5:7].rstrip('\0')) #strip out null byte
    else:
        readSerial()


def getBits():
    global bedroomWindow, frontDoor, BalconyDoor
    
    # Sets a value for each bit of the data
    bedroomWindow = ((dataState & 0b0001) >> 0)
    frontDoor = ((dataState & 0b0010) >> 1)
    BalconyDoor = ((dataState & 0b0100) >> 2)

# get current time
def currentTime():
    return strftime("%H:%M:%S", localtime())

# get current date
def currentDate():
    return strftime("%m/%d/%Y", localtime())

# get current date and time
def currentDateTime():
    return strftime("%Y-%m-%d---%H-%M-%S", localtime())

# create title and message based on changing states
# assumes only one state ever changes at a time
def stateChanged():
    # if nothing changes, these will both equal 0
    global title, message
    title = 0
    message = 0
    
    if (bedroomWindow == 1 and bedroomWindowLS == 0):
        title = "Bedroom Window"
        message = "opened at "+ currentTime()+ " on "+ currentDate()

    if (bedroomWindow== 0 and bedroomWindowLS == 1):
        title = "Bedroom Window"
        message = "closed at "+ currentTime()+ " on "+ currentDate()

    if (frontDoor == 1 and frontDoorLS == 0):
        title = "Front Door"
        message = "opened at "+ currentTime()+ " on "+ currentDate()

    if (frontDoor == 0 and frontDoorLS == 1):
        title = "Front Door"
        message = "closed at "+ currentTime()+ " on "+ currentDate()

    if (BalconyDoor == 1 and BalconyDoorLS == 0):
        title = "Balcony Door"
        message = "opened at "+ currentTime()+ " on "+ currentDate()

    if (BalconyDoor == 0 and BalconyDoorLS == 1):
        title = "Balcony Door"
        message = "closed at "+ currentTime()+ " on "+ currentDate()

def createFolderDropbox():
    # class that lets you make Dropbox API calls
    client = dropbox.client.DropboxClient(access_token)
    
    # create folder called the current date/time
    folderName = currentDateTime()+"---"+title
    folderMetadata = client.file_create_folder('/'+folderName+'/')

    # subprocess.Popen
        # Execute a child program in a new process
    # sys.executable
        # The path of the executable for the Python interpreter
    subprocess.Popen([sys.executable, "backgroundUploadImagesDropbox.py", str(folderName), str(iterations), str(period)])

    # create a sharable link to that folder
    folderShare = client.share('/'+folderName+'/')
    url = folderShare['url']
    return url

def sendChanges():
    # something changed
    if (title != 0 and message != 0):
        # if something opens, want to take pictures
        if (message[0:6] == "opened"):
            url = createFolderDropbox()
            # change to send via pushover
            print title, ":", message, ":", url
            #pushover.notify_tmu(title, message, url)
            subprocess.Popen([sys.executable, "pushoverArgs.py", str(title), str(message), str(url)])
        # something closed, don't need pictures, just notification
        elif (message[0:6] == "closed"):
            print title, ":", message
            #pushover.notify_tm(title, message)
            subprocess.Popen([sys.executable, "pushoverArgs.py", str(title), str(message)])
    else:
        print "Nothing has changed"

# change last state to current state
def makeCurrentLast():
    global bedroomWindowLS, frontDoorLS, BalconyDoorLS
    bedroomWindowLS = bedroomWindow
    frontDoorLS = frontDoor
    BalconyDoorLS = BalconyDoor



# formats the number to always show 7 bits
# (2 for 0b prefix, and 5 for binary digits)
#print format(dataState, '#06b')


# display the values to ensure it's done right
#print "xb0"+str(BalconyDoor)+str(frontDoor)+str(bedroomWindow)


#### Main loop
while(True):
    readSerial() # strips out data to get the important bits
    getBits() # finds state of each bit in serial
    stateChanged() # looks to see if any states have changed
    sendChanges() # f anything changed, will print/send via pushover
    makeCurrentLast() # makes the last state the current state
