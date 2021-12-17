import streamlit as st
import soala as a
import soalb as b
import soalc as c

opsi = st.sidebar.selectbox("Fitur Aplikasi", ("Produksi Minyak Mentah Tahunan Negara", "Produksi Minyak Mentah Terbesar pada Tahun Tertentu", "Produksi Minyak Mentah Kumulatif Terbesar", "Informasi Negara Tertentu serta Data Produksi Minyak Mentah"))

if opsi == "Produksi Minyak Mentah Tahunan Negara":
    a.minyak()
elif opsi == "Produksi Minyak Mentah Terbesar pada Tahun Tertentu":
    b.terbesar()
elif opsi == "Produksi Minyak Mentah Kumulatif Terbesar":
    c.kumulatif()
elif opsi == "Informasi Negara Tertentu serta Data Produksi Minyak Mentah":
    a.info_negara()
