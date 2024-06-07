class Parent:
    last_name = "Paul"

class Child(Parent):
    def __init__(self, str):
        self.first_name = str

    def show(self):
        print(f"My name is {self.first_name} {super().last_name}")

C = Child("Moinam")
C.show()
