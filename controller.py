class PersonController:
    def __init__(self, service):
        self.service = service

    def get(self, id):
        return self.service.get(id)

    def get_all(self):
        return self.service.get_all()

    def add(self, person):
        self.service.add(person)

    def update(self, old_person, new_person):
        self.service.update(old_person, new_person)

    def delete(self, id):
        self.service.delete(id)

    def get_by_name(self, name):
        return self.service.get_by_name(name)
    
    def filter_by_age(self, age):
        return self.service.filter_by_age(age)