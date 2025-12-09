# Edge Detection Using Roberts and Sobel Operators
Proyek ini mengimplementasikan deteksi tepi (edge detection) pada citra digital menggunakan dua metode populer, yaitu **Operator Roberts** dan **Operator Sobel**. Hasil keduanya kemudian dibandingkan untuk melihat perbedaan performa dan kualitas deteksi tepi.

---

## 📌 1. Deskripsi Proyek
Edge detection adalah proses penting dalam pengolahan citra, digunakan untuk mengekstraksi informasi bentuk, kontur, dan struktur objek dalam gambar.

Dalam proyek ini digunakan:
- **Python**
- **imageio** untuk pemrosesan gambar
- **numpy** untuk perhitungan matriks
- **matplotlib** untuk menampilkan hasil

Metode yang dibandingkan:
1. **Roberts Cross Operator (2×2 kernels)**
2. **Sobel Operator (3×3 kernels)**

---

## 📁 2. Struktur Folder
EdgeDetection-Roberts-Sobel/
│
├── edge_detection.py
├── sample.jpg
├── README.md
└── analysis.txt

---

## ⚙️ 3. Instalasi

Pastikan Python 3 sudah terpasang.

### Install dependency:
```bash
pip install numpy imageio matplotlib

▶️ 4. Cara Menjalankan Program

Jalankan script menggunakan:
python edge_detection.py

Program akan:
Memuat gambar sample.jpg
Mengonversi gambar ke grayscale
Menghitung gradien menggunakan operator Roberts dan Sobel
Menampilkan hasil perbandingan dalam 1 window matplotlib

🧠 5. Penjelasan Singkat Metode
Roberts Operator:
Kernel kecil 2×2
Mengukur perubahan diagonal
Menghasilkan tepi lebih tipis
Sangat sensitif terhadap noise
Perhitungan cepat

Sobel Operator:
Kernel 3×3
Menangkap gradien horizontal & vertikal
Lebih tahan noise (efek smoothing)
Menghasilkan tepi lebih tebal dan stabil

📊 6. Analisis Perbandingan
Hasil Roberts:
Tepi terlihat lebih tipis dan tajam
Sangat sensitif terhadap noise, sehingga beberapa area menjadi bercak
Tepi diagonal cukup jelas
Kurang stabil pada gambar dengan kontras rendah

Hasil Sobel:
Tepi lebih tebal, halus, dan konsisten
Noise lebih sedikit berkat kernel 3×3
Kontur objek lebih lengkap dan menyatu
Lebih cocok untuk aplikasi computer vision modern

📈 7. Tabel Perbandingan
| Aspek              | Roberts       | Sobel       |
| ------------------ | ------------- | ----------- |
| Ukuran Kernel      | 2×2           | 3×3         |
| Ketahanan Noise    | Rendah        | Tinggi      |
| Ketebalan Tepi     | Tipis         | Tebal       |
| Stabilitas Deteksi | Kurang stabil | Stabil      |
| Kualitas Hasil     | Menengah      | Baik        |
| Kecepatan          | Sangat cepat  | Cukup cepat |

📝 8. Kesimpulan
Dari percobaan yang dilakukan, dapat ditarik kesimpulan bahwa:
Operator Roberts memberikan hasil deteksi tepi yang sangat sensitif dan tipis, namun rentan terhadap noise dan ketidakstabilan.
Operator Sobel memberikan hasil tepi yang lebih baik secara visual, lebih stabil, dan lebih tahan terhadap noise.
Kesimpulan Utama:
Operator Sobel lebih direkomendasikan untuk aplikasi pengolahan citra karena menghasilkan deteksi tepi yang lebih bersih dan akurat.
Sementara itu, Roberts masih berguna ketika dibutuhkan komputasi cepat dan struktur kernel yang sederhana.

📄 9. Referensi

Digital Image Processing – Rafael C. Gonzalez & Richard E. Woods
OpenCV Documentation
Scikit-Image Edge Detection Guide

👨‍💻 10. Pembuat
Silakan modifikasi bagian ini dengan nama kamu:
Nama: [Raihan Daffa Abdurrohman]
Kelas: [TI23E]
NIM : [20230040145]
Prodi: Teknik Informatika
