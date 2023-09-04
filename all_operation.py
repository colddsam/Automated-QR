from send_mail import send_mail
from barcode_generator import qr_code_generator
from gspread_connection import gspread_connection
import os

def operations():
    dataframe=gspread_connection()
    for num,email in enumerate(dataframe["Email Address"]):
        qr_code_generator(dataframe["Unique ID"][num])
        send_mail(name=dataframe["First Name"][num],receiver_email=email)
        os.remove("barcode.jpg")