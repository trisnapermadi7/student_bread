import unittest
from infrastructures.in_memory_student_controller import InMemoryStudentController
from domain.student import Student

class TestInMemoryStudentController(unittest.TestCase):
    def setUp(self):
        self.controller = InMemoryStudentController()

    def test_add_and_get(self):
        student = Student(id=1, name="Budi", major="TI")
        self.controller.add(student)
        self.assertEqual(self.controller.get(1), student)

    def test_get_all(self):
        self.controller.add(Student(id=1, name="A", major="X"))
        self.controller.add(Student(id=2, name="B", major="Y"))
        self.assertEqual(len(self.controller.get_all()), 2)

    def test_delete(self):
        student = Student(id=2, name="Ani", major="SI")
        self.controller.add(student)
        self.controller.delete(2)
        self.assertIsNone(self.controller.get(2))

    def test_update(self):
        student = Student(id=3, name="Joko", major="MI")
        self.controller.add(student)
        updated = Student(id=3, name="Joko Updated", major="MI")
        self.controller.update(updated)
        self.assertEqual(self.controller.get(3).name, "Joko Updated")

if __name__ == '__main__':
    unittest.main()
