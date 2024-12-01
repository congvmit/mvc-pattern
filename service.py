from repo import PersonRepository


class PersonService:
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def get(self, id: id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def add(self, person):
        self.repository.add(person)

    def delete(self, id: int):
        self.repository.delete(id)

    def update(self, old_person, new_person):
        self.repository.update(old_person, new_person)

    # Business logic
    def get_by_name(self, name):
        return [person for person in self.get_all() if person.name == name]

    def get_by_age(self, age):
        return [person for person in self.get_all() if person.age == age]
