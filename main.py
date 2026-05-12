##################### Extra Hard Starting Project ######################
import random

import pandas as pd
import datetime as dt
import smtplib

# 1. Update the birthdays.csv
data = pd.read_csv('birthdays.csv')
#birth_list = data.to_dict('records')

#print(birth_list)

now = dt.datetime.now()
#today_date = now.date()
today_date = now.day
today_month = now.month
print(today_date)
print(today_month)




my_email = "oneglobalinc8888@gmail.com"
password = "drhqgrxprsmhjckn"

with open("./letter_templates/letter_1.txt", "r") as f:
    letter_1 = f.read()

with open("./letter_templates/letter_2.txt", "r") as f:
    letter_2 = f.read()

with open("./letter_templates/letter_3.txt", "r") as f:
    letter_3 = f.read()

letter_list = [letter_1, letter_2, letter_3]

def send_email(to_address,email_content):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(to_addrs=email,
                            from_addr=my_email,
                            msg=f"Subject: Hello World!\n\n{email_content}"
                            )


# 2. Check if today matches a birthday in the birthdays.csv
#
# if today_date in birth_list["day"].values and today_month in birth_list["month"].values:
#     birthday_person = birth_list["name"]
#     print(birthday_person)

birthday_person_row = data[(today_month == data["month"]) & (today_date == data["day"])]
if not birthday_person_row.empty:
    name = birthday_person_row["name"].item()
    email = birthday_person_row["email"].item()
    picked_letter = random.choice(letter_list)
    final_letter = picked_letter.replace("[NAME]", name)
    #print(picked_letter)

    send_email(to_address=email, email_content=final_letter)

# for birth in birth_list:
#     if :
#        birthday_person = birth_list[birth]["name"]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




