import os
from twilio.rest import Client

class NotificationManager:
    """This class is responsible for sending notifications with the Api key."""
    from_ = os.environ.get("FROM")
    account_sid = os.environ.get("ACCOUNT_SID")  # Copied from my Dashboard remove config and write yours as a string
    auth_token = os.environ.get("AUTH_TOKEN")  # Copied from my Dashboard  remove config and write yours as a string

    def send_sms(self,message:str,to:str):
        """Sends an sms message"""
        client = Client(self.account_sid, self.auth_token)
        message_t = client.messages \
            .create(
            body=message,
            from_=self.from_,
            to=to
        )
        print(message_t.sid)
        if message_t.status == "queued":

            print("Process Completed 100%")
