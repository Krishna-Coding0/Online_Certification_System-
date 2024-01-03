import smtplib
import ssl
import random
from email.message import EmailMessage



def accept_student(email,no,name):
    otp=None
    if no==0:
        subject="Not Registered "
        body=f"Sorry Mr. {name} You Are Not Accepted Please COntact You Department"
    elif no==1:
        subject="Registered "
        body=f"Congratulation Mr. {name} You Are Accepted You Can Login Now"
    else:
        otp=random_no(no)
        subject="Verification OTP"
        body=f"Hello Mr. {name} Please Go TO Site and Enter OTP for email Varifiaction: {otp}"
        

    sender_email="bekarkam200@gmail.com"
    reciver_email=email
    password="krishna100"

    message=EmailMessage()
    message["From"]=sender_email
    message["To"]=reciver_email
    message["Subject"]=subject

    message.set_content(body)
    context=ssl.create_default_context()

    print("sending Email")

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,reciver_email,message.as_string())

    print("Done Sending Email")
    return otp


def random_no(no):
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number="0123456789"
    symbol="@#$%&?"
    lenght=6
    all=lower+upper+number+symbol
    otp="".join(random.sample(all,lenght))
    return otp