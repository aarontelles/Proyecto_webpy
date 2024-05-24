#Script para manejar el calendario de Google
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import streamlit as st
from datetime import datetime

class GoogleCalendar:
    def __init__(self, credentials, idcalendar):
        self.credentials = credentials
        self.idcalendar = idcalendar
        self.service = build('calendar', 'v3',
                              credentials= service_account.Credentials.from_service_account_info(
                                  self.credentials, scopes = ['https://www.googleapis.com/auth/calendar'])
                              )
def create_event (self, name_event, start_time, end_time, timezone, attendes = None):

    event = {
        'summary': name_event,
        'start': {
            'DateTime': start_time,
            'TimeZone': timezone, 
        },

        'end': {
            'DateTime': start_time,
            'TimeZone': timezone, 
        },

    }

    if attendes: 
        event['attendes']= [{"email:": email} for email in attendes]

    try:
        created_event = self.service.events().insert(calendarId= self.idcalendar,body = event).execute()
    except HttpError as error:
        raise Exception(f"An error as ocurred:{error}")
    
    return created_event

def get_events_star_time(self,date):
    events= self.get_events(date)
    star_time=[]

    for event in events:
        star_time = event['start']['dateTime']




credentials = st.secrets["sheets"]["credentials_sheet"]
idcalendar = "atelles@gbm.net"
google = GoogleCalendar(credentials,idcalendar )
start_date = '2024-05-20T10 : 00+02:00'
end_date = '2024-05-20T14 : 00+02:00'
time_zone = 'America/Costa Rica'
attendes = ''
idevent = google.create_event("Partido de padel",start_date,end_date,time_zone,attendes)
print(idevent)


#start_date = ' 
#google.create_event("partido de padel","")


    