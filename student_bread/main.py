from domain.student import Student
from infrastructures.in_memory_student_controller import InMemoryStudentController
from usecases.student_usecase import StudentUseCase

repo = InMemoryStudentController()
usecase = StudentUseCase(repo)

def print_menu():
    print("\nMenu:")
    print("1. Add Siswa")
    print("2. Browse Siswa/I")
    print("3. Read berdasarkan ID")
    print("4. Update Siswa/I")
    print("5. Delete Siswa/I")
    print("6. Keluar")

while True:
    print_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        id = int(input("ID: "))
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        usecase.add_student(Student(id=id, name=nama, major=jurusan))
        print("Siswa/I ditambahkan.")

    elif pilihan == '2':
        students = usecase.list_students()
        for s in students:
            print(s)

    elif pilihan == '3':
        id = int(input("ID Siswa/I: "))
        student = usecase.get_student(id)
        print(student if student else "Tidak ditemukan.")

    elif pilihan == '4':
        id = int(input("ID: "))
        nama = input("Nama baru: ")
        jurusan = input("Jurusan baru: ")
        usecase.update_student(Student(id=id, name=nama, major=jurusan))
        print("Data Siswa/I diperbarui.")

    elif pilihan == '5':
        id = int(input("ID Siswa/I yang akan dihapus: "))
        usecase.delete_student(id)
        print("Data dihapus.")

    elif pilihan == '6':
        break

    else:
        print("Pilihan tidak valid.")

