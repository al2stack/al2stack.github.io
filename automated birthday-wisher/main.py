
import pandas
import datetime as dt
import random
import smtplib

my_email = "codecoursemail12@gmail.com"
password = "zwmqbkwlgkmptevd"
today =dt.datetime.now()
month= today.month
day= today.day
date_today = (month, day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

if date_today in birthdays_dict:
    birthday_person = birthdays_dict[date_today]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        content = letter.read()
        new_msg = content.replace("[NAME]", birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject:Happy Birthday\n\n{new_msg}")


  


