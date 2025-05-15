from abc import ABC, abstractmethod
from typing import List
from domain.student import Student

class StudentController(ABC):
    @abstractmethod
    def add(self, student: Student): pass

    @abstractmethod
    def get(self, student_id: int) -> Student: pass

    @abstractmethod
    def get_all(self) -> List[Student]: pass

    @abstractmethod
    def update(self, student: Student): pass

    @abstractmethod 
    def delete(self, student_id: int): pass
