# Laporan Proyek Machine Learning Terapan - Qaila Casandra
## Domain Proyek
Pasar saham merupakan salah satu instrumen investasi yang paling dinamis dan menarik perhatian banyak investor di seluruh dunia. Indeks S&P 500, sebagai salah satu indeks pasar saham terkemuka di Amerika Serikat, sering dijadikan acuan untuk mengukur kinerja pasar saham secara keseluruhan. Indeks ini mencakup 500 perusahaan besar dengan kapitalisasi pasar tinggi yang tercatat di bursa saham AS, sehingga pergerakannya mencerminkan kesehatan ekonomi secara makro.Proyek ini berada dalam domain keuangan, khususnya pada analisis pasar saham. Pasar saham, terutama indeks S&P 500, merupakan indikator penting dari kesehatan ekonomi Amerika Serikat dan menjadi acuan utama bagi para investor global.

Dengan banyaknya faktor yang memengaruhi pergerakan harga saham, memprediksi indeks S&P 500 secara akurat sangatlah menantang. Namun, dengan teknik machine learning, kita dapat memanfaatkan pola historis dalam data harga saham untuk melakukan prediksi yang lebih akurat dan berbasis data.

### Refrensi
J. Y. Campbell, A. W. Lo, and A. C. MacKinlay, The Econometrics of Financial Markets, Princeton University Press, 1997.

Investing.com: [S&P%500_Investing.com](https://id.investing.com/indices/us-spx-500-historical-data)

## Business Understanding
### Problem Statements
1. Bagaimana memprediksi nilai indeks S&P 500 di masa mendatang berdasarkan data historis?
2. Teknik machine learning apa yang paling efektif dalam memprediksi indeks S&P 500 berdasarkan performa dan akurasi?

### Goals
1. Mengembangkan model prediktif untuk memperkirakan nilai S&P 500 menggunakan data historis.
2. Membandingkan beberapa algoritma machine learning dan menentukan model terbaik berdasarkan nilai error terkecil.

### Solution Statements
1. Menggunakan dua algoritma yaitu K-Nearest Neighbors (KNN) dan Gradient Boosting Regressor (GBR).
2. Melakukan preprocessing dan teknik scaling serta Principal Component Analysis (PCA) untuk mengurangi dimensi.
3. Evaluasi dilakukan dengan Mean Squared Error (MSE) untuk memilih model terbaik.

## Data Understanding
Dataset diambil dari Investing.com untuk indeks S&P 500: (https://id.investing.com/indices/us-spx-500-historical-data)

### Fitur utama pada dataset
Tanggal: Tanggal pengamatan
Terakhir: Nilai penutupan indeks
Pembukaan: Nilai pembukaan
Tertinggi: Nilai tertinggi
Terendah: Nilai terendah
Vol.: Volume perdagangan
Perubahan%: Persentase perubahan dari hari sebelumnya 

### Data Preparation
adapun beberapa tahapan yang dilakukan
1. Pembersihan kolom: kolom Vol. dihapus karena seluruhnya bernilai null.
2. Konversi data numerik: kolom seperti Terakhir, Pembukaan, Tertinggi, Terendah yang awalnya string dengan koma (,) diubah menjadi float.
3. Ekstraksi target: target prediksi adalah Terakhir hari berikutnya.
4. Pemisahan fitur dan target.
5. Scaling dengan MinMaxScaler untuk menyetarakan skala fitur.
6. PCA dilakukan untuk mereduksi dimensi dan mengurangi noise.

### Modeling
1. K-Nearest Neighbors Regressor (KNN)
2. Gradient Boosting Regressor (GBR)
#### Catatan:
1. KNN cocok untuk prediksi berbasis kedekatan pola, namun kurang baik untuk data dengan noise.
2. GBR lebih mampu menangani kompleksitas, cocok untuk regresi finansial.

## Evaluation
### Metrik evaluasi: Mean Squared Error (MSE)
Rumus:
![image](https://github.com/user-attachments/assets/4e036d87-7255-49f7-b8d7-11dfdfd8e48e)
### Adapun hasil dari evaluasi model :
1. K-Nearest Neighbors Regressor:
MSE = 0.0569
2. Gradient Boosting Regressor:
MSE = 0.0536
### Kesimpulan
Model Gradient Boosting Regressor (GBR) menghasilkan MSE yang lebih kecil dibandingkan KNN, sehingga dipilih sebagai model terbaik dalam proyek ini untuk memprediksi indeks S&P 500 berdasarkan data historis.
