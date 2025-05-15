import unittest
from domain.student import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student(id=1, name="Budi", major="TI")
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "Budi")
        self.assertEqual(student.major, "TI")

    def test_student_str(self):
        student = Student(id=2, name="Ani", major="SI")
        expected_str = "ID: 2, Nama: Ani, Jurusan: SI\n"
        self.assertEqual(str(student), expected_str)

    def test_student_attributes_mutability(self):
        student = Student(id=3, name="Cici", major="MI")
        student.name = "Citra"
        self.assertEqual(student.name, "Citra")

if __name__ == '__main__':
    unittest.main()
