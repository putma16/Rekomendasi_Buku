# Sistem Rekomendasi Buku Berbasis Kemiripan

## Deskripsi Proyek

Proyek ini merupakan Sistem Rekomendasi Buku yang dikembangkan dengan menggunakan metode Cosine Similarity. Sistem ini memanfaatkan dataset publik dari Kaggle yang terdiri dari dua tabel, yakni ulasan pengguna dan detail buku. Dalam implementasinya, kolom-kolom esensial yang digunakan meliputi 'Title', 'description', dan 'ratingsCount'.

Tujuan utama dari sistem ini adalah memberikan rekomendasi buku kepada pengguna berdasarkan kemiripan (similarity) antara buku yang dipilih oleh pengguna dengan buku-buku lain dalam dataset. Metode yang digunakan, yaitu Cosine Similarity, mengukur sejauh mana kemiripan antara deskripsi buku menggunakan representasi TF-IDF.

## Dataset

Dataset yang digunakan berasal dari Kaggle dengan tautan [berikut](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews). Dataset ini terdiri dari dua tabel, dimana tabel pertama berisi ulasan pengguna dan tabel kedua berisi detail buku.

## Metode dan Tahapan

### Metode: Cosine Similarity

Cosine Similarity digunakan untuk mengukur sejauh mana kemiripan antara dua vektor non-nol, dalam hal ini, vektor-vektor merepresentasikan deskripsi buku dalam bentuk TF-IDF.

### Tahapannya:

1. **Pemilihan dan Persiapan Data:**
   - Memuat dataset buku dan melakukan pemrosesan data seperti penghapusan nilai-nilai yang hilang.

2. **Normalisasi Teks:**
   - Melakukan normalisasi teks pada deskripsi buku.

3. **Representasi TF-IDF:**
   - Mengonversi deskripsi buku menjadi representasi vektor TF-IDF menggunakan TF-IDF Vectorizer.

4. **Perhitungan Cosine Similarity:**
   - Menghitung matriks kesamaan kosinus antara vektor-vektor TF-IDF dari deskripsi buku.

5. **Rekomendasi:**
   - Jika pengguna memilih suatu buku, sistem akan merekomendasikan buku-buku lain dengan kemiripan kosinus tertinggi.

## Pengujian Aplikasi

Sistem Rekomendasi Buku ini dapat diakses melalui [tautan ini](https://aplikasi-rekomendasi-buku-anisputma.streamlit.app/). 

**Selamat menikmati eksplorasi dunia literasi melalui Sistem Rekomendasi Buku!**
