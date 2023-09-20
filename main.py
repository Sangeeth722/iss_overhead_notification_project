import requests
from datetime import datetime,timezone
import time
import smtplib


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


#search in google
MY_LAT =  # Your latitude
MY_LONG =  # Your longitude




def iss_in_ur_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    MY_LAT = iss_latitude
    MY_LONG = iss_longitude
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <=MY_LAT + 5 and MY_LONG -5 <=iss_longitude <= MY_LONG+5:
        return True
def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    utc_time = datetime.now(timezone.utc)
    utc_time_hour = utc_time.hour

    if sunset <= utc_time_hour <=sunrise:
        return True
while True:
    time.sleep(60)
    if iss_in_ur_location() and is_night():
        my_email = "@gmail.com"
        paasword = "find in google"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=paasword)
            connection.sendmail(from_addr=my_email, to_addrs="@gmail.com",
                                msg="Subject:ISS IN YOUR LOCATION \n\n Look at the sky")


