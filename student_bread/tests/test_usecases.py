import unittest
from domain.student import Student
from usecases.student_usecase import StudentUseCase
from infrastructures.in_memory_student_controller import InMemoryStudentController

class TestStudentUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryStudentController()
        self.usecase = StudentUseCase(self.repo)

    # === ADD ===
    def test_add_student_success(self):
        student = Student(id=1, name="Budi", major="TI")
        self.usecase.add_student(student)
        self.assertEqual(self.repo.get(1), student)

    def test_add_duplicate_student(self):
        student = Student(id=2, name="Ani", major="SI")
        self.usecase.add_student(student)
        with self.assertRaises(ValueError):
            self.usecase.add_student(student)

    def test_add_multiple_students(self):
        students = [
            Student(id=3, name="Joko", major="MI"),
            Student(id=4, name="Sari", major="TI"),
        ]
        for s in students:
            self.usecase.add_student(s)
        self.assertEqual(len(self.repo.get_all()), 2)
    

    # === READ ===
    def test_get_existing_student(self):
        student = Student(id=5, name="Andi", major="SI")
        self.repo.add(student)
        result = self.usecase.get_student(5)
        self.assertEqual(result.name, "Andi")

    def test_get_nonexistent_student(self):
        result = self.usecase.get_student(999)
        self.assertIsNone(result)

    def test_get_student_after_add(self):
        student = Student(id=6, name="Rina", major="MI")
        self.usecase.add_student(student)
        self.assertEqual(self.usecase.get_student(6).major, "MI")

    # === BROWSE ===
    def test_list_students_empty(self):
        result = self.usecase.list_students()
        self.assertEqual(len(result), 0)

    def test_list_students_single(self):
        student = Student(id=7, name="Doni", major="SI")
        self.usecase.add_student(student)
        result = self.usecase.list_students()
        self.assertEqual(len(result), 1)

    def test_list_students_multiple(self):
        self.usecase.add_student(Student(id=8, name="Nina", major="TI"))
        self.usecase.add_student(Student(id=9, name="Yusuf", major="MI"))
        result = self.usecase.list_students()
        self.assertEqual(len(result), 2)

    # === UPDATE ===
    def test_update_existing_student(self):
        student = Student(id=10, name="Eka", major="TI")
        self.repo.add(student)
        updated = Student(id=10, name="Eka Updated", major="SI")
        self.usecase.update_student(updated)
        self.assertEqual(self.repo.get(10).name, "Eka Updated")

    def test_update_nonexistent_student(self):
        student = Student(id=11, name="Ghost", major="Unknown")
        self.usecase.update_student(student)
        self.assertEqual(self.repo.get(11).name, "Ghost")  # add if not exist

    def test_update_student_major_only(self):
        student = Student(id=12, name="Arif", major="TI")
        self.repo.add(student)
        updated = Student(id=12, name="Arif", major="SI")
        self.usecase.update_student(updated)
        self.assertEqual(self.repo.get(12).major, "SI")

    # === DELETE ===
    def test_delete_existing_student(self):
        student = Student(id=13, name="Lina", major="MI")
        self.repo.add(student)
        self.usecase.delete_student(13)
        self.assertIsNone(self.repo.get(13))

    def test_delete_nonexistent_student(self):
        self.usecase.delete_student(999)  # should not raise error
        self.assertIsNone(self.repo.get(999))

    def test_delete_after_add(self):
        student = Student(id=14, name="Tomi", major="TI")
        self.usecase.add_student(student)
        self.usecase.delete_student(14)
        self.assertIsNone(self.usecase.get_student(14))

if __name__ == '__main__':
    unittest.main()
