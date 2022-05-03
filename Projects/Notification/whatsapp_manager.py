from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
import subprocess
# subprocess.Popen(r'explorer /select,""')

ACCOUNT_SID=os.environ.get("ACCOUNT_SID")
AUTH_TOKEN=os.environ.get("AUTH_TOKEN")
FROM=os.environ.get("WHATSAPP_FROM")
TO=os.environ.get("TO")
print(FROM)

client=Client(ACCOUNT_SID,AUTH_TOKEN)
message=client.messages.create(body="hi bro",from_=f"whatsapp:{FROM}",to=f"whatsapp:{TO}")
