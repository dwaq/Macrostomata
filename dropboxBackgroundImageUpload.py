import sys
from dropbox_token import access_token
import dropbox
from time import localtime, strftime, time, sleep
import subprocess
import os

# parse the arguments recieved when starting
# [0]=script name, [1]=folder name, [2]=iterations, [3]=time between
if (2 <= len(sys.argv) <= 4):
    folderName = sys.argv[1]
    iterations = 5  #default
    period = 10     #default
if (3 <= len(sys.argv) <= 4):
    iterations = int(sys.argv[2])
if (len(sys.argv) == 4):
    period = int(sys.argv[3])

# class that lets you make Dropbox API calls
client = dropbox.client.DropboxClient(access_token)

def currentDateTime():
    return strftime("%Y-%m-%d---%H-%M-%S", localtime())

for i in range(iterations):
	# get time at beginning of loop
	timeStart = time()

    # take a picture titled the current date/time
    fileName = currentDateTime()+".jpg"
    subprocess.Popen(['raspistill', '-t', '10', '-n', '-o', fileName]).wait()
    print "Image taken:", fileName

    # upload the created image to that folder
    fileInfo = open(fileName, 'rb')
    fileMetadata = client.put_file('/'+folderName+'/'+fileName, fileInfo)

    # delete the file from local storage after it has been uploaded
    fileInfo.close()
    os.remove(fileName)

    # get time after loop has completed and subtract to find the elapsed time of loop
    timeElapsed = time() - timeStart

    # if the time of the loop was longer than the defined period of the loop, don't sleep at all
    if timeElapsed > period:
		period = 0

    # wait in between pictures (won't wait after the last one)
    if i<(iterations):
        sleep(period)
