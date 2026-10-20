# Latihan 6: Fungsi Statistik
# Membuat fungsi untuk menghitung rata-rata list.
# Jika list kosong, fungsi mengembalikan 0 agar tidak terjadi pembagian dengan nol.

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata = {rata_rata(nilai):.2f}")
