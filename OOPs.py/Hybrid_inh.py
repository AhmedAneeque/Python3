# Hybrid Inheritance- This is a mixture of single,multiple,mutilevel,heirachy inheritance
class Person:
    def __init__(self, name, city, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.city = city


class Sports(Person):
    def __init__(self, name, city, sports_name, **kwargs):
        super().__init__(name=name, city=city, **kwargs)
        self.sports_name = sports_name

    def display(self):
        print(self.name, self.city)
        print(self.sports_name)


class Skills(Person):
    def __init__(self, skill_set, **kwargs):
        super().__init__(**kwargs)
        self.skill_set = skill_set


class Academics(Person):
    def __init__(self, education, grade, **kwargs):
        super().__init__(**kwargs)
        self.education = education
        self.grade = grade


class Employee(Skills, Academics):
    def __init__(self, name, city, skill_set, education, grade,
                 company, designation):
        super().__init__(
            name=name,
            city=city,
            skill_set=skill_set,
            education=education,
            grade=grade
        )
        self.company = company
        self.designation = designation

    def display_data(self):
        print(self.name, self.city)
        print(self.skill_set)
        print(self.education, self.grade)
        print(self.company, self.designation)


S1 = Sports("ahmed", "Malegaon", "FootBall")
S1.display()

E1 = Employee(
    "Aneeque", "Malegaon",
    ["Python", "C", "Java", "SQL"],
    "B Tech", "A", "Google", "Developer"
)
E1.display_data()