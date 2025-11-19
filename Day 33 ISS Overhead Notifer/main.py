import requests
import smtplib
from datetime import datetime
import os
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSW = os.getenv("PASSW")
MY_LAT = os.getenv("LAT")
MY_LNG = os.getenv("LNG")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude =  float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    
def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
    }
    
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSW)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL, 
                msg=f"Subject: ISS Overhead\n\nThe ISS is above you in the sky."
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email to {MY_EMAIL} : {e}")