import streamlit as st
from PIL import Image
import soala as a
import soalb as b
import soalc as c

gambar = Image.open('logo.png')
st.sidebar.image(gambar)
opsi = st.sidebar.selectbox("Fitur Aplikasi", ("Produksi Minyak Mentah Tahunan", "Produksi Terbesar pada Tahun Tertentu", "Produksi Minyak Mentah Kumulatif", "Informasi Negara"))

if opsi == "Produksi Minyak Mentah Tahunan":
    a.minyak()
elif opsi == "Produksi Terbesar pada Tahun Tertentu":
    b.terbesar()
elif opsi == "Produksi Minyak Mentah Kumulatif":
    c.kumulatif()
elif opsi == "Informasi Negara":
    a.info_negara()
