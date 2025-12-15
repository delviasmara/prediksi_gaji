import streamlit as st
import joblib
import numpy as np
import pandas as pd
from io import BytesIO

# ===============================
# Load model regresi
# ===============================
lin_reg_loaded = joblib.load('prediksi_gaji.joblib')

# ===============================
# Judul aplikasi
# ===============================
st.title("Prediksi Gaji Berdasarkan Lama Bekerja")
st.write("Aplikasi Prediksi Gaji Menggunakan Regresi Linier")

# ===============================
# 1. Prediksi Manual
# ===============================
st.subheader("🔹 Prediksi Gaji Manual")

years_experience = st.number_input(
    "Masukkan jumlah tahun bekerja:",
    min_value=0.0,
    step=0.1
)

if st.button("Prediksi Gaji"):
    gaji = lin_reg_loaded.predict([[years_experience]])
    gaji = gaji * 17000
    st.success(
        f"Gaji setelah bekerja {years_experience} tahun adalah "
        f"Rp {gaji[0]:,.2f}"
    )

# ===============================
# 2. Upload File Excel
# ===============================
st.subheader("🔹 Prediksi Gaji dari File Excel")

uploaded_file = st.file_uploader(
    "Upload file Excel (.xlsx)",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.write("📄 Data yang di-upload:")
    st.dataframe(df)

    # Validasi kolom
    if "years_experience" not in df.columns:
        st.error("File Excel harus memiliki kolom 'years_experience'")
    else:
        # Prediksi
        prediksi = lin_reg_loaded.predict(df[["years_experience"]])
        df["prediksi_gaji"] = prediksi * 17000

        st.write("📊 Hasil Prediksi:")
        st.dataframe(df)

        # ===============================
        # 3. Download Hasil Excel
        # ===============================
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Hasil Prediksi")

        st.download_button(
            label="⬇️ Download Hasil Prediksi (Excel)",
            data=output.getvalue(),
            file_name="hasil_prediksi_gaji.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
