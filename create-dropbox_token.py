# To install the Dropbox API, go to:
# https://www.dropbox.com/developers/core/sdks/python
# and download the python SDK.
# Unzip the folder and open a command prompt inside that folder.
# Enter "python setup.py install" and it will install.

import dropbox

# Get your app key and secret from the Dropbox developer website
print "Go to: https://www.dropbox.com/developers/apps/create"
print "Choose \"Dropbox API app\", \"Files and datastores\", \"Yes\""
print "And then name your app."

print "\nFrom your app page, copy the necessary information at the prompt."
app_key = raw_input("Enter the app key here: ").strip()
app_secret = raw_input("Enter the app secret here: ").strip()

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '\n1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

# Create text document with access token in it
dropboxFile = open("dropbox_token.py", "w")
dropboxFile.writelines("# Application specific variable for Dropbox")
dropboxFile.writelines("\naccess_token = \""+access_token+"\"")
dropboxFile.close()
print "The Dropbox access token was written successfully."
