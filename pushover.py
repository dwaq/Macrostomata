from pushover_tokens import application_token, user_token
import httplib, urllib
import sys

# Notification sends title, message, and url
def notify_tmu(title, message, url):
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
    "token": application_token,
    "user": user_token,
    "title": title,
    "message": message,
    "url": url,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# Notification sends title and message
def notify_tm(title, message):
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
    "token": application_token,
    "user": user_token,
    "title": title,
    "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# Notification sends message and url
def notify_mu(message, url):
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
    "token": application_token,
    "user": user_token,
    "message": message,
    "url": url,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# Notification sends only message
def notify_m(message):
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
    "token": application_token,
    "user": user_token,
    "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# Start your connection with the Pushover API server
conn = httplib.HTTPSConnection("api.pushover.net:443")

# send title and message
if (len(sys.argv) == 3):
    title = str(sys.argv[1])
    message = str(sys.argv[2])
    notify_tm(title, message)

# send title, message, and url
if (len(sys.argv) == 4):
    title = str(sys.argv[1])
    message = str(sys.argv[2])
    url = str(sys.argv[3])
    notify_tmu(title, message, url)
