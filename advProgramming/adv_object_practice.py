class Person:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self._email = email

    @property
    def email(self):
        return self._email

    def get_last_name(self):
        return self.name.split()[1]


class Student(Person):
    def __init__(self, name: str, email: str, credits: str) -> None:
        super().__init__(name, email)
        self.credits = credits

    def get_credits(self):
        return self.credits

    def __str__(self):
        return f"{self.name}'s email is {self.email}"

    def __gt__(self, other_student: "Student"):
        if self.credits > other_student.credits:
            return True
        else:
            return False


class ExchangeStudent(Student):
    def __init__(self, name: str, email: str, credits: str, exCredits) -> None:
        super().__init__(name, email, credits)
        self.credits = credits
        self.exCredits = exCredits

    def get_credits(self):
        return self.exCredits


class Teacher(Person):
    def __init__(self, name: str, email: str, room: str) -> None:
        super().__init__(name, email)
        self.room = room


s = Student("Simon Simoleans", "simo@test.com", 123)
s2 = Student("Simone Simoleanes", "simone@test.com", 33)

if s > s2:
    print('s1 is better')

print(s.name, s.email, s.credits, s.get_last_name())

print(s)

e = ExchangeStudent("Simon Simoleans", "simo@test.com", 123, 1)

print(e.name, e.email, e.credits, e.get_credits())

print('--------------------------------')


class Box:
    def __init__(self, item: str) -> None:
        self.item = item

    def __str__(self) -> str:
        return f"Box(item={self.item})"


class Warehouse:
    def __init__(self) -> None:
        self.__boxes = []

    def add(self, box: Box):
        self.__boxes.append(box)

    def add_many(self, *boxes):
        for _, fruta in enumerate(boxes):
            self.add(fruta)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.__boxes):
            self.counter += 1
            return self.__boxes[self.counter -1 ]
        else:
            raise StopIteration


b1 = Box("Carrots")
b2 = Box("Banana")
b3 = Box("Apples")
b4 = Box("Oranges")

w = Warehouse()
w.add_many(b1, b2, b3, b4)

for box in w:
    print(box)
