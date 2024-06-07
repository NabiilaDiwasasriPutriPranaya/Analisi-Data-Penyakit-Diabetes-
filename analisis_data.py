import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data dari CSV
df_patient_info = pd.read_csv("diabetes_patient_info.csv")
df_medical_records = pd.read_csv("diabetes_medical_records.csv")
df_lifestyle_info = pd.read_csv("diabetes_lifestyle_info.csv")

# Menggabungkan tabel berdasarkan Patient_ID
df_combined = pd.merge(df_patient_info, df_medical_records, on="Patient_ID")
df_combined = pd.merge(df_combined, df_lifestyle_info, on="Patient_ID")

# Setting style and color palette
sns.set(style="whitegrid")
color_palette = sns.color_palette("husl", 8)  # Using 'husl' color palette for vibrant colors

# Analisis Distribusi Usia
plt.figure(figsize=(10, 6))
sns.histplot(df_combined['Age'], kde=True, bins=10, color=color_palette[0])
plt.title('Distribusi Usia Pasien', fontsize=16)
plt.xlabel('Usia', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

# Analisis Distribusi BMI
plt.figure(figsize=(10, 6))
sns.histplot(df_combined['BMI'], kde=True, bins=10, color=color_palette[1])
plt.title('Distribusi BMI Pasien', fontsize=16)
plt.xlabel('BMI', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

# Analisis Distribusi Gula Darah Puasa
plt.figure(figsize=(10, 6))
sns.histplot(df_combined['Fasting_Blood_Sugar'], kde=True, bins=10, color=color_palette[2])
plt.title('Distribusi Gula Darah Puasa Pasien', fontsize=16)
plt.xlabel('Fasting Blood Sugar', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

# Korelasi antara faktor-faktor
correlation_matrix = df_combined[['Age', 'BMI', 'Fasting_Blood_Sugar', 'HbA1c', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic', 'Cholesterol']].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title('Matriks Korelasi', fontsize=16)
plt.show()

# Analisis berdasarkan Gaya Hidup
plt.figure(figsize=(10, 6))
sns.boxplot(x='Physical_Activity_Level', y='Fasting_Blood_Sugar', data=df_combined, palette="Set2")
plt.title('Level Gula Darah Puasa berdasarkan Aktivitas Fisik', fontsize=16)
plt.xlabel('Level Aktivitas Fisik', fontsize=14)
plt.ylabel('Fasting Blood Sugar', fontsize=14)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Diet_Type', y='BMI', data=df_combined, palette="Set3")
plt.title('BMI berdasarkan Jenis Diet', fontsize=16)
plt.xlabel('Jenis Diet', fontsize=14)
plt.ylabel('BMI', fontsize=14)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Alcohol_Consumption', y='HbA1c', data=df_combined, palette="Set1")
plt.title('HbA1c berdasarkan Konsumsi Alkohol', fontsize=16)
plt.xlabel('Konsumsi Alkohol', fontsize=14)
plt.ylabel('HbA1c', fontsize=14)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Stress_Level', y='Blood_Pressure_Systolic', data=df_combined, palette="Paired")
plt.title('Tekanan Darah Sistolik berdasarkan Level Stres', fontsize=16)
plt.xlabel('Level Stres', fontsize=14)
plt.ylabel('Blood Pressure Systolic', fontsize=14)
plt.show()
