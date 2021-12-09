class Test:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def print_details(self):
        print(f"{self.name} is {self.age} and lives in {self.location}")

test = Test("Carly", 28, "Los Angeles")

test.print_details()