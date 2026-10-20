# Pertemuan 09 — List dan Pengolahan Data Numerik
  
**Nama:** Arya Kusmana Anas 
**NIM:** 2225250118
**Kelas:** 3B 

## Tujuan
Mempelajari penggunaan list Python untuk menyimpan, mengakses, memanipulasi, dan mengolah kumpulan data numerik. Latihan juga menggabungkan perulangan, seleksi, fungsi, pengujian program, serta pengumpulan melalui GitHub.

## Struktur Folder

```text
pertemuan-09-list/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Materi yang Dipraktikkan
- Membuat list dan menghitung jumlah elemen dengan `len()`.
- Mengakses elemen menggunakan indeks positif dan negatif.
- Mengambil bagian list menggunakan slicing.
- Mengubah, menambah, menyisipkan, dan menghapus elemen.
- Menggunakan `sum()`, `min()`, dan `max()` untuk pengolahan numerik.
- Menelusuri list dengan perulangan dan menyaring nilai kelulusan.
- Membuat fungsi yang menerima list sebagai parameter.

## Persiapan
1. Pastikan Python 3 sudah terpasang.
2. Buka folder proyek ini melalui **File → Open Folder** di VS Code.
3. Pilih interpreter Python 3 melalui **Python: Select Interpreter**.
4. Buka terminal VS Code melalui **Terminal → New Terminal**.

## Cara Menjalankan
Jalankan perintah dari terminal pada folder utama proyek.

Windows:
```powershell
python latihan/01_buat_list.py
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
python praktik/analisis_nilai_mahasiswa.py
```

macOS/Linux (jika perintah `python` tidak tersedia, gunakan `python3`):
```bash
python3 latihan/01_buat_list.py
python3 latihan/02_indeks_slicing.py
python3 latihan/03_manipulasi_list.py
python3 latihan/04_agregasi_nilai.py
python3 latihan/05_filter_kelulusan.py
python3 latihan/06_fungsi_statistik.py
python3 praktik/analisis_nilai_mahasiswa.py
```

Alternatif: buka file `.py`, lalu tekan tombol **Run Python File** di VS Code.

## Ringkasan Praktik Utama
Program `analisis_nilai_mahasiswa.py` menggunakan 10 nilai contoh dan batas kelulusan 60. Program menampilkan banyak data, total, rata-rata, nilai minimum, nilai maksimum, daftar nilai lulus, jumlah lulus, dan jumlah belum lulus.

## Test Case
| Data | Hal yang diperiksa | Hasil yang diharapkan |
|---|---|---|
| `[60, 70, 80]` | Rata-rata | `70.00` |
| `[60, 70, 80]` | Minimum dan maksimum | `60` dan `80` |
| `[60, 70, 80]` | Jumlah nilai lulus | `3` |
| `[59, 60, 61]` | Batas kelulusan 60 | `2` nilai lulus |
| `[]` | Fungsi rata-rata | Mengembalikan `0`, tidak error |

## Hasil Pengujian
Jalankan setiap file dan cocokkan output dengan tujuan latihan. Catat hasil aktual berikut setelah pengujian:

| File | Hasil aktual | Status |
|---|---|---|
| `01_buat_list.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `02_indeks_slicing.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `03_manipulasi_list.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `04_agregasi_nilai.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `05_filter_kelulusan.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `06_fungsi_statistik.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `analisis_nilai_mahasiswa.py` | Isi setelah diuji | Lulus/Perlu perbaikan |

## Cara Mengunggah ke GitHub
Buat repositori baru di GitHub, lalu salin URL HTTPS repositori. Dari terminal VS Code, jalankan perintah berikut (ganti URL dengan URL repositori milik sendiri):

```bash
git init
git add .
git commit -m "feat: menambahkan latihan list pertemuan 09"
git branch -M main
git remote add origin https://github.com/USERNAME/pertemuan-09-list-NIM.git
git push -u origin main
```

Untuk commit bertahap sesuai bahan ajar:
```bash
git add latihan
git commit -m "feat: menyelesaikan latihan list dan agregasi"

git add praktik/analisis_nilai_mahasiswa.py
git commit -m "feat: menyelesaikan praktik analisis nilai"

git add README.md
git commit -m "docs: menambahkan test case dan refleksi"

git push
```

Periksa hasil dengan:
```bash
git status
git log --oneline --decorate -5
git remote -v
```

## Refleksi
1. Satu hal yang saya pahami tentang list dan indeks: ...
2. Kesalahan yang saya temui dan cara memperbaikinya: ...
3. Hal yang masih perlu saya pelajari: ...

## Referensi
- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 09: *List/Array dan Pengolahan Data Numerik Sederhana*.
- Python Software Foundation, dokumentasi Python 3 tentang struktur data.
- Dokumentasi Visual Studio Code untuk Python.
- Dokumentasi GitHub tentang menambahkan kode lokal ke GitHub.

> Sesuaikan nama, NIM, kelas, hasil pengujian, dan refleksi berdasarkan pekerjaan Anda sendiri. Pastikan Anda memahami dan dapat menjelaskan kode yang dikumpulkan.
