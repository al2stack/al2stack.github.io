import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 34.207050# Your latitude
MY_LONG = -84.140358 # Your longitude
my_email = "codecoursemail12@gmail.com"
password = "zwmqbkwlgkmptevd"


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LAT - 5 <= iss_longitude <= MY_LAT + 5:
        return True
    else:
        return  False
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True
while True:
    time.sleep(60)
    if is_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="amurove12@yahoo.com",
                                msg=f"Subject:LOOK UP!\n\nLook up the ISS is right above you, \n Astrology forever!")
# BONUS: run the code every 60 seconds.



