from domain.student_controller import StudentController
from domain.student import Student

class InMemoryStudentController(StudentController):
    def __init__(self):
        self.students = {}

    def add(self, student: Student):
        self.students[student.id] = student

    def get(self, student_id: int) -> Student:
        return self.students.get(student_id)

    def get_all(self):
        return list(self.students.values())

    def update(self, student: Student):
        if student.id in self.students:
            self.students[student.id] = student

    def delete(self, student_id: int):
        if student_id in self.students:
            del self.students[student_id]
