# Analisi Data Penyakit Diabetes
# DISKRIPSI
Proyek ini bertujuan untuk menganalisis data terkait diabetes dari dataset pasien. Analisis ini mencakup visualisasi distribusi demografis, korelasi antar variabel medis, serta hubungan antara faktor gaya hidup dan indikator medis.
# Langkah-Langkah
## Setup dan Persiapan Data
1. **Memuat Data**: Skrip ini memulai dengan memuat data dari tiga file CSV:
   - `diabetes_patient_info.csv`: Informasi dasar pasien seperti usia, jenis kelamin, BMI, dan riwayat keluarga.
     Here is the data in a table format:

    | Patient_ID | Age | Gender | BMI | Family_History | Smoker |
    | --- | --- | --- | --- | --- | --- |
    | 1 | 76 | Female | 37.5 | No | Yes |
    | 2 | 18 | Female | 23.9 | No | No |
    | 3 | 40 | Male | 33.1 | No | Yes |
    | 4 | 34 | Male | 35.9 | No | Yes |
    | 5 | 60 | Female | 27.8 | No | Yes |
    | 6 | 54 | Male | 34.7 | Yes | Yes |
    | 7 | 48 | Female | 36.3 | Yes | No |
    | 8 | 42 | Male | 26.6 | No | Yes |
    | 9 | 70 | Female | 20.6 | No | Yes |
    | 10 | 21 | Male | 24.0 | No | No |
    | 11 | 69 | Male | 31.2 | No | No |
    | 12 | 26 | Male | 28.7 | No | Yes |
    | 13 | 74 | Male | 29.0 | No | Yes |
    | 14 | 45 | Female | 28.4 | No | No |
    | 15 | 47 | Female | 29.8 | No | Yes |
    | 16 | 77 | Male | 28.0 | Yes | No |
    | 17 | 64 | Female | 36.8 | Yes | Yes |
    | 18 | 41 | Male | 27.8 | Yes | No |
    | 19 | 50 | Female | 36.3 | No | Yes |
    | 20 | 37 | Female | 29.5 | No | No |
    | 21 | 26 | Male | 20.4 | No | No |
    | 22 | 25 | Female | 32.7 | No | No |
    | 23 | 41 | Male | 22.9 | Yes | Yes |
    | 24 | 31 | Male | 36.7 | Yes | No |
    | 25 | 76 | Male | 33.1 | No | Yes |
    | 26 | 35 | Male | 22.3 | Yes | No |
    | 27 | 74 | Male | 20.0 | No | No |
    | 28 | 70 | Female | 18.7 | No | Yes |
    | 29 | 73 | Female | 37.7 | No | Yes |
    | 30 | 18 | Male | 21.4 | No | Yes |
    | 31 | 29 | Male | 35.3 | No | No |
    | 32 | 46 | Male | 38.4 | Yes | No |
    | 33 | 54 | Male | 33.9 | Yes | Yes |
    | 34 | 43 | Female | 29.1 | Yes | Yes |
    | 35 | 50 | Female | 28.6 | Yes | Yes |
    | 36 | 60 | Male | 37.5 | No | Yes |
    | 37 | 32 | Male | 29.0 | Yes | Yes |
    | 38 | 40 | Female | 27.4 | Yes | Yes |
    | 39 | 46 | Male | 22.2 | Yes | No |
    | 40 | 38 | Female | 28.7 | Yes | Yes |
    | 41 | 36 | Female | 35.3 | No | Yes |
    | 42 | 22 | Female | 30.5 | No | Yes |
    | 43 | 40 | Female | 21.9 | No | Yes |
    | 44 | 53 | Female | 21.6 | No | No |
    | 45 | 76 | Female | 32.5 | No | Yes |
    | 46 | 37 | Female | 30.1 | Yes | Yes |
    | 47 | 25 | Female | 25.5 | No | Yes |
    | 48 | 26 | Female | 21.7 | Yes | No |
    | 49 | 79 | Female | 21.9 | Yes | No |
    | 50 | 31 | Female | 21.3 | No | Yes |
    | 51 | 23 | Male | 30.9 | No | No |
    | 52 | 18 | Male | 20.5 | No | Yes |
    | 53 | 26 | Female | 38.1 | No | Yes |
    | 54 | 33 | Female | 20.3 | No | Yes |
    | 55 | 33 | Female | 35.7 | Yes | No |
    | 56 | 71 | Female | 37.4 | Yes | Yes |
    | 57 | 29 | Male | 20.5 | No | Yes |
    | 58 | 22 | Male | 27.7 | Yes | Yes |
    | 59 | 57 | Female | 28.7 | Yes | No |
    | 60 | 46 | Male | 31.0 | No | No |
    | 61 | 63 | Male | 33.9 | No | No |
    | 62 | 44 | Female | 19.1 | No | Yes |
    | 63 | 28 | Male | 34.2 | Yes | Yes |
    | 64 | 70 | Female | 35.0 | Yes | No |
    | 65 | 64 | Male | 18.7 | No | Yes |
    | 66 | 67 | Female | 25.1 | No | No |
    | 67 | 45 | Male | 23.5 | Yes | No |
    | 68 | 69 | Male | 29.3 | Yes | Yes |
    | 69 | 53 | Female | 39.0 | Yes | Yes |
    | 70 | 59 | Male | 30.5 | No | Yes |
    | 71 | 36 | Male | 20.6 | No | Yes |
    | 72 | 71 | Male | 31.9 | Yes | Yes |
    | 73 | 52 | Male | 37.1 | No | Yes |
    | 74 | 69 | Male | 21.9 | Yes | Yes |
    | 75 | 48 | Female | 39.8 | No | Yes |
    | 76 | 71 | Male | 20.3 | Yes | No |
    | 77 | 76 | Female | 20.5 | No | Yes |
    | 78 | 61 | Male | 32.1 | No | No |
    | 79 | 73 | Male | 38.9 | No | Yes |
    | 80 | 78 | Female | 38.6 | No | No |
    | 81 | 78 | Female | 28.1 | Yes | Yes |
    | 82 | 36 | Female | 34.1 | Yes | Yes |
    | 83 | 63 | Female | 34.5 | Yes | Yes |
    | 84 | 41 | Male | 25.1 | No | No |
    | 85 | 19 | Male | 21.1 | No | Yes |
    | 86 | 24 | Female | 28.0 | No | No |
    | 87 | 60 | Male | 26.9 | No | No |
    | 88 | 71 | Female | 29.9 | Yes | Yes |
    | 89 | 66 | Female | 36.7 | Yes | Yes |
    | 90 | 48 | Female | 30.0 | Yes | Yes |
    | 91 | 77 | Female | 33.1 | Yes | No |
    | 92 | 34 | Male | 31.6 | Yes | Yes |
    | 93 | 44 | Male | 20.6 | Yes | No |
    | 94 | 78 | Female | 20.5 | No | No |
    | 95 | 53 | Male | 19.7 | No | No |
    | 96 | 76 | Male | 20.4 | Yes | Yes |
    | 97 | 67 | Female | 23.6 | No | No |
    | 98 | 60 | Female | 36.5 | Yes | Yes |
    | 99 | 27 | Female | 29.7 | Yes | Yes |
    | 100 | 62 | Male | 29.5 | No | Yes |

   - `diabetes_medical_records.csv`: Rekam medis seperti gula darah puasa, HbA1c, tekanan darah, dan kolesterol.
     Here is the data in a table format:
   
    | Patient_ID | Age | Gender | BMI | Family_History | Smoker |
    | --- | --- | --- | --- | --- | --- |
    | 1 | 76 | Female | 37.5 | No | Yes |
    | 2 | 18 | Female | 23.9 | No | No |
    | 3 | 40 | Male | 33.1 | No | Yes |
    | 4 | 34 | Male | 35.9 | No | Yes |
    | 5 | 60 | Female | 27.8 | No | Yes |
    | 6 | 54 | Male | 34.7 | Yes | Yes |
    | 7 | 48 | Female | 36.3 | Yes | No |
    | 8 | 42 | Male | 26.6 | No | Yes |
    | 9 | 70 | Female | 20.6 | No | Yes |
    | 10 | 21 | Male | 24.0 | No | No |
    | 11 | 69 | Male | 31.2 | No | No |
    | 12 | 26 | Male | 28.7 | No | Yes |
    | 13 | 74 | Male | 29.0 | No | Yes |
    | 14 | 45 | Female | 28.4 | No | No |
    | 15 | 47 | Female | 29.8 | No | Yes |
    | 16 | 77 | Male | 28.0 | Yes | No |
    | 17 | 64 | Female | 36.8 | Yes | Yes |
    | 18 | 41 | Male | 27.8 | Yes | No |
    | 19 | 50 | Female | 36.3 | No | Yes |
    | 20 | 37 | Female | 29.5 | No | No |
    | 21 | 26 | Male | 20.4 | No | No |
    | 22 | 25 | Female | 32.7 | No | No |
    | 23 | 41 | Male | 22.9 | Yes | Yes |
    | 24 | 31 | Male | 36.7 | Yes | No |
    | 25 | 76 | Male | 33.1 | No | Yes |
    | 26 | 35 | Male | 22.3 | Yes | No |
    | 27 | 74 | Male | 20.0 | No | No |
    | 28 | 70 | Female | 18.7 | No | Yes |
    | 29 | 73 | Female | 37.7 | No | Yes |
    | 30 | 18 | Male | 21.4 | No | Yes |
    | 31 | 29 | Male | 35.3 | No | No |
    | 32 | 46 | Male | 38.4 | Yes | No |
    | 33 | 54 | Male | 33.9 | Yes | Yes |
    | 34 | 43 | Female | 29.1 | Yes | Yes |
    | 35 | 50 | Female | 28.6 | Yes | Yes |
    | 36 | 60 | Male | 37.5 | No | Yes |
    | 37 | 32 | Male | 29.0 | Yes | Yes |
    | 38 | 40 | Female | 27.4 | Yes | Yes |
    | 39 | 46 | Male | 22.2 | Yes | No |
    | 40 | 38 | Female | 28.7 | Yes | Yes |
    | 41 | 36 | Female | 35.3 | No | Yes |
    | 42 | 22 | Female | 30.5 | No | Yes |
    | 43 | 40 | Female | 21.9 | No | Yes |
    | 44 | 53 | Female | 21.6 | No | No |
    | 45 | 76 | Female | 32.5 | No | Yes |
    | 46 | 37 | Female | 30.1 | Yes | Yes |
    | 47 | 25 | Female | 25.5 | No | Yes |
    | 48 | 26 | Female | 21.7 | Yes | No |
    | 49 | 79 | Female | 21.9 | Yes | No |
    | 50 | 31 | Female | 21.3 | No | Yes |
    | 51 | 23 | Male | 30.9 | No | No |
    | 52 | 18 | Male | 20.5 | No | Yes |
    | 53 | 26 | Female | 38.1 | No | Yes |
    | 54 | 33 | Female | 20.3 | No | Yes |
    | 55 | 33 | Female | 35.7 | Yes | No |
    | 56 | 71 | Female | 37.4 | Yes | Yes |
    | 57 | 29 | Male | 20.5 | No | Yes |
    | 58 | 22 | Male | 27.7 | Yes | Yes |
    | 59 | 57 | Female | 28.7 | Yes | No |
    | 60 | 46 | Male | 31.0 | No | No |
    | 61 | 63 | Male | 33.9 | No | No |
    | 62 | 44 | Female | 19.1 | No | Yes |
    | 63 | 28 | Male | 34.2 | Yes | Yes |
    | 64 | 70 | Female | 35.0 | Yes | No |
    | 65 | 64 | Male | 18.7 | No | Yes |
    | 66 | 67 | Female | 25.1 | No | No |
    | 67 | 45 | Male | 23.5 | Yes | No |
    | 68 | 69 | Male | 29.3 | Yes | Yes |
    | 69 | 53 | Female | 39.0 | Yes | Yes |
    | 70 | 59 | Male | 30.5 | No | Yes |
    | 71 | 36 | Male | 20.6 | No | Yes |
    | 72 | 71 | Male | 31.9 | Yes | Yes |
    | 73 | 52 | Male | 37.1 | No | Yes |
    | 74 | 69 | Male | 21.9 | Yes | Yes |
    | 75 | 48 | Female | 39.8 | No | Yes |
    | 76 | 71 | Male | 20.3 | Yes | No |
    | 77 | 76 | Female | 20.5 | No | Yes |
    | 78 | 61 | Male | 32.1 | No | No |
    | 79 | 73 | Male | 38.9 | No | Yes |
    | 80 | 78 | Female | 38.6 | No | No |
    | 81 | 78 | Female | 28.1 | Yes | Yes |
    | 82 | 36 | Female | 34.1 | Yes | Yes |
    | 83 | 63 | Female | 34.5 | Yes | Yes |
    | 84 | 41 | Male | 25.1 | No | No |
    | 85 | 19 | Male | 21.1 | No | Yes |
    | 86 | 24 | Female | 28.0 | No | No |
    | 87 | 60 | Male | 26.9 | No | No |
    | 88 | 71 | Female | 29.9 | Yes | Yes |
    | 89 | 66 | Female | 36.7 | Yes | Yes |
    | 90 | 48 | Female | 30.0 | Yes | Yes |
    | 91 | 77 | Female | 33.1 | Yes | No |
    | 92 | 34 | Male | 31.6 | Yes | Yes |
    | 93 | 44 | Male | 20.6 | Yes | No |
    | 94 | 78 | Female | 20.5 | No | No |
    | 95 | 53 | Male | 19.7 | No | No |
    | 96 | 76 | Male | 20.4 | Yes | Yes |
    | 97 | 67 | Female | 23.6 | No | No |
    | 98 | 60 | Female | 36.5 | Yes | Yes |
    | 99 | 27 | Female | 29.7 | Yes | Yes |
    | 100 | 62 | Male | 29.5 | No | Yes |
   - `diabetes_lifestyle_info.csv`: Informasi gaya hidup termasuk tingkat aktivitas fisik, jenis diet, konsumsi alkohol, dan tingkat stres.
     
    | ID | Sugar Level | Fat Level | Sugar Content | Fat Content |
    | --- | --- | --- | --- | --- |
    | 1 | Moderate | High | None | High |
    | 2 | Low | High | High | Moderate |
    | 3 | Moderate | Vegetarian | Low | Moderate |
    | 4 | High | High | Moderate | Low |
    | 5 | Low | High | Moderate | Low |
    | 6 | Low | High | None | Low |
    | 7 | Low | Vegetarian | None | High |
    | 8 | Low | High | Low | High |
    | 9 | Low | High | None | High |
    | 10 | Low | Balanced | Moderate | High |
    | 11 | High | High | Low | High |
    | 12 | Low | High | High | High |
    | 13 | Low | High | High | Moderate |
    | 14 | High | High | Low | Moderate |
    | 15 | Low | High | None | Low |
    | 16 | Low | High | Moderate | High |
    | 17 | High | Balanced | Low | Moderate |
    | 18 | Low | High | Low | Low |
    | 19 | Low | High | None | Low |
    | 20 | High | Vegetarian | Moderate | Low |
    | 21 | Low | Balanced | Moderate | Low |
    | 22 | High | Vegetarian | High | Moderate |
    | 23 | Low | High | High | Moderate |
    | 24 | Low | Balanced | Low | Moderate |
    | 25 | High | Balanced | Moderate | Low |
    | 26 | Moderate | High | None | Low |
    | 27 | High | High | None | High |
    | 28 | Moderate | High | Low | High |
    | 29 | Moderate | High | Low | Low |
    | 30 | Low | High | Moderate | Moderate |
    | 31 | High | High | None | Low |
    | 32 | Moderate | High | High | High |
    | 33 | Moderate | High | High | High |
    | 34 | Moderate | Balanced | High | Moderate |
    | 35 | Moderate | High | Moderate | Low |
    | 36 | High | High | Moderate | High |
    | 37 | Low | Balanced | Low | Moderate |
    | 38 | Low | Balanced | None | High |
    | 39 | Moderate | Balanced | High | Moderate |
    | 40 | Low | Vegetarian | None | High |
    | 41 | Moderate | High | Moderate | High |
    | 42 | Low | High | None | Low |
    | 43 | Low | High | High | Moderate |
    | 44 | High | High | None | Moderate |
    | 45 | Moderate | High | High | High |
    | 46 | High | Vegetarian | Moderate | Low |
    | 47 | Low | Vegetarian | Low | High |
    | 48 | Moderate | High | High | High |
    | 49 | Moderate | Vegetarian | Low | High |
    | 50 | Moderate | High | High | Moderate |
    | 51 | Moderate | Vegetarian | Low | Low |
    | 52 | Moderate | Balanced | Moderate | High |
    | 53 | Moderate | Balanced | None | High |
    | 54 | Low | High | High | High |
    | 55 | Moderate | Balanced | High | Moderate |
    | 56 | Low | High | High | High |
    | 57 | High | Balanced | Moderate | Moderate |
    | 58 | Low | Vegetarian | High | Moderate |
    | 59 | High | High | Moderate | Moderate |
    | 60 | Moderate | Vegetarian | Low | Moderate |
    | 61 | Low | Vegetarian | None | Moderate |
    | 62 | Low | High | Low | Low |
    | 63 | Low | Balanced | None | Moderate |
    | 64 | High | Balanced | None | Moderate |
    | 65 | Moderate | Vegetarian | Low | High |
    | 66 | Low | High | High | Low |
    | 67 | High | High | High | Low |
    | 68 | Low | High | Low | High |
    | 69 | Low | Vegetarian | Moderate | Moderate |
    | 70 | Low | High | None | Low |
    | 71 | Low | High | None | Moderate |
    | 72 | High | Balanced | None | High |
    | 73 | Moderate | Balanced | None | Low |
    | 74 | Moderate | Vegetarian | None | Moderate |
    | 75 | Low | High | High | Low |
    | 76 | High | Balanced | Moderate | Low |
    | 77 | Moderate | High | None | Moderate |
    | 78 | Moderate | High | Moderate | Moderate |
    | 79 | Low | Balanced | Low | Low |
    | 80 | Low | High | Moderate | High |
    | 81 | High | Balanced | High | Low |
    | 82 | Moderate | Balanced | Moderate | High |
    | 83 | Low | Balanced | Moderate | Low |
    | 84 | High | High | Low | Moderate |
    | 85 | High | High | None | High |
    | 86 | High | Balanced | Moderate | High |
    | 87 | Moderate | High | High | Low |
    | 88 | Moderate | Balanced | Low | Low |
    | 89 | Moderate | Vegetarian | Moderate | High |
    | 90 | High | High | Moderate | Moderate |
    | 91 | High | High | Low | High |
    | 92 | Low | Balanced | High | High |
    | 93 | Low | Balanced | High | Moderate |
    | 94 | Moderate | Vegetarian | High | Moderate |
    | 95 | Moderate | Balanced | Moderate | Low |
    | 96 | Low | High | Moderate | Low |
    | 97 | Moderate | High | High | Low |
    | 98 | Low | Vegetarian | None | Moderate |
    | 99 | Low | Balanced | High | High |
    | 100 | Low | Balanced | Low | Moderate |

2. **Penggabungan Data**: Data dari ketiga file ini digabungkan berdasarkan `Patient_ID` untuk memungkinkan analisis yang komprehensif.

## Visualisasi dan Analisis
1. **Distribusi Usia**: Visualisasi distribusi usia pasien menggunakan histogram dengan overlay kernel density estimate (KDE).

2. **Distribusi BMI**: Histogram untuk menunjukkan distribusi BMI pasien.

3. **Distribusi Gula Darah Puasa**: Histogram untuk mengamati distribusi kadar gula darah puasa.

4. **Matriks Korelasi**: Matriks korelasi antar variabel medis untuk memahami hubungan antar indikator kesehatan pasien.

5. **Analisis Berdasarkan Gaya Hidup**:
   - **Aktivitas Fisik dan Gula Darah Puasa**: Boxplot yang menunjukkan hubungan antara level aktivitas fisik dan gula darah puasa.
   - **Jenis Diet dan BMI**: Boxplot yang mengeksplorasi pengaruh jenis diet terhadap BMI.
   - **Konsumsi Alkohol dan HbA1c**: Boxplot untuk melihat dampak konsumsi alkohol terhadap HbA1c.
   - **Stres dan Tekanan Darah Sistolik**: Boxplot yang menggambarkan hubungan antara tingkat stres dan tekanan darah sistolik.

## Persiapan Lingkungan
- Skrip ini memerlukan Python dengan pustaka berikut:
  - Pandas
  - Matplotlib
  - Seaborn

Instal pustaka-pustaka ini jika belum ada:
```bash
pip install pandas matplotlib seaborn
```

## Cara Menjalankan Skrip
1. Pastikan file CSV `diabetes_patient_info.csv`, `diabetes_medical_records.csv`, dan `diabetes_lifestyle_info.csv` berada di direktori yang sama dengan skrip Python ini.
2. Jalankan skrip ini di lingkungan Python Anda.

# Pertanyaan dan Jawaban
Tentu! Berikut adalah beberapa pertanyaan analisis data terkait dengan penyakit diabetes yang dapat dijawab dan divisualisasikan menggunakan kode yang telah dibuat:

1. **Bagaimana distribusi usia pasien dengan diabetes?**
   - Visualisasi: Histogram distribusi usia.

2. **Bagaimana distribusi BMI pasien dengan diabetes?**
   - Visualisasi: Histogram distribusi BMI.

3. **Bagaimana distribusi tingkat gula darah puasa pasien dengan diabetes?**
   - Visualisasi: Histogram distribusi gula darah puasa.

4. **Bagaimana hubungan antara usia, BMI, gula darah puasa, HbA1c, tekanan darah, dan kolesterol pada pasien dengan diabetes?**
   - Visualisasi: Matriks korelasi (heatmap).

5. **Bagaimana pengaruh tingkat aktivitas fisik terhadap tingkat gula darah puasa pasien dengan diabetes?**
   - Visualisasi: Boxplot gula darah puasa berdasarkan tingkat aktivitas fisik.

6. **Bagaimana pengaruh jenis diet terhadap BMI pasien dengan diabetes?**
   - Visualisasi: Boxplot BMI berdasarkan jenis diet.

7. **Bagaimana pengaruh konsumsi alkohol terhadap HbA1c pasien dengan diabetes?**
   - Visualisasi: Boxplot HbA1c berdasarkan konsumsi alkohol.

8. **Bagaimana pengaruh tingkat stres terhadap tekanan darah sistolik pasien dengan diabetes?**
   - Visualisasi: Boxplot tekanan darah sistolik berdasarkan tingkat stres.

Berikut adalah cara menjawab dan memvisualisasikan beberapa pertanyaan tersebut menggunakan kode yang telah dibuat:

### 1. Bagaimana distribusi usia pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.histplot(df_combined['Age'], kde=True, bins=10, color=color_palette[0])
plt.title('Distribusi Usia Pasien', fontsize=16)
plt.xlabel('Usia', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()
```

### 2. Bagaimana distribusi BMI pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.histplot(df_combined['BMI'], kde=True, bins=10, color=color_palette[1])
plt.title('Distribusi BMI Pasien', fontsize=16)
plt.xlabel('BMI', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()
```

### 3. Bagaimana distribusi tingkat gula darah puasa pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.histplot(df_combined['Fasting_Blood_Sugar'], kde=True, bins=10, color=color_palette[2])
plt.title('Distribusi Gula Darah Puasa Pasien', fontsize=16)
plt.xlabel('Fasting Blood Sugar', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()
```

### 4. Bagaimana hubungan antara usia, BMI, gula darah puasa, HbA1c, tekanan darah, dan kolesterol pada pasien dengan diabetes?

```python
correlation_matrix = df_combined[['Age', 'BMI', 'Fasting_Blood_Sugar', 'HbA1c', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic', 'Cholesterol']].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title('Matriks Korelasi', fontsize=16)
plt.show()
```

### 5. Bagaimana pengaruh tingkat aktivitas fisik terhadap tingkat gula darah puasa pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='Physical_Activity_Level', y='Fasting_Blood_Sugar', data=df_combined, palette="Set2")
plt.title('Level Gula Darah Puasa berdasarkan Aktivitas Fisik', fontsize=16)
plt.xlabel('Level Aktivitas Fisik', fontsize=14)
plt.ylabel('Fasting Blood Sugar', fontsize=14)
plt.show()
```

### 6. Bagaimana pengaruh jenis diet terhadap BMI pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='Diet_Type', y='BMI', data=df_combined, palette="Set3")
plt.title('BMI berdasarkan Jenis Diet', fontsize=16)
plt.xlabel('Jenis Diet', fontsize=14)
plt.ylabel('BMI', fontsize=14)
plt.show()
```

### 7. Bagaimana pengaruh konsumsi alkohol terhadap HbA1c pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='Alcohol_Consumption', y='HbA1c', data=df_combined, palette="Set1")
plt.title('HbA1c berdasarkan Konsumsi Alkohol', fontsize=16)
plt.xlabel('Konsumsi Alkohol', fontsize=14)
plt.ylabel('HbA1c', fontsize=14)
plt.show()
```

### 8. Bagaimana pengaruh tingkat stres terhadap tekanan darah sistolik pasien dengan diabetes?

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='Stress_Level', y='Blood_Pressure_Systolic', data=df_combined, palette="Paired")
plt.title('Tekanan Darah Sistolik berdasarkan Level Stres', fontsize=16)
plt.xlabel('Level Stres', fontsize=14)
plt.ylabel('Blood Pressure Systolic', fontsize=14)
plt.show()
```
![Figure_1](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/b1797679-20bc-46b0-ae48-80cbd5405c59)
![Figure_2](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/a52284cb-0494-4c8f-af6a-59907c27bb15)
![Figure_3](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/5720a673-aa5f-4afa-b374-fe390455b3de)
![Figure_4](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/6a901fcc-3150-4e8b-87ab-cd3cec33375e)
![Figure_5](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/1258370d-4ddc-4f67-a303-dbf918aed171)
![Figure_6](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/97382f96-57f0-42f6-bd94-5d56d2ae0ffb)
![Figure_7](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/dcaab50b-9ad9-4df5-8e01-e262dcc495ee)
![Figure_8](https://github.com/NabiilaDiwasasriPutriPranaya/Analisi-Data-Penyakit-Diabetes-/assets/167085600/9543699f-7b79-4a46-87de-c94f76b7dffb)



