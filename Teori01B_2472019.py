# File: Tugas01B_2472019
# Penulis: Miracle Steven Gerrald
# Tujuan program: Membaca variabel nama, tinggi, dan tahun sesuai dengan nilai yang diinput user, dan mencetak tinggi badan anak tersebut beberapa tahun kemudian. Asumsi anak sehat, setiap tahun tingginya bertambah 5 cm.
# ---- Kamus Data ----
# i : variabel integer

import datetime

def main():
    # INPUT / STORED DATA / PREP
    today = datetime.date.today()
    current_year = today.year

    nama = input("Nama  : ")
    tinggi = int(input("Tinggi (cm) : "))
    tahun = int(input("Tahun    : "))

    # OUTPUT
    print(f'''
    ====================================
    Sekarang tinggi {nama} {tinggi} cm
    ------------------------------------
    Tahun {tahun + 5}, tingginya menjadi {tinggi + 5}
    ====================================
          ''')
    
    return 0


if __name__ == '__main__':
    main()