Macrostomata
============

A security system for my apartment. It uses a JeeNode to read the states of the windows and doors and wirelessly sends the data to a JeeLink connected to a Rasperry Pi. The Raspberry Pi uses various python scripts to create a folder in Dropbox of the current date, time, and location of the switch in my apartment. That information is sent as a push notification to my iPhone using Pushover. Over a user-selectable period of time, I take a series of pictures with the Raspberry Pi Camera and upload them to that Dropbox folder.

The name of this project, Macrostomata, is the order of snakes that includes the python - the langauge I'm using for most of the project. Also "macro" relates to programming as an instruction that exands into a set of instructions to perform a task, or means "large-scale", such as the project looks over my entire apartment. "Stomata" is plural for "stoma", which is a pore in a plant, which relates to the raspberry in Raspberry Pi.

* macrostomata.py the main python code running on the Raspberry Pi
* dropboxBackgroundImageUpload.py background task that takes multiple images over a period of time
* dropbox_token.py contains the Dropbox access token (an example is given)
* create-dropbox_token.py a script that creates "dropbox_token.py" by using your Dropbox developer account details
* pushover.py sends a push notification using Pushover
* pushover_tokens.py  contains the application and user tokens to use the Pushover API (an example is given)
* create-pushover_tokens.py a script that creates "pushover_tokens.py" by using your Pushover account details
* icon.png my personal icon for the Pushover app
* jeenode.ino the Arduino code for the JeeNode
* RF12demo.ino the Arduino code for the JeeLink

This code is a work in progress and will continue to be updated.

This work is licensed under a Creative Commons Attribution 3.0 Unported License.