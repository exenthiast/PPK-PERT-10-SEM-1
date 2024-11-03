def enkripsi_nama(nama):
    encrypted = ""
    for char in nama:
        if char.isalpha():
            char_baru = chr(((ord(char) - 97 + 3) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + 3) % 26) + 65)
            encrypted += char_baru
        else:
            encrypted += char
    return encrypted

def input_data():
    nama = input("Masukkan nama mahasiswa: ")
    umur = int(input("Masukkan usia mahasiswa: "))
    rata_rata = float(input("Masukkan nilai rata-rata mahasiswa: "))
    enkripsi_nama_value = enkripsi_nama(nama)
    return {"nama": nama, "enkripsi_nama": enkripsi_nama_value, "umur": umur, "rata_rata": rata_rata}

def display_data(students, encrypted=False):
    if encrypted:
        print("Daftar Mahasiswa (Terenkripsi):")
        for i, student in enumerate(students):
            print(f"{i+1}. Nama Terenkripsi: {student['enkripsi_nama']}, Usia: {student['umur']}, Nilai: {student['rata_rata']}")
    else:
        print("Daftar Mahasiswa (Nama Asli):")
        for i, student in enumerate(students):
            print(f"{i+1}. {student['nama']}, Usia: {student['umur']}, Nilai: {student['rata_rata']}")

def mencari_student(students, nama):
    for student in students:
        if student["nama"].lower() == nama.lower():
            print(f"Mahasiswa '{nama}' ditemukan: Usia: {student['umur']}, Nilai Rata-Rata: {student['rata_rata']}")
            return
    print(f"Mahasiswa '{nama}' tidak ditemukan.")

def menghitung_rata_rata(students):
    if students:
        avg = sum(student["rata_rata"] for student in students) / len(students)
        print(f"Rata-rata nilai mahasiswa: {avg:.2f}")
    else:
        print("Tidak ada data mahasiswa.")

def display_passed_students(students):
    print("Mahasiswa yang Lulus (Nilai >= 70):")
    for student in students:
        if student["rata_rata"] >= 70:
            print(f"Nama Terenkripsi: {student['enkripsi_nama']}")

def display_tertua_and_termuda(students):
    if students:
        tertua = max(students, key=lambda x: x["umur"])
        termuda = min(students, key=lambda x: x["umur"])
        print(f"Mahasiswa Tertua: {tertua['nama']}, Usia: {tertua['umur']}")
        print(f"Mahasiswa Termuda: {termuda['nama']}, Usia: {termuda['umur']}")
    else:
        print("Tidak ada data mahasiswa.")

def main():
    students = []
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa (Terenkripsi)")
        print("3. Tampilkan Nama Asli Mahasiswa")
        print("4. Cari Mahasiswa Berdasarkan Nama")
        print("5. Hitung Rata-Rata Nilai Mahasiswa")
        print("6. Tampilkan Mahasiswa yang Lulus")
        print("7. Tampilkan Mahasiswa Tertua dan Termuda")
        print("8. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            students.append(input_data())
        elif pilihan == "2":
            display_data(students, encrypted=True)
        elif pilihan == "3":
            display_data(students, encrypted=False)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin dicari: ")
            mencari_student(students, nama)
        elif pilihan == "5":
            menghitung_rata_rata(students)
        elif pilihan == "6":
            display_passed_students(students)
        elif pilihan == "7":
            display_tertua_and_termuda(students)
        elif pilihan == "8":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
