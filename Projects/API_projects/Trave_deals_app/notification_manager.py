from decouple import config
from twilio.rest import Client

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_sms(self,message:str):
        account_sid = config("ACCOUNT_SID")  # Copied from my Dashboard remove config and write yours as a string
        auth_token = config("AUTH_TOKEN")  # Copied from my Dashboard  remove config and write yours as a string

        client = Client(account_sid, auth_token)

        message_t = client.messages \
            .create(
            body=message,
            from_=config("FROM"),
            to=config("TO")
        )

        print(message_t.sid)
        if message_t.status == "queued":
            print("Process Completed 100%")
