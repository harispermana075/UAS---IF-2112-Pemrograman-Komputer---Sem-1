import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def sum_data(b):
    data_csv = pd.read_csv("produksi_minyak_mentah.csv")
    data_json = pd.read_json("kode_negara_lengkap.json")
    data_negara = data_csv.drop(columns="tahun")
    data_negara["cek_negara"] = data_negara["kode_negara"].isin(data_json["alpha-3"])
    data_negara = data_negara.loc[data_negara["cek_negara"] == True, ["kode_negara","produksi"]]
    data_negara = data_negara.groupby("kode_negara")["produksi"].sum().reset_index()
    data_negara = data_negara.sort_values(by="produksi", ascending=False)
    data_negara = data_negara.set_index("kode_negara")
    data_negara = data_negara[:b]
    return data_negara

def kumulatif():
    st.title("Produksi Minyak Kumulatif Terbesar")
    besar = st.number_input("Masukkan banyak negara yang akan ditampilkan", value=5, step=1)
    if besar <= 0:
        st.write("Masukkan angka diatas 0")
    else:
        data = sum_data(int(besar))
        data.plot(kind="bar")
        if besar < 17:
            plt.xticks(rotation=0)
        plt.xlabel("Kode Negara")
        st.pyplot(plt)