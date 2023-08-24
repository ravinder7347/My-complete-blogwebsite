from smtplib import SMTP
USER = "kumarravinder6245@gmail.com"
APP_PASSWORD = "qhzkteyxwutogvmv"

class SEND_MAIL:
    def __init__(self,username, useremail, userphone, message) -> None:
        self.username = username
        self.useremail = useremail
        self.userphone = userphone
        self.message = message
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USER, password=APP_PASSWORD)
            connection.sendmail( from_addr=self.useremail, to_addrs="pamberray0@gmail.com", msg=f"SUBJECT: Persons blog message website \n\n Name: {self.username} \n email: {self.useremail} \n phone: {self.userphone}\n message: {self.message}")
           
    # def sendmail(self):
    #     mail_bot.sendmail()
# mail_bot = SEND_MAIL('ravinder', 'bindubhatoy@gmail.com', '9465622706', 'testing sending email using blog_post website')