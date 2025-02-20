# File: Tugas01A_2472019
# Penulis: Miracle Steven Gerrald
# Tujuan program: Membaca suatu bilangan integer yang menyatakan jumlah minggu, dan mencetak berapa tahun dan bulan serta minggu yang setara dengan jumlah hari yang diinputkan.
# ---- Kamus Data ----
# input_awal : jumlah minggu yang ingin dikonversi oleh pengguna
# year : jumlah tahun dari pembagian input_awal
# month : jumlah bulan dari pembagian input_awal
# week : jumlah minggu dari sisa pembagian input_awal

def main():
    # INPUT
    input_awal = int(input("Jumlah minggu: "))

    # PROSES
    year = input_awal // 52
    month = (input_awal % 52) // 4
    week = (input_awal % 52) % 4

    # OUTPUT
    print(f"{input_awal} minggu setara dengan {year} tahun, {month} bulan, dan {week} minggu.")
    return 0


if __name__ == '__main__':
    main()
