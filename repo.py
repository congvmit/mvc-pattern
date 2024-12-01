class PersonRepository:
    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)

    def get(self, id):
        for person in self.people:
            if person.id == id:
                return person
        return None

    def get_all(self):
        return self.people

    def update(self, old_person, new_person):
        self.delete(old_person.id)
        self.add(new_person)

    def delete(self, id):
        for person in self.people:
            if person.id == id:
                self.people.remove(person)
                return
        raise Exception("Person not found")
