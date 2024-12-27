# Program Menghitung Gaji Karyawan

# Input dari pengguna
jam_kerja = float(input("Masukkan jumlah jam kerja: "))
tarif_per_jam = float(input("Masukkan tarif per jam: "))

# Konstanta untuk menghitung lembur
jam_normal = 40
tarif_lembur = 1.5

# Perhitungan gaji
if jam_kerja > jam_normal:
    jam_lembur = jam_kerja - jam_normal
    gaji_lembur = jam_lembur * tarif_per_jam * tarif_lembur
    gaji_total = (jam_normal * tarif_per_jam) + gaji_lembur
else:
    gaji_total = jam_kerja * tarif_per_jam

# Menampilkan hasil
print(f"Gaji total karyawan: Rp {gaji_total:.2f}")
