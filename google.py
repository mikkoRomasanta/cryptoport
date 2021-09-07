from googleapiclient.discovery import build
from google.oauth2 import service_account
import datetime
import cmc
import pancakeswap as ps
import os
from dotenv import load_dotenv


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

# result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range="tst!A1:B3").execute()
# values = result.get('values', [])
# print(values)

#--- GET QUOTES ---
quotes_cmc = cmc.get_quotes()
quotes_pancakeswap = ps.get_quotes()

quotes = quotes_cmc + quotes_pancakeswap

# print(quotes)

#--- UPDATE COINS ---
sheet.values().update(spreadsheetId=SPREADSHEET_ID,range="CMC quotes!A1",
                                    valueInputOption="USER_ENTERED", body={"values":quotes}).execute()

#--- UPDATE DATE/TIME UPDATED ---
dt = datetime.datetime.now()
dt_json = [['timestamp', dt.strftime('%Y-%m-%dT%Hh:%Mm:%Ss.%f')]]

sheet.values().update(spreadsheetId=SPREADSHEET_ID,range="CMC quotes!D1",
                                    valueInputOption="USER_ENTERED", body={"values":dt_json}).execute()
print(dt_json)