import streamlit as st
from streamlit_option_menu import option_menu
from send_email import send_email
import re
from google_sheets import GoogleSheets
import uuid

#Variables
titulo_pagina = "Club de Padel"
layout_pagina = "centered"

horas = ["10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
pistas = ["Pista 1", "Pista 2"]

document = "gestion-club-padel"
sheet = "reservas"
credentials = st.secrets["sheets"]["credentials_sheet"]


#Funciones
def validar_email(email):
    patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(patron, email):
        return True
    else:
        return False

def generate_uid():
    return str (uuid.uuid4())
    
#Cuerpo de la Página    

st.set_page_config(page_title= titulo_pagina, layout=layout_pagina)

st.image("assets/portada.jpg")
st.title("Club de Padel")
st.text ("Escazu, San Antonio")

selected = option_menu(menu_title=None,options=["Reservar","Pistas","Detalles"],
                       icons=["calendar-date","building","clipboard-minus"],
                       orientation="horizontal")

if selected == "Detalles":
    #st.image("assets/mapa_toño.png")

    st.subheader("Ubicación")
    st.markdown("""<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2336.99804580683!2d-84.13504633929176!3d9.905066945920703!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8fa0fcfa959b3f91%3A0xec3f2a55eea68f6a!2sChurch%20of%20San%20Antonio%20de%20Padua!5e0!3m2!1sen!2shn!4v1715631439224!5m2!1sen!2shn" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""", unsafe_allow_html= True)
   
    st.subheader("Horarios")
    dia,hora = st.columns(2)
 
    dia.text("Lunes")
    hora.text("10:00 - 21:00")
    dia.text("Martes")
    hora.text("10:00 - 21:00")
    dia.text("Miércoles")
    hora.text("10:00 - 21:00")
    dia.text("Jueves")
    hora.text("10:00 - 21:00")
    dia.text("Viernes")
    hora.text("10:00 - 21:00")
    dia.text("Sabado")
    hora.text("10:00 - 21:00")
    dia.text("Domingo")
    hora.text("10:00 - 21:00")

    st.subheader("Contacto")
    st.text("83413391")

    st.subheader("Instagram")
    st.text("Seguinos en Instagram")

if selected == "Pistas":

    st.write("##")
    st.image("assets/pistas_padel.jpg", caption="Esta es la pista 1")
    st.image("assets/pistas_padel.jpg", caption="Esta es la pista 2")

if selected == "Reservar":

    st.subheader("Reservar")

    c1,c2 = st.columns(2)

    nombre = c1.text_input("Nombre *",placeholder="Nombre",label_visibility="hidden")
    email = c2.text_input("Email *",placeholder="email")

    fecha= c1.date_input("fecha *")
    hora= c2.selectbox("Hora",horas)
    pista= c1.selectbox("Pistas",pistas)
    notas= c2.text_area("Notas",placeholder="notas")

    enviar=st.button("Reservar")
 #Backend
   
   
if enviar:

       with st.spinner("cargando ..."):

            if nombre == "":
                st.warning("El nombre es obligatorio")
            elif email == "":
                st.warning("el email es obligatorio") 
            elif not validar_email(email):
                st.warning ("El email no es valido")  
            else:
                #Crear evento en google calendar. 
                #Crear registro en google sheet.
                uid = generate_uid()
                data =[[nombre,email,pista,str(fecha),hora,notas, uid]]
                gs =GoogleSheets(credentials, document,sheet)
                range = gs.get_last_row_range()
                gs.write_data(range,data)
                send_email(email, nombre, fecha, hora,pista,notas)

                st.success=("Su pista ha sido reservada de forma exitosa") 



    