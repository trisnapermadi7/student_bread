class Student:
    def __init__(self, id: int, name: str, major: str):
        self.id = id
        self.name = name
        self.major = major

    def __str__(self):
        return f"ID: {self.id}, Nama: {self.name}, Jurusan: {self.major}\n"

