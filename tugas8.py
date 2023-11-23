#latihan 2
def PredikatKelulusan(nilai):
    if nilai <= 60: 
        print("gagal")
    elif nilai >= 61 and nilai <= 70:
        print("baik")
    elif nilai >= 71 and nilai <= 80:
        print("sangat baik")
    elif nilai >= 81 and nilai <= 100:
        print("istimewa")
PredikatKelulusan(60)

print()

# Latihan 3
def sebut_ganjil(angka):
    for i in range(angka):
        if i % 2 != 0 :
            print(i)
sebut_ganjil(20)

print()

# latihan 1. buatlah fungsi untuk menampilkan data diri
# contoh pemanggilan : profil (nama, alamat, gender, umur, hobby)
def data_diri (nama, alamat, gender, umur, hobby):
    print("nama:",nama)
    print("alamat:",alamat)
    print("gender:",gender)
    print("umur:",umur)
    print("hobby:",hobby)
data_diri("adinda", "buana 5", "perempuan", "19 tahun", "olahraga")
    
    






