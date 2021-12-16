import streamlit as st
import soala as a
import soalb as b
import soalc as c

opsi = st.sidebar.selectbox("Fitur Aplikasi", ("Jumlah Produksi Terhadap Tahun", "Jumlah Produksi Terbesar pada Tahun", "Jumlah Produksi Secara Kumulatif", "Informasi Negara"))

if opsi == "Jumlah Produksi Terhadap Tahun":
    a.minyak()
elif opsi == "Jumlah Produksi Terbesar pada Tahun":
    b.terbesar()
elif opsi == "Jumlah Produksi Secara Kumulatif":
    c.kumulatif()
elif opsi == "Informasi Negara":
    a.minyak_tahun()
