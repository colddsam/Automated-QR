import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from unique_id_generator import unique_id_generator

def gspread_connection():
    scopes=[
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds=ServiceAccountCredentials.from_json_keyfile_name('secret_key.json',scopes=scopes)

    file=gspread.authorize(creds)
    workbook=file.open("Event Registration form")
    sheet=workbook.sheet1

    dataframe = pd.DataFrame(sheet.get_all_records())
    dataframe["Unique ID"]=""
    dataframe["Unique ID"]=dataframe["Unique ID"].apply(unique_id_generator)
    return dataframe
    