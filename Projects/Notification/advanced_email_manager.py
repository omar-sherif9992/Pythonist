import smtplib
import os
from email.message import EmailMessage
import imghdr
from dotenv import load_dotenv
class EmailManager:
    def __init__(self):
        load_dotenv()
        self.my_email=os.environ.get('MY_SUPPORT_EMAIL')
        self.my_password=os.environ.get('MY_PASSWORD')

    def send_email(self,subject:str ,message: str, contacts: [], first_name: str, last_name: str ,image_folder_path="",pdf_folder_path="",html_file_path=""):
        previous_cwd=os.getcwd()
        self.msg=EmailMessage()
        self.msg['Subject']=subject
        self.msg['From']=self.my_email
        # self.msg['To']=', '.join(contacts)
        message=f"Dear {first_name} {last_name},\n\n{message}\n\n Best regards,\nOmar\nComputer Science Engineer"
        for contact in contacts:
            self.msg['To']=contact
            if html_file_path=="":
             self.msg.set_content(message)
            else:

                with open(html_file_path) as file:
                    html=file.read()
                    html=html.replace('{{user.email}}',contact.title())
                    html=html.replace('{{name}}',f"Hi {first_name} {last_name},".title())
                self.msg.add_alternative(f"""\
                {html}
                """,subtype='html')

            self.attach_image(image_folder_path, previous_cwd)
            self.attach_pdf(pdf_folder_path, previous_cwd)
            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                # location of our email provider
                connection.login(user=self.my_email, password=self.my_password)  # login to your email
                connection.send_message(self.msg)
                print(f"Email is sent to {contact}")

    def attach_image(self, image_folder_path, previous_cwd):
        """It loops over a folder of images and attach all the images into the email"""
        if image_folder_path != "":
            os.chdir(image_folder_path)
            for image_path in os.listdir("."):
                with open(image_path, "rb") as image:
                    image_data = image.read()
                    image_type = imghdr.what(image.name)
                    image_name = image.name
                self.msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        os.chdir(previous_cwd)

    def attach_pdf(self, pdf_folder_path, previous_cwd):
        """It loops over a folder of pdfs and attach all the pdfs into the email"""
        if pdf_folder_path != "":
            os.chdir(pdf_folder_path)
            for pdf_path in os.listdir("."):
                with open(pdf_path, "rb") as pdf:
                    pdf_data = pdf.read()
                    pdf_name = pdf.name
                self.msg.add_attachment(pdf_data, maintype='application', subtype='octet-stream', filename=pdf_name)
        os.chdir(previous_cwd)

m=EmailManager()
m.send_email(html_file_path='Email-Verification-Gmail-template.html',message="hallo",contacts=['omar.sherif9992@gmail.com'],subject="Help",first_name="Omar",last_name="Sherif")


