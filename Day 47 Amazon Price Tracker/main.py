import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL_ADDRESS = 0
EMAIL_PASSWORD = 0
PRODUCT_URL = 'https://www.amazon.co.uk/iRasptek-Raspberry-8GB-Starter-Pre-installed/dp/B0D1D6RFNG/ref=sr_1_2?crid=OQEPCKQPZKWB&dib=eyJ2IjoiMSJ9.FjwMamt6biMIgU5rbxqVpLaSJmstI4EynCvAYbjRGWwwLji5EaZ-4SwwJ1A8-SXhuitwL5o15yFo_Hejf617AAkXI6IBpw3gziC6-kAflIkAQVuSJoeVg_eLv43r9TGdi0Llljs1KRs5ESOdO1aY7NHlP9meNfkUIaf8VVUZDKsp7JvjgHNAKap-puPJ92OPmDsAmezh8_UdAZOXky3FKwtn9U5b5S48a5mX8JpPxjc.rBDp9wkWJOhcU5Jg5NtghQ5hkc4RkcSMKRK7o_44y_k&dib_tag=se&keywords=raspberry+pi&qid=1763888656&sprefix=raspberry+pi%2Caps%2C97&sr=8-2'
TARGET_PRICE = 140

header = {
    'Accept-Language': 'en-GB,en;q=0.5',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0'
}
response = requests.get(url=PRODUCT_URL, headers=header)


content = response.text
soup = BeautifulSoup(content, "html.parser")

price = soup.find(name="span", class_ = "a-offscreen").text

int_price = float(price[1:])

if int_price <= TARGET_PRICE:
    '''
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS, 
            to_addrs=EMAIL_ADDRESS, 
            msg=f"Subject: Price!\n\nPrice Dropped down to {price}, Go check it out: {PRODUCT_URL}"
        )
        print("Email sent successfully!")
    '''
    print(int_price, type(int_price))