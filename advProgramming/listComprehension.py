values = [(5,1), (2,10), (3,3), (1,2)]

#values.sort()

def tuple_value(t: tuple):
    return (t[0] + t[1])/2

values.sort(key=tuple_value)

print(values)

class Student:
    def __init__(self, name: str, credits: int) -> None:
        self.name = name
        self.credits = credits

    def __repr__(self) -> str:
        return f"{self.name} has {self.credits} credits"
    
s1 = Student("Simon", 25)
s2 = Student("Roger", 26)
s3 = Student("Mario", 29)
s4 = Student("Maria", 24)

students = [s1, s2, s3, s4]

def student_item_value(student: Student):
    return student.credits

students.sort(key=lambda student: student.credits, reverse=True)

print(students)