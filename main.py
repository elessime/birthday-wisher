import datetime as dt
import os
import random
import smtplib
import pandas

my_email = "great@gmail.com"
password = "żyrafywchodządoszafy"
to_email = "better@gmail.com"

birthdays = pandas.read_csv("birthdays.csv")
birt_list = birthdays.to_dict(orient="records")

now = dt.datetime.now()
now_month = now.month
now_day = now.day


def prepare_letter(address_name):
    letters = os.listdir("letter_templates")
    current_letter = random.choice(letters)
    with open(f"letter_templates/{current_letter}") as letter:
        letter_content = letter.read()
        return letter_content.replace("[NAME]", address_name)


def send_email(send_to, letter_content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to,
            msg=f"Subject:Happy Birthday!!!\n\n{letter_content}"
        )


for record in birt_list:
    if record["month"] == now_month and record["day"] == now_day:
        content = prepare_letter(record["name"])
        send_email(record["email"], content)
