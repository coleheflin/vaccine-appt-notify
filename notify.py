from dotenv import load_dotenv
from pathlib import Path
import pyautogui
import smtplib
import time
import os

def send_email(SENDER_EMAIL, SENDER_PASS, RECEIVER_EMAIL, EMAIL_TEXT):
	print(EMAIL_TEXT)
	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	  
	# start TLS for security 
	s.starttls() 
	  
	# Authentication 
	s.login(SENDER_EMAIL, SENDER_PASS)
	  
	# sending the mail 
	s.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, EMAIL_TEXT) 
	  
	# terminating the session 
	s.quit()

	return None

# loading in environment vars
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_PASS = os.environ['SENDER_PASSWORD']
RECEIVER_EMAILS= os.environ['RECEIVER_EMAILS'].split(',')
BODY = 'Found a vaccine appointment, please go to https://www.sandiegocounty.gov/content/sdc/hhsa/programs/phs/community_epidemiology/dc/2019-nCoV/vaccines/vax-schedule-appointment.html#petcoInstructions to register now'
SUBJECT = 'Vaccine Appointment Available!!!'
EMAIL_TEXT = """\
From: %s
To: %s
Subject: %s

%s
""" % (SENDER_EMAIL, RECEIVER_EMAILS, SUBJECT, BODY)

for i in range(1000):
    print(i)
    pyautogui.click()
    time.sleep(10)

    found_appointment = pyautogui.locateCenterOnScreen('sorry_pic.png')
    if not found_appointment:
        print('Found appointment!!')
        send_email(SENDER_EMAIL, SENDER_PASS, RECEIVER_EMAILS, EMAIL_TEXT)
        break
    else:
        print('Did not find appt')
    time.sleep(100)
	
	
