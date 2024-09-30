import requests 
import smtplib  
import datetime as dt
import os
from dotenv import load_dotenv 
import json

# load environment variables
load_dotenv()

NINJAS_API_KEY = os.getenv('NINJAS_API_KEY')
MY_EMAIL = os.getenv('MY_EMAIL')
MY_EMAIL_PASSWORD = os.getenv('MY_EMAIL_PASSWORD')

def send_mail(received_quote, received_author):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()   # encrypts email
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        message = f'Subject: 🧠Monday Motivation🫀\n\n"{received_quote}"\n-{received_author}\n\nKeep pushing, you will archive your Goals!\nLove you!'
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=message.encode("utf-8"))
        
now = dt.datetime.now()
day_of_week = now.weekday()

# API stuff
Ninja_header = {
    "X-Api-Key": NINJAS_API_KEY
}
response_Ninja = requests.get(url=f"https://api.api-ninjas.com/v1/quotes", headers=Ninja_header)

if response_Ninja.status_code == 200:
    quote_data = json.loads(response_Ninja.text)
    quote = quote_data[0]["quote"]
    author = quote_data[0]["author"]
    #category = quote_data[0]["category"]
    
    # if monday call send_mail function, pass parameters
    if day_of_week == 6:
        send_mail(received_quote=quote, received_author=author)

else:
    print("Error:", response_Ninja.status_code, response_Ninja.text)

