import smtplib
import datetime as dt
import pandas
import random
import os
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSW = os.getenv("PASSW")

# Use a relative path for better cross-platform compatibility
BIRTHDAYS_FILE = "Day 32 Birthday Mail/birthdays.csv"
LETTERS_DIR = "Day 32 Birthday Mail/letter_templates"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# --- DATA LOADING ---
data = pandas.read_csv(BIRTHDAYS_FILE)
data_dict = data.to_dict(orient="records")

# --- DATE CHECKING ---
now = dt.datetime.now()
current_day = now.day
current_month = now.month

# --- MAIN LOOP ---
for person in data_dict:
    person_month = person["month"]
    person_day = person["day"]
    person_name = person["name"]
    target_email = person["email"]

    if (current_day, current_month) == (person_day, person_month):
        print(f"It's {person_name}'s birthday! Sending email to {target_email}...")

        random_letter_path = f"{LETTERS_DIR}/{random.choice(LETTERS)}"
        
        with open(random_letter_path) as file:
            content = file.read()
            personalized_letter = content.replace("[NAME]", person_name)
        
        # --- SEND EMAIL ---
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSW)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=target_email, 
                    msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email to {person_name}: {e}")