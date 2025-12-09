# Tugas_PCD_EdgeDetectionRobertSobel

📘 ANALISA LENGKAP DETEKSI TEPI ROBERTS DAN SOBEL
1. Pendahuluan

Deteksi tepi merupakan salah satu teknik dasar dalam pengolahan citra digital yang digunakan untuk mencari perubahan intensitas piksel yang signifikan pada sebuah gambar. Teknik ini banyak digunakan dalam:

segmentasi objek

deteksi bentuk

computer vision

machine learning vision preprocessing

Dalam tugas ini, dilakukan implementasi dan analisis dua operator deteksi tepi:

Operator Roberts

Operator Sobel

Keduanya dianalisis menggunakan Python dengan library imageio, numpy, dan matplotlib, serta diuji pada gambar JPEG.

📗 2. Analisis Algoritma dan Implementasi
2.1 Operator Roberts

Operator Roberts menggunakan dua kernel 2×2:

𝐺
𝑥
=
[
1
	
0


0
	
−
1
]
,
𝐺
𝑦
=
[
0
	
1


−
1
	
0
]
G
x
	​

=[
1
0
	​

0
−1
	​

],G
y
	​

=[
0
−1
	​

1
0
	​

]

Ciri-ciri:

Ukuran kernel kecil (2×2)

Sangat sensitif terhadap perubahan intensitas piksel

Cocok untuk mendeteksi tepi yang sangat tajam

Namun sensitif terhadap noise

Hasilnya cenderung lebih "kasar" dan lebih terfragmentasi

Operator Roberts menghitung gradien menggunakan perbedaan diagonal, sehingga cocok untuk mendeteksi tepi diagonal.

2.2 Operator Sobel

Operator Sobel menggunakan kernel 3×3:

𝐺
𝑥
=
[
−
1
	
0
	
1


−
2
	
0
	
2


−
1
	
0
	
1
]
,
𝐺
𝑦
=
[
−
1
	
−
2
	
−
1


0
	
0
	
0


1
	
2
	
1
]
G
x
	​

=
	​

−1
−2
−1
	​

0
0
0
	​

1
2
1
	​

	​

,G
y
	​

=
	​

−1
0
1
	​

−2
0
2
	​

−1
0
1
	​

	​


Karakteristik:

Kernel lebih besar (3×3) → lebih stabil

Menggunakan pembobotan pada baris tengah → hasil lebih halus

Lebih tahan noise dibanding Roberts

Lebih baik untuk mendeteksi tepi vertikal dan horizontal

Operator Sobel memberikan hasil yang lebih “halus” dan lebih kontinu.

2.3 Perbedaan Utama
Aspek	Roberts	Sobel
Ukuran Kernel	2×2	3×3
Sensitivitas Noise	Tinggi	Lebih rendah
Kualitas Tepi	Kasar, lebih tipis	Lebih jelas dan tebal
Kecepatan	Lebih cepat	Sedikit lebih lambat
Hasil	Fragmented / patah-patah	Lebih smooth
📘 3. Analisis Hasil Pengujian

Setelah program dijalankan, diperoleh tiga output gambar:

output_grayscale.png

output_roberts.png

output_sobel.png

output_all.png (gabungan)

Berikut hasil analisisnya:

3.1 Hasil Grayscale

Konversi grayscale dilakukan menggunakan rumus luminance:

0.299
𝑅
+
0.587
𝐺
+
0.114
𝐵
0.299R+0.587G+0.114B

Gambar grayscale digunakan karena operator gradien lebih efektif bekerja pada intensitas tunggal, bukan RGB.

3.2 Analisis Hasil Roberts

Karakter hasil:

Tepi terdeteksi dengan sangat tajam

Terdapat banyak noise (bintik kecil)

Tepi diagonal lebih kuat dibanding horizontal/vertikal

Detail kecil pada gambar cenderung ikut terdeteksi

Hasil Roberts tampak "kasar" dan sering memberikan garis yang tidak menyambung.

3.3 Analisis Hasil Sobel

Karakter hasil:

Tepi lebih rata, halus, dan lebih tebal

Noise lebih sedikit

Objek utama terlihat lebih jelas

Kontur tepi lebih menyatu dan tidak putus-putus

Sobel memberikan hasil yang lebih siap diproses lebih lanjut (misalnya segmentasi)

Hasil Sobel tampak lebih “bersih” dan memiliki kualitas estetika yang lebih baik.

📗 4. Perbandingan Robert vs Sobel
Akurasi deteksi tepi

Sobel lebih akurat, terutama pada gambar dengan noise atau gradien lembut.

Kejelasan kontur

Sobel memberikan garis kontur yang lebih tebal dan menyatu.

Sensitivitas terhadap detail kecil

Roberts lebih tajam tetapi cenderung mendeteksi noise sebagai tepi.

Kecepatan

Roberts sedikit lebih cepat karena kernel lebih kecil.

📘 5. Kesimpulan

Dari implementasi dan pengujian yang telah dilakukan, dapat disimpulkan:

Operator Roberts:

Memberikan deteksi tepi yang sangat sensitif.

Cocok untuk gambar dengan kontras tinggi.

Tidak cocok untuk gambar dengan noise.

Operator Sobel:

Lebih stabil dan lebih tahan terhadap noise.

Memberikan hasil deteksi tepi yang lebih halus dan jelas.

Lebih cocok digunakan pada kebanyakan aplikasi computer vision modern.

Berdasarkan hasil pengujian:

Sobel lebih direkomendasikan untuk deteksi tepi secara umum.

Roberts hanya cocok untuk kebutuhan spesifik yang membutuhkan deteksi perubahan intensitas yang sangat tajam.
