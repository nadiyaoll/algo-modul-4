# Konstanta
massa = 1.5  # kg
percepatan = 4  # m/s²
posisi_awal = 20  # m
g = 10  # m/s² (diasumsikan untuk energi potensial gravitasi)
waktu_total = 6  # detik

# Fungsi untuk menghitung nilai pada waktu t
def hitung_nilai(t):
    # Kecepatan akhir (v = u + a t, u=0)
    kecepatan = percepatan * t
    
    # Posisi (h = h0 + (1/2) a t²)
    posisi = posisi_awal + 0.5 * percepatan * t**2
    
    # Energi kinetik (EK = 1/2 m v²)
    energi_kinetik = 0.5 * massa * kecepatan**2
    
    # Energi potensial gravitasi (EP = m g h)
    energi_potensial = massa * g * posisi
    
    return kecepatan, posisi, energi_kinetik, energi_potensial

# Header tabel
print("Waktu (s) | Kecepatan (m/s) | Posisi (m) | Energi Kinetik (J) | Energi Potensial (J)")
print("-" * 80)

# Loop untuk setiap interval 1 detik dari t=1 sampai t=6
for t in range(1, waktu_total + 1):
    kecepatan, posisi, ek, ep = hitung_nilai(t)
    print(f"{t:8} | {kecepatan:13.2f} | {posisi:9.2f} | {ek:17.2f} | {ep:18.2f}")