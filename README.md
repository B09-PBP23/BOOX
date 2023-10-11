# BOOX
Proyek Tengah Semester 

Pemrograman Berbasis Platform B - Gasal 23/24

## Anggota Kelompok:
- Aldyandry Nureza Phutra - 2206809936
- Fadhil Muhammad - 2206083464
- Neva Denstia Shabira - 2206083073
- Salma Kurnia Dewi - 2206026681
- Theodore Kasyfillah -  2206083136
- Yoshelin Yamala Vijnana - 22062826702


## Dataset
Sumber dataset yang kami pilih adalah dataset dari Kaggle dengan URL sebagai berikut:
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

Alasannya karena dataset tersebut sangat terperinci. Terdapat lebih dari 100 data buku yang dilengkapi dengan nomor ISBN, judul buku, nama penulis, tahun publikasi, penerbit buku, serta URL image cover buku tersebut. Pada dataset tersebut juga memiliki beberapa collaborator yang menyertakan kode untuk filter buku dan rekomendasi dalam bahasa python.

## Cerita Aplikasi dan Manfaatnya
Aplikasi “Boox” adalah platform yang ditujukan untuk memudahkan pengguna dalam memberikan penilaian, ulasan, serta mengeksplorasi dunia buku dengan beragam genre. Situs ini menyediakan wadah bagi para pembaca untuk bertukar ulasan  tentang buku-buku yang mereka baca.

Situs “Boox” memberikan kesempatan kepada penggunanya untuk berpartisipasi dalam memperluas dan memperbarui data buku. Pengguna dapat menambahkan buku yang belum tersedia di aplikasi. Hal ini bertujuan untuk memastikan bahwa aplikasi selalu up-to-date dengan daftar buku yang terus bertambah dan diperbarui.

Situs “Boox” juga mengakomodasi pengguna untuk berinteraksi dengan pengguna lainnya. Pengguna dapat memberikan respon atau komentar terkait dengan ulasan pengguna lainnya. Hal ini tentunya menjadi salah satu daya tarik aplikasi “Boox”, review buku menjadi tidak monoton karena pengguna dapat saling berkomunikasi dan bertukar pikiran. 

Dengan adanya situs “Boox” beserta kelengkapan fiturnya, dapat membantu dalam memperkaya koleksi buku yang ada di dalam aplikasi dan memungkinkan pengguna untuk menemukan buku-buku yang mungkin belum mereka ketahui sebelumnya. Dengan berkontribusi untuk menyediakan informasi buku yang lebih lengkap dan bervariasi, pengguna aplikasi XYZ dapat membantu memberikan kesempatan bagi pengguna lain untuk mengeksplorasi lebih banyak pilihan bacaan, dan memperkaya pengalaman sebagai pembaca.

## Daftar Modul

1. **Register & Login page**:

    Halaman ini dapat diakses melalui halaman landing page. Halaman register berfungsi untuk mendaftarkan pengguna baru. Setelah pengguna selesai mendaftarkan pada halaman register, maka akan diarahkan ke halaman login. Sementara itu, halaman login berfungsi untuk login pengguna yang sudah memiliki akun.
2. **Reader’s Favorite page** :

    Halaman ini memberikan informasi mengenai review-review terfavorit dari para pengguna. Review-review disini diurutkan berdasarkan jumlah upvote dan pengguna dapat menekan button upvote untuk menaikkan posisi pada urutan review terfavorit.
3. **Profile Page**

    Pada halaman ini, terdapat informasi dari pengguna yang sedang login. Page ini berisikan fitur berikut:
    - **Foto Profil**: Pengguna dapat mengunggah foto profil atau gambar avatar yang mewakili diri mereka. Ini adalah gambar yang akan dilihat oleh pengguna lain ketika mereka mengunjungi profil pengguna tersebut.
    - **Username**: Nama pengguna atau alias yang digunakan oleh pengguna di situs tersebut. Ini dapat menjadi nama asli atau nama samaran, tergantung pada preferensi pengguna.
    - **Ringkasan Profil**: Ringkasan singkat yang memberikan gambaran tentang pengguna. Ini bisa berisi informasi tentang minat dalam membaca, genre buku favorit, atau apa pun yang ingin pengguna bagikan dengan komunitas.
    - **Riwayat Ulasan**: Ini adalah daftar ulasan buku yang telah ditulis oleh pengguna. Setiap ulasan biasanya dilengkapi dengan judul buku, penilaian (biasanya dalam bentuk bintang atau peringkat numerik), dan teks ulasan itu sendiri. Pengguna juga dapat menyertakan tanggal ulasan untuk menunjukkan seberapa baru atau lama ulasan tersebut.

4. **Bookmarks**

    Pada setiap buku, tersedia tombol “Bookmarks” yang bertujuan untuk mempermudah pengguna dalam menandai buku yang ingin mereka markah. Dengan adanya halaman bookmarks, maka pengguna dapat mengakses kembali buku apa saja yang menarik perhatian pengguna. Pada halaman ini, akan ditampilkan semua buku yang telah di-markah oleh pengguna. Fitur ini akan membantu pengguna untuk mengorganisir buku yang ditandai dalam satu tempat yang mudah diakses.

5. **Add Reviews**

    Modul add reviews berfungsi bagi para pengguna untuk menambahkan review mengenai sebuah buku. Modul ini dapat diakses di halaman review buku yang sudah ada. Apabila belum ada halaman review mengenai suatu buku, pengguna dapat membuat halaman review yang baru menggunakan modul ini. 

6. **Edit Reviews**

    Setelah pengguna menambahkan review sebuah buku di halaman add review, pengguna dapat mengedit review tersebut melalui modul ini.

## Fitur Utama

1. Formulir Review: formulir yang tersedia memungkinkan pengguna untuk mengisi informasi seperti judul review, peringkat (rating), teks ulasan, dan beberapa aspek tambahan seperti kategori buku, dan tanggal baca. 
2. Peringkat (Rating): Pengguna dapat memberikan peringkat berdasarkan jumlah bintang (misalnya, dari 1 hingga 5 bintang), yang merupakan cara cepat untuk menggambarkan kesan keseluruhan mereka tentang buku.
3. Pengunggahan Gambar: Pada halaman review buku yang baru, pengguna dapat mengunggah foto buku yang akan di-review. 
4. Komentar dan Interaksi: Modul ini juga dapat memungkinkan pengguna untuk memberikan komentar atau tanggapan terhadap ulasan pengguna lainnya, memungkinkan interaksi antara anggota komunitas. Jadi, pengguna lainnya juga bisa membalas komentar pengguna lain.


## Role atau Peran Pengguna Beserta Deskripsi

Target pengguna dari website yang kami buat ini adalah untuk mahasiswa/pelajar di Indonesia yang berumur 17-25 tahun yang memiliki ketertarikan terhadap buku/literatur. Terdapat dua tipe pengguna aplikasi berbeda yang dapat mengakses website “Boox.” Tipe pengguna pertama adalah pengguna yang melakukan registrasi/login, dan tipe pengguna kedua adalah pengguna yang mengakses website tanpa melakukan registrasi. Pengguna yang telah melakukan registrasi dapat mengakses website kami secara keseluruhan, yaitu dapat langsung menulis ulasan, menggunakan fitur bookmarks, dan mengakses riwayat ulasan. Berbeda dengan pengguna yang belum memiliki akun/melakukan registrasi. Pengguna tersebut hanya dapat melihat review saja.
