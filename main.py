from repo import PersonRepository
from service import PersonService
from controller import PersonController
from console import Console

repository = PersonRepository()
service = PersonService(repository)
controller = PersonController(service)
console = Console(controller)

console.run()
