import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def ambil_data(tahun, b):
    data_csv = pd.read_csv('produksi_minyak_mentah.csv')
    data_negara = data_csv.loc[data_csv["tahun"] == tahun, ["kode_negara", "produksi"]]
    data_negara = data_negara.sort_values(by="produksi", axis=0, ascending=False)
    data_json = pd.read_json("kode_negara_lengkap.json")
    data_negara["cek negara"] = data_negara["kode_negara"].isin(data_json["alpha-3"])
    data_negara = data_negara.loc[data_negara["cek negara"] == True, ["kode_negara", "produksi"]]
    data_negara = data_negara.set_index("kode_negara")
    data_negara = data_negara[:b]
    return data_negara

def terbesar():
    st.title("Produksi Minyak Mentah Terbesar pada Tahun Tertentu")
    tahun = st.number_input("Tahun Produksi (1971-2015)", min_value=1971, max_value=2015, step=1)
    besar = st.number_input("Banyak negara yang ditampilkan", value=5, step=1)
    if tahun == '' or besar == '':
        st.write("Masukkan Tahun atau Besar Negara!!!")
    else:
        try:
            data = ambil_data(int(tahun), int(besar))
        except ValueError:
            st.write("Masukkan data yang benar!!!")
        else:
            try:
                data.plot(kind='bar')
            except IndexError:
                st.write("Tahun di luar jangkauan!!!")
            else:
                if int(besar) < 17:
                    plt.xticks(rotation=0)
                plt.xlabel("Kode Negara")
                plt.title(f"Produksi Minyak Terbesar pada Tahun {tahun}")
                st.pyplot(plt)

