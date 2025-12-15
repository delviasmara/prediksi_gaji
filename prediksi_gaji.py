import streamlit as st # membuat apliaksi jalan di browser
import joblib #membaca model
import numpy as np

#memuat model regresi linier yang sudah disimpan
lin_reg_loaded = joblib.load('prediksi_gaji.joblib')

#judul aplikasi
st.title("Prediksi Gaji Berdasarkan Lama Bekerja by Delvi Asmara")

#Input tahun pengalaman kerja
years_experience = st.number_input ("Masukkan jumlah tahun bekerja:", min_value=0.0, step=0.1)

#Prediksi gaji
if st.button("Prediksi Gaji"):
    gaji = lin_reg_loaded.predict([[years_experience]])
    gaji = gaji*17000
    st.write(f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah Rp{gaji[0]:,.2f}")