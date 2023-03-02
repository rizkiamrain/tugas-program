import pickle
from pathlib import Path
from PIL import Image
from streamlit_option_menu import option_menu
from st_functions import st_button, load_css
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="program rizki amrain", page_icon=":bar_chart:", layout="wide")


# --- USER AUTHENTICATION ---
names = ["Rizki Amrain", "Salsabillah"]
usernames = ["rizki", "bila"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.sidebar.header("Pilih Menu :")
    
    with st.sidebar:
        selected = option_menu('MOH. RIZKI AMRAIN',
        ['Home',
        'Menghitung Gaji Karyawan',
        'Menu Menghitung Matematika',
        'Menghitung Harga Jual Tanah'],
        default_index=0)

    if (selected == 'Home'):
        load_css()
        col1, col2, col3 = st.columns(3)
        col2.image(Image.open('ra1.png'))

        st.header('Mohamad Rizki Amrain')

        st.info('Mahasiswa Universitas Ichsan Gorontalo')

        icon_size = 20

        st_button('youtube', 'https://www.youtube.com/@hellobiwa', 'Hello Biwa Youtube Channel', icon_size)
        st_button('youtube', 'https://www.youtube.com/@rizkiamrain9560', 'Rizki Amrain Youtube Channel', icon_size)
        st_button('facebook', 'https://www.facebook.com/rizki.amrain26', 'Mohamad Rizki Amrain Facebook', icon_size)
        st_button('twitter', 'https://twitter.com/mohamadrizki26', 'Mohamad Rizki Amrain Twitter', icon_size)
        st_button('instagram','https://instagram.com/rizkiamrain_', 'Mohamad Rizki Amrain Instagram', icon_size)
    # halaman hitung gaji karyawan
    if (selected == 'Menghitung Gaji Karyawan'):
        st.title(':blue[MENGHITUNG GAJI KARYAWAN]')

        namakr = st.text_input("Masukan Nama Karyawan",)
        gol = st.selectbox("Masukan Golongan", [' ','A','B','C'] )
        jamkerja = st.number_input("Masukan Total Jam Kerja",)
        hitung = st.button("Hitung Gaji")

        if hitung:
            if (gol =='A'):
                gapok = 500000
                if (jamkerja>6):
                    tunjangan = 0.1*gapok
                else:
                    tunjangan = 0
            elif(gol == 'B'):
                gapok = 700000
                if (jamkerja>7):
                    tunjangan = 0.15*gapok
                else:
                    tunjangan = 0
            elif(gol=='C'):
                gapok = 900000
                if (jamkerja>8):
                    tunjangan = 0.2*gapok
                else:
                    tunjangan=0


            totalgaji = gapok+tunjangan

            st.write("GAJI KARYAWAN : ")
            st.write('Nama Karyawan = ',namakr)
            st.write('Golongan = ',gol)
            st.write('Total Jam kerja = ',jamkerja)
            st.write('Tunjangan       = Rp.',tunjangan)
            st.write('Total Gaji      = Rp.',totalgaji)

    if (selected == 'Menghitung Harga Jual Tanah'):
        st.title(':orange[MENGHITUNG HARGA JUAL TANAH]')
        panjangA = st.number_input('Panjang Bidang A')
        lebarA = st.number_input('Lebar A')
        panjangB = st.number_input('Panjang Bidang B')
        lebarB = st.number_input('Lebar B')
        hitung = st.button("Hitung Luas Tanah")

        if hitung:
            luasA = panjangA*lebarA
            luasB = panjangB*lebarB
            st.write('Total Luas A =',luasA)
            st.write('Total Luas B =',luasB)

            totalluas=luasA+luasB
            hargajual=totalluas*200000

            st.write('Total Luas Tanah =   ',totalluas)
            st.write('Harga Jual Tanah = Rp.',hargajual)
            st.success(f"Harga Jual Tanah = Rp.{hargajual}")



    if (selected == 'Menu Menghitung Matematika'):
        st.title(':red[MENU MENGHITUNG MATEMATIKA]')

        pilih = st.selectbox("Pilihan Operator", ['Tambah','Kurang','Kali','Bagi','Pangkat','Modulus'])
        nilai1 = st.slider("Masukan Nilai 1",0,100)
        nilai2 = st.slider("Masukan Nilai 2",0,100)
        hitung = st.button("Hitung")

        if hitung:
            if (pilih=="Tambah"):
                hasil=nilai1+nilai2
            elif(pilih=="Kurang"):
                hasil=nilai1-nilai2
            elif(pilih=="Kali"):
                hasil=nilai1*nilai2
            elif(pilih=="Bagi"):
                hasil=nilai1/nilai2
            elif(pilih=="Pangkat"):
                hasil=nilai1**nilai2
            elif(pilih=="Modulus"):
                hasil=nilai1%nilai2

            st.write("Hasil Dari",nilai1,pilih,nilai2,"=", hasil)
            st.success(f"Hasil Akhir = {hasil}")
