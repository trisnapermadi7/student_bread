from infrastructures.in_memory_student_controller import InMemoryStudentController

class StudentUseCase:
    def __init__(self, controller: InMemoryStudentController):
        self.controller = controller

    def add_student(self, student):
        if self.controller.get(student.id):
            raise ValueError("Student already exists")
        self.controller.add(student)

    def get_student(self, student_id):
        return self.controller.get(student_id)

    def update_student(self, student):
        if self.controller.get(student.id) is None:
            self.controller.add(student)
        else:
            self.controller.update(student)

    def delete_student(self, student_id):
        self.controller.delete(student_id)

    def list_students(self):
        return self.controller.get_all()
