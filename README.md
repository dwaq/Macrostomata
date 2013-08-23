Macrostomata
============

A security system for my apartment. It uses a JeeNode to read the states of the windows and doors and wirelessly sends the data to a JeeLink connected to a Rasperry Pi. The Raspberry Pi uses various python scripts to create a folder in Dropbox of the current date, time, and location of the switch in my apartment. That information is sent as a push notification to my iPhone using Pushover. Over a user-selectable period of time, I take a series of pictures with the Raspberry Pi Camera and upload them to that Dropbox folder.

The name of this project, Macrostomata, is the order of snakes that includes the python - the langauge I'm using for most of the project. Also "macro" relates to programming as an instruction that exands into a set of instructions to perform a task, or means "large-scale", such as the project looks over my entire apartment. "Stomata" is plural for "stoma", which is a pore in a plant, which relates to the raspberry in Raspberry Pi.

* macrostomata.py the main python code running on the Raspberry Pi
* backgroundUploadImagesDropbox.py background task that takes multiple images over a period of time
* dropbox_access_token.txt a text file containing the Dropbox access token
* getDropboxAccesToken.py a script that creates "dropbox_access_token.txt" by using your Dropbox dev account details
* pushoverArgs.py sends a push notification using Pushover
* pushover_tokens.py  contains the application and user tokens to use the Pushover API

This code is a work in progress and will continue to be updated.

This work is licensed under a Creative Commons Attribution 3.0 Unported License.