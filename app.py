import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load('best_random_forest.pkl')

# Judul Aplikasi
st.title("🎓 Prediksi Status Mahasiswa (Graduate vs Dropout)")

# Input Form
st.subheader("Masukkan Data Mahasiswa")

marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6])
application_mode = st.selectbox("Mode Aplikasi", list(range(1, 58)))  # Sesuaikan jika perlu
previous_qualification_grade = st.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 130.0)
admission_grade = st.slider("Admission Grade", 0.0, 200.0, 125.0)
displaced = st.selectbox("Apakah Mahasiswa Tergusur?", [0, 1])
debtor = st.selectbox("Memiliki Tanggungan Utang?", [0, 1])
tuition_fees_up_to_date = st.selectbox("Biaya Kuliah Sudah Lunas?", [0, 1])
gender = st.selectbox("Gender", ["Female", "Male"])
scholarship_holder = st.selectbox("Memiliki Beasiswa?", [0, 1])
age_at_enrollment = st.slider("Umur Saat Masuk Kuliah", 17, 70, 20)

curr_1st_enrolled = st.slider("Mata Kuliah 1st Semester Diambil", 0, 30, 6)
curr_1st_approved = st.slider("Mata Kuliah 1st Semester Lulus", 0, 30, 5)
curr_1st_grade = st.slider("Nilai Rata-rata 1st Semester", 0.0, 20.0, 12.0)

curr_2nd_enrolled = st.slider("Mata Kuliah 2nd Semester Diambil", 0, 30, 6)
curr_2nd_eval = st.slider("Evaluasi 2nd Semester", 0, 30, 7)
curr_2nd_approved = st.slider("Mata Kuliah 2nd Semester Lulus", 0, 30, 5)
curr_2nd_grade = st.slider("Nilai Rata-rata 2nd Semester", 0.0, 20.0, 12.0)
curr_2nd_wo_eval = st.slider("2nd Sem Tanpa Evaluasi", 0, 30, 0)

# Jika tombol ditekan
if st.button("🔍 Prediksi Status"):
    # Mapping gender
    gender_value = 1 if gender == 'Male' else 0

    input_dict = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Previous_qualification_grade': previous_qualification_grade,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Gender': gender_value,
        'Scholarship_holder': scholarship_holder,
        'Age_at_enrollment': age_at_enrollment,
        'Curricular_units_1st_sem_enrolled': curr_1st_enrolled,
        'Curricular_units_1st_sem_approved': curr_1st_approved,
        'Curricular_units_1st_sem_grade': curr_1st_grade,
        'Curricular_units_2nd_sem_enrolled': curr_2nd_enrolled,
        'Curricular_units_2nd_sem_evaluations': curr_2nd_eval,
        'Curricular_units_2nd_sem_approved': curr_2nd_approved,
        'Curricular_units_2nd_sem_grade': curr_2nd_grade,
        'Curricular_units_2nd_sem_without_evaluations': curr_2nd_wo_eval
    }

    input_df = pd.DataFrame([input_dict])

    # Prediksi
    prediction = model.predict(input_df)[0]
    label = "🎓 Graduate" if prediction == 1 else "❌ Dropout"

    st.success(f"Hasil Prediksi: {label}")