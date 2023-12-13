class Person:
    def __init__(self,name, age=0,location=""):
        self.name = name
        self.age = age
        self.location = location

    def get_person(self):
        print(f"you are {self.name},and {self.age} years old. and stays at {self.location}")
    
    def eat(self,food):
        print(f"{self.name} is Eating {food}")
        
    def sleep(self):
        print(f"{self.name} is sleeping......")
        

class Ama(Person):
    def __init__(self):
        super().__init__(age=24,name="Ama",location="Accra")
        self.favorite_food = "rice"
        self.dress_color = "blue"
        
    def __eat(self):
        return super().eat("rice")
        

make_person = Ama()
make_person.get_person()
make_person._Ama__eat()
        
        