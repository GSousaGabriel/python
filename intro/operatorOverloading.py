class Box:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        
    # add def __add__(elf, another):
    # subt def __sub__(elf, another):
    # mult def __mul__(elf, another):
    # divid(floating point result) def __truediv__(elf, another):
    # divid(integer result) def __floordiv__(elf, another):
    
    def __add__(self, other: "Box"):
        return f"The combined height of this boxes is {sum([self.height, other.height])}"
        
    def __str__(self) -> str:
        return f"This box is {self.height} x {self.width}"
    
b1 = Box(23, 30)
b2 = Box(12, 51)

print(b1+b2)

print('####################################')

class Teacher:
    def __init__(self, name: str, email: str, hours: int) -> None:
        self.name = name
        self.email = email
        self.__hours = hours
        
    @property
    def hours(self):
        return self.__hours
    
    # less than def __lt__(elf, another):
    # greater than def __gt__(elf, another):
    # = to def __eq__(elf, another):
    # != to def __ne__(elf, another):
    # less than or = to def __le__(elf, another):
    # greater than or = to def __gt__(elf, another):
    
    def __gt__(self, other: "Teacher"):
        if self.__hours > other.hours:
            return True
        return False
        
    def __str__(self) -> str:
        return f"{self.name} ({self.email}), {self.__hours} per week"
    
    
t1 = Teacher("Roger", "roger@gmail.com", 21)
t2 = Teacher("Maria", "maria@gmail.com", 31)

if t1 > t2:
    print("t1 is more hard working")
else:
    print("t2 is more hard working")
    