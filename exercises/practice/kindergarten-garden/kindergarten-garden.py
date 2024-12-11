import plants as p
while True:
    try:
        student_name=input("Insert the name of the student: ").strip().lower().title()
        if student_name.isdigit():
            raise ValueError("The name hasn't be composed by numbers!")
        if student_name not in p.students:
            raise ValueError("The name has to be in the list of students!")
    except ValueError as e:
        print(f"Error,{e}")
    else:
        break
class Garden:
    def __init__(self,name,inventory):
        self.name=name
        self.inventory=inventory
    def plants(self):
        student_plants=self.inventory[self.name]
        print(f"The student {self.name} has these plants: ")
        for plant in student_plants:
            print(p.plants[plant].title(), end="  ")

class_1=Garden(student_name,p.inventory)
class_1.plants()
