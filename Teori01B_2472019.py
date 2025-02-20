# File: Tugas01B_2472019
# Penulis: Miracle Steven Gerrald
# Tujuan program: Membaca variabel nama, tinggi, dan tahun sesuai dengan nilai yang diinput user, dan mencetak tinggi badan anak tersebut beberapa tahun kemudian. Asumsi anak sehat, setiap tahun tingginya bertambah 5 cm.
# ---- Kamus Data ----
# today = tanggal hari ini (menggunakan bentuk datetime.date.today() yang diimport dari modul datetime, agar hasil tanggal yang ditampilkan adaptif)
# tahun_awal = tahun ini (menggunakan today.year untuk menampilkan hasil tahun yang dinamis)
# nama = nama anak
# tinggi = tinggi anak
# tahun_akhir = tahun yang diinput user

import datetime

def main():
    # INPUT / STORED DATA / PREP
    today = datetime.date.today()
    tahun_awal = today.year

    nama = input("Nama        : ")
    tinggi = int(input("Tinggi (cm) : "))
    tahun_akhir = int(input("Tahun       : "))

    # OUTPUT
    print(f'''
    ====================================
    Sekarang tinggi {nama} {tinggi} cm
    ------------------------------------
    Tahun {tahun_akhir}, tingginya menjadi {tinggi + 5 * (tahun_akhir - tahun_awal)} cm
    ====================================
          ''')
    
    return 0


if __name__ == '__main__':
    main()