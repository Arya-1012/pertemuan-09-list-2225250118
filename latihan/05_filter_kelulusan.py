# Latihan 5: Filter Kelulusan
# Menampilkan nilai yang memenuhi batas kelulusan 60 dan menghitung jumlahnya.

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
