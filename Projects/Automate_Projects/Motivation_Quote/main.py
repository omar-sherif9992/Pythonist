import random, smtplib

with open(file="quotes.txt") as file:
    lines = file.readlines()
    my_email = str(input("Please enter your email : "))  # the part after the @ is the identity of my email provider
    my_password = str(input("Please enter your Password : "))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # location of our email provider
        connection.starttls()  # to secure the email
        connection.login(user=my_email, password=my_password)  # login to your email
        connection.sendmail(from_addr=my_email,
                            to_addrs="omar.sherif9991@gmail.com",
                            msg=f"Subject:Motivation Quote!\n\n{random.choice(lines)}")  # sending the email
