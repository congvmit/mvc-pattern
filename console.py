# > person.py -> This will be our model data
# > repo.py -> Class for persistence layer that handles persons
# > service.py -> Here you can handle business logic
# > console.py -> Can be the view of your application, or presentation layer

# A Console class for PersonController
from person import Person


class Console:
    def __init__(self, controller):
        self.controller = controller

    def get_all(self):
        persons = self.controller.get_all()
        for person in persons:
            print(person.id, person.name, person.age)

    def get(self, id):
        person = self.controller.get(id)
        if person is None:
            print("Person not found")
        else:
            print(person.id, person.name, person.age)

    def add(self, name, age):
        person = Person(name, age, 0)
        self.controller.add(person)
        print("Person added")

    def update(self, id, name, age):
        person = Person(name, age, id)
        self.controller.update(self.controller.get(id), person)
        print("Person updated")

    def delete(self, id):
        self.controller.delete(id)
        print("Person deleted")

    def get_by_name(self, name):
        person = self.controller.get_by_name(name)
        if person is None:
            print("Person not found")
        else:
            print(person.id, person.name, person.age)

    def filter_by_age(self, age):
        persons = self.controller.filter_by_age(age)
        for person in persons:
            print(person.id, person.name, person.age)

    # Menu for user input
    def run(self):
        while True:
            print("1. Get all persons")
            print("2. Get person by id")
            print("3. Add person")
            print("4. Update person")
            print("5. Delete person")
            print("6. Get person by name")
            print("7. Filter person by age")
            print("8. Exit")
            print("Enter your choice: ", end="")
            choice = int(input())
            if choice == 1:
                self.get_all()
            # and other functions for your menu, you got the point
            elif choice == 2:
                print("Enter id: ", end="")
                id = int(input())
                self.get(id)
            elif choice == 3:
                print("Enter name: ", end="")
                name = input()
                print("Enter age: ", end="")
                age = int(input())
                self.add(name, age)
            else:
                print("Invalid choice")