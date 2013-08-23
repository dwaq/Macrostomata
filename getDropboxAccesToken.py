import dropbox

# gotta write where to go and what to do
# Get your app key and secret from the Dropbox developer website
app_key = raw_input("Enter the app key here: ").strip()
app_secret = raw_input("Enter the app secret here: ").strip()

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

# Create text document with access token in it
textFile = open("dropbox_access_token.txt", "w")
textFile.writelines(access_token)
textFile.close()
print "The access token was written successfully."
