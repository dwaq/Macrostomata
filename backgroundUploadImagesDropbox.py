import sys
import dropbox
from time import localtime, strftime, sleep
import os

# the first[0] argument is always the script name
#print 'Number of arguments:', len(sys.argv), 'arguments'
#print 'Argument List:', str(sys.argv)

# parse the arguments recieved when starting
# script name, folder name, iterations, time between
if (2 <= len(sys.argv) <= 4):
    folderName = sys.argv[1]
    iterations = 5      #default
    period = 10    #default
if (3 <= len(sys.argv) <= 4):
    iterations = int(sys.argv[2])
if (len(sys.argv) == 4):
    period = int(sys.argv[3])

# open file for authorized app token
textFile = open("dropbox_access_token.txt", "r")
access_token = textFile.readline().rstrip('\t').rstrip('\n')
textFile.close()

# class that lets you make Dropbox API calls
client = dropbox.client.DropboxClient(access_token)

def currentDateTime():
    return strftime("%Y-%m-%d---%H-%M-%S", localtime())

for i in range(iterations):
    # create a file from the command line called the current date/time
    # this will be replaced with a picture taken with the Raspi camera
    fileName = currentDateTime()+".txt"
    print "Image taken:", fileName
    #os.system("<nul (set/p z=) >"+fileName)    # for windows
    os.system("touch "+fileName)    # for linux

    # upload the created file to that folder
    fileInfo = open(fileName, 'rb')
    fileMetadata = client.put_file('/'+folderName+'/'+fileName, fileInfo)

    # delete the file from local storage after it has been uploaded
    # Might need to change method of doing this after I change to actaully taking pictures
    fileInfo.close()
    os.remove(fileName)

    # wait in between pictures
    sleep(period-1)
