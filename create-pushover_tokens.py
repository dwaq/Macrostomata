# get the application token
print "Go to: https://pushover.net/apps"
print "Choose \"Create a New Application\""
print "Fill in the necessary information and then click \"Create Application\""
print "\nFrom the next page, copy the necessary information at the prompt."
application_token = raw_input("Enter the API Token/Key here: ").strip()

# get the user token
print "\nGo to: https://pushover.net"
print "\nFrom this page, copy the necessary information at the prompt."
user_token = raw_input("Enter Your User Key here: ").strip()

# Create text document with access token in it
dropboxFile = open("pushover_tokens.py", "w")
dropboxFile.writelines("# Application specific variables for Pushover")
dropboxFile.writelines("\napplication_token = \""+application_token+"\"")
dropboxFile.writelines("\nuser_token = \""+user_token+"\"")
dropboxFile.close()
print "The Pushover application and user tokens were written successfully."
