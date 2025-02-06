class Engine:
    def __init__(self, power):
        self.power = power
    def start(self):
        print(f'Engine has: {self.power} horsepower')

class Car():
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.engine = Engine(power)
    def ride(self):
        self.engine.start()
    def __str__(self):
        return f'{self.brand} {self.model} with {self.engine.power} HP'

vehicles = [
    Car('Toyota', 'Corolla', 200),
    Car('Mazda', '626', 150),
    Car('Dodge', 'Mustang', 450),
    Car('Ford', 'Focus', 180),
    Car('Audi', 'TT', 230)
]

for i in vehicles:
    print(i)
    i.ride()