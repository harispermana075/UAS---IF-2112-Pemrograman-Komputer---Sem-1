import streamlit as st
import soala as a
import soalb as b
import soalc as c

opsi = st.sidebar.selectbox("Fitur Aplikasi", ("Produksi Minyak Mentah Tahunan Negara", "Produksi Terbesar pada Tahun Tertentu", "Produksi Minyak Mentah Kumulatif", "Informasi Negara"))

if opsi == "Produksi Minyak Mentah Tahunan Negara":
    a.minyak()
elif opsi == "Produksi Terbesar pada Tahun Tertentu":
    b.terbesar()
elif opsi == "Produksi Minyak Mentah Kumulatif":
    c.kumulatif()
elif opsi == "Informasi Negara":
    a.info_negara()
