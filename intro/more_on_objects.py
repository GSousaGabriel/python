from typing import Any


class Student:
    EMAIL_DOMAIN = "gmail.com"
    counter = 0
    
    def __init__(self, id: int, name: str, credits: int, email: str = "") -> None:
        self.__id = id
        
        if self.__id_ok(id):
            self.__name = name
            self.__credits = credits
            self.__validate_email(email)
            Student.counter += 1
        else:
            raise ValueError("Id invalid, can't save student data!")
        
    def better_student(self, student2: "Student") -> "Student":
        if self.credits > student2.credits:
            return self
        elif student2.credits > self.credits:
            return student2
        else:
            return None
       
    @classmethod 
    def output_school_name(cls):
        return "Gabriel's university"
        
    @property
    def id(self):
        return self.__id
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name and len(new_name) > 1:
            self.__name = new_name
        else:
          raise ValueError("name is invalid, fix and try again!")  
        
    @property
    def credits(self) -> Any:
        return self.__credits
    
    @credits.setter
    def credits(self, qtd: int) -> Any:
        if qtd >= 0:
            self.__credits = qtd
        else:
            raise ValueError('Number of credits is invalid, check and input again!')
      
    def __id_ok(self, id: str):
        if id > 0:
            return True
        return False    
      
    def __validate_email(self, email: str):
        if email:
            self.email = email + "@" + Student.EMAIL_DOMAIN
        else:
            self.email = self.name + "@" + Student.EMAIL_DOMAIN
        
    def __str__(self) -> str:
        return f"Name: {self.name}, id: {self.id}. This student has {self.credits} credits"
    
    def __repr__(self) -> str:
        return f"Student(name={self.name}, id={self.id}, credits={self.credits})"
    

class CompleteCourse:
    def __init__(self, course: str, student: Student, grade: int) -> None:
        self.course = course
        self.student = student
        self.grade = grade
    
    def __str__(self) -> str:
        return f"Course: {self.course}, student: {self.student.name}. This student got a grade of {self.grade}"
    
    def __repr__(self) -> str:
        return f"CompleteCourse(course={self.course}, student={self.student}, grade={self.grade})"
    

def output_student_name(student: Student):
    print(student.name)
    
s1 = Student(1, "Jose", 12)
s2 = Student(2, "Maria", 123)
s3 = Student(3, "Robert", 52)
s4 = Student(4, "Roberto", 52)

studentsTuple = (s1, s2, s3)
studentsList = [s1, s2, s3]

print(studentsTuple[2])
print(studentsList[0])
print(studentsTuple)
s1.credits = 100
s2.name = "Marta"

print(s1.credits)
print(s2.name)

output_student_name(s1)
print(s1.better_student(s2))
print(s3.better_student(s4))

completed = CompleteCourse("Python", s1, 3)

print("###########")
print(completed.course)
print(completed)
print(completed.student.name)
print(s1.email)

print(Student.EMAIL_DOMAIN)
print(Student.output_school_name(), "has", Student.counter, "students")