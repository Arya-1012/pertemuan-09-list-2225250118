# Praktik: Analisis Nilai Mahasiswa
# Mengolah nilai mahasiswa menggunakan list dan fungsi.
# Batas kelulusan adalah 60.

def rata_rata(data):
    """Menghitung rata-rata; mengembalikan 0 jika data kosong."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Mengembalikan list nilai yang sama dengan atau di atas batas."""
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil


def tampilkan_analisis(data):
    """Menampilkan ringkasan statistik dan informasi kelulusan."""
    print("=== ANALISIS NILAI MAHASISWA ===")
    print(f"Data nilai       : {data}")
    print(f"Banyak data      : {len(data)}")

    if len(data) == 0:
        print("Tidak ada data untuk dianalisis.")
        return

    lulus = nilai_lulus(data)
    jumlah_lulus = len(lulus)
    jumlah_belum_lulus = len(data) - jumlah_lulus

    print(f"Total nilai      : {sum(data)}")
    print(f"Rata-rata        : {rata_rata(data):.2f}")
    print(f"Nilai minimum    : {min(data)}")
    print(f"Nilai maksimum   : {max(data)}")
    print(f"Nilai lulus      : {lulus}")
    print(f"Jumlah lulus     : {jumlah_lulus}")
    print(f"Jumlah belum lulus: {jumlah_belum_lulus}")


if __name__ == "__main__":
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    tampilkan_analisis(nilai)
