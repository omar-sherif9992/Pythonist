import smtplib
from decouple import config


class EmailManager:

    def send_email(self,title:str ,message: str, to_addrs: str, first_name: str, last_name: str):
        my_email = config("MY_SUPPORT_EMAIL")  # the part after the @ is the identity of my email provider
        my_password = config("MY_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # location of our email provider
            connection.starttls()  # to secure the email
            connection.login(user=my_email, password=my_password)  # login to your email
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_addrs,
                                msg=f"Subject: {title}\n\nDear {first_name} {last_name},\n\n\n {message}.")  # sending the email
            print("Process is Completed 100%")
