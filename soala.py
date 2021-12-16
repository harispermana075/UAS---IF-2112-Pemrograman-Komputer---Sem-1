import streamlit as st
import pandas as pd
import numpy as np
import json

def search_data(negara):
    file_json = open('kode_negara_lengkap.json')
    indexnegara = json.loads(file_json.read())
    file_json.close()

    for x in range(len(indexnegara)):
        if negara.lower() == indexnegara[x]["name"].lower():
            return x
    raise KeyError

def ambil_data(kode):
    data_csv = pd.read_csv('produksi_minyak_mentah.csv')
    data_csv.set_index("kode_negara", inplace=True)
    data_negara = data_csv.loc[kode, ["tahun", "produksi"]]
    data_negara.set_index("tahun", inplace=True)
    return data_negara

def minyak_tahun():
    file_json = open('kode_negara_lengkap.json')
    file_json = json.loads(file_json.read())
    list_negara = list()
    for x in range(len(file_json)):
        list_negara.append(file_json[x]['name'])
    st.title('Informasi Negara')   
    nama_negara = st.selectbox('Negara', list_negara)
    try:
        no_country = search_data(nama_negara)
    except KeyError:
        st.write("Negara tidak ditemukan!!!")
    else:
        st.header('Informasi Negara')
        st.write('Nama Negara: %s' % (file_json[no_country]['name']))
        st.write('Kode alpha-2: %s' % (file_json[no_country]['alpha-2']))
        st.write('Kode alpha-3: %s' % (file_json[no_country]['alpha-3']))
        st.write('Kode negara: %s' % (file_json[no_country]['country-code']))
        st.write('Region: %s' % (file_json[no_country]['region']))
        st.write('Sub-Region: %s' % (file_json[no_country]['sub-region']))
        try:
            data_raw = ambil_data(file_json[no_country]['alpha-3'])
        except KeyError:
            st.write('Negara tidak memiliki produksi minyak')
        else:
            data = data_raw.loc[data_raw['produksi'] > 0, 'produksi']
            if data.empty:
                st.write('Negara tidak memiliki produksi minyak')
            else:
                st.header('Produksi Minyak')
                data = data.sort_values(ascending=False)
                terbesar = data.head().index.values[0]
                terkecil = data.tail().index.values[len(data.tail().index)-1]
                data0 = data_raw.loc[data_raw['produksi'] == 0, 'produksi']
                st.write(f'Produksi terbesar pada tahun: {terbesar}')
                st.write(f'Produksi terkecil pada tahun: {terkecil}')
                if data0.empty:
                    st.write('Produksi sama dengan nol pada tahun: -')
                elif len(data0) == 1:
                    nol = data0.head().index.values[0]
                    st.write(f'Produksi sama dengan nol pada tahun: {nol}')
                else:
                    tahunnol = list()
                    for x in range(len(data0)):
                        tahunnol.append(data0.index.values[x])
                    tahunnol = str(tahunnol)[1:-1]
                    st.write(f'Produksi sama dengan nol pada tahun: {tahunnol}')
                kumulatif = data_raw['produksi'].sum()
                st.write(f'Jumlah produksi kumulatif: {kumulatif:.2f}')
                median = data_raw['produksi'].median()
                rata = data_raw['produksi'].mean()
                lower_q = np.percentile(data_raw['produksi'], 25)
                upper_q = np.percentile(data_raw['produksi'], 75)
                st.write(f'Rata-rata data: {rata:.2f}')
                st.write(f'Median data: {median:.2f}')            
                st.write(f'Kuartil bawah: {lower_q:.2f}')
                st.write(f'Kuartil atas: {upper_q:.2f}')

def minyak():
    file_json = open('kode_negara_lengkap.json')
    file_json = json.loads(file_json.read())
    list_negara = list()
    for x in range(len(file_json)):
        list_negara.append(file_json[x]['name'])
    st.title('Produksi Minyak Negara dalam Tahun')   
    nama_negara = st.selectbox('Negara', list_negara)
    try:
        no_country = search_data(nama_negara)
    except KeyError:
        st.write("Negara tidak ditemukan!!!")
    else:
        try:
            data_raw = ambil_data(file_json[no_country]['alpha-3'])
        except KeyError:
            st.write('Negara tidak memiliki produksi minyak')
        else:
            data = data_raw.loc[data_raw['produksi'] > 0, 'produksi']
            if data.empty:
                st.write('Negara tidak memiliki produksi minyak')
            else:
                st.header(f'Produksi Minyak Negara {nama_negara}')
                st.bar_chart(data_raw)