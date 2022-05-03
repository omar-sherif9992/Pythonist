import random, smtplib, datetime as dt, pandas


def create_message():
    message = ""
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        line = file.readline()
        while line != "":
            message += line
            line = file.readline()
    return message

def message_to(recievers, names, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # location of our email provider
        my_email = str(input("Please enter your email : "))  # the part after the @ is the identity of my email provider
        my_password = str(input("Please enter your Password : "))
        connection.starttls()  # to secure the email
        connection.login(user=my_email, password=my_password)  # login to your email
        for i in range(0, len(recievers)):
            new_message = message
            new_message = new_message.replace("[NAME]", names[i].title())
            connection.sendmail(from_addr=my_email,
                                to_addrs=recievers[i],
                                msg=f"Subject:Happy Birthday!\n\n{new_message}")  # sending the email


dt = dt.datetime.now()
month = dt.month
day = dt.day
# name,email,year,month,day

data = pandas.read_csv("birthdays.csv")
months = data['month']
emails = data['email']
days = data['day']
names = data['name']

correct_emails = []
correct_names = []

for i in range(0, len(emails)):
    if days[i] == day and months[i] == month:
        correct_names.append(names[i])
        correct_emails.append(emails[i])

message = create_message()

message_to(correct_emails, correct_names, message)
