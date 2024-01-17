import streamlit as sl
import smtplib
import email.mime.multipart
import email.mime.text

MY_EMAIL = "mujsmtptest@gmail.com"
PASSWORD = "nyghnsnobgqdgxys"


# -----------message send function--------------
def send_mail():
    msg = email.mime.multipart.MIMEMultipart()
    msg['to'] = "Zdenal866@seznam.cz"
    msg['from'] = MY_EMAIL
    msg['subject'] = "Contact form\n\n"
    msg.add_header('reply-to', client_email)

    text_part = email.mime.text.MIMEText(message)
    msg.attach(text_part)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(msg['from'], msg['to'], msg.as_string())


sl.title("Contact me")
client_email = sl.text_input(label="Email")
message = sl.text_area(label="Message")
sl.button(label="send", on_click=send_mail)
sl.write(client_email)
sl.write(message)





