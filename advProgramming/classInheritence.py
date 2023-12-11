class Teacher:
    def __init__(self, name: str, email: str, hours: int) -> None:
        self.name = name
        self.email = email
        self.__hours = hours
        
    @property
    def hours(self):
        return self.__hours
        
    def __str__(self) -> str:
        return f"{self.name} ({self.email}), {self.__hours} per week"
    
class SpecialTeacher(Teacher):
    def __init__(self, name: str, email: str, hours: int, special_hours: int) -> None:
        super().__init__(name, email, hours)
        self.special_hours = special_hours
        
    # @property
    # def hours(self):
    #     return self._hours + self.special_hours
        
    def __str__(self) -> str:
        return super().__str__() + f" plus {self.special_hours} special hours"
      
        
s_teacher = SpecialTeacher("Roger", "roger@gmail.com", 21, 3)
print(s_teacher.hours)