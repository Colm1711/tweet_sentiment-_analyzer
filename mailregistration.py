#IMPORTS

import smtplib
import json

# VARS

creds_admin = open('admin_creds.json')
admin_data = json.load(creds_admin)

# CONSTANTS
USER = admin_data.get('user')
PASSWD = admin_data.get('passw')

# Setting up session

smtp = smtplib.SMTP()
smtp.connect("smtp.gmail.com", 587)
smtp.starttls()
smtp.login(USER, PASSWD)