class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def move(self):
        print(f'{self.name} ({self.age}) is moving')

class Cat(Animal):
    def says_meow(self):
        print(f'{self.name} says MEOW!!')

class Dog(Animal):
    def barks(self):
        print(f'{self.name} barks AU AU!')

cat = Cat('Pepermint', '2years old')
cat.move()
cat.says_meow()
dog = Dog('Rex', '5years old')
dog.move()
dog.barks()

