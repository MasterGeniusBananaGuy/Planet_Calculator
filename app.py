import os
import time
import json
import math



class calculator:
    def __init__(self, laan, density):           # laan = la : laser | an : angle
        os.system('cls')
        self.laan = laan
        self.density = density
    
    def Radius(self):
        try:
            self.radius = 360 / self.laan / math.pi / 2
            return self.radius
        except TypeError:
            print(f"Program only supports integers or floats \nGiven were the types: {type(self.laan), type(self.density)}")
            pass
            

    def Diameter(self):
        self.diameter = calculator.Radius(self) * 2
        return self.diameter

    def Circumference(self):
        self.circumference = 2 * math.pi * calculator.Radius(self)
        return self.circumference

    def Volume(self):
        self.volume = calculator.Radius(self) ** 3 * math.pi * 4/3
        return self.volume

    def Mass(self):
        self.mass = calculator.Volume(self) / self.density / 1000
        return self.mass

    def Surface(self):
        self.surface = 4 * math.pi * calculator.Radius(self)
        return self.surface



class Planet:
    def __init__(self, name, density, laan):
        os.system('cls')
        self.name = name
        self.density = density
        self.laan = laan
        self.file = 'Test/saves.json'


    def load(self):
        with open(self.file, 'r') as f:
            saves = json.load(f)
            planets = saves["planets"]
            self.planets = []
            for x in planets:
                self.planets.append(x)
            return self.planets


    def create(self):
        c = calculator(laan=self.laan, density=self.density)
        self.name = self.name
        self.radius = c.Radius()
        self.diameter = c.Diameter()
        self.circumference = c.Circumference()
        self.volume = c.Volume()
        self.mass = c.Mass()
        self.surface = c.Surface()
        self.planet = {'name': self.name, 'Radius': self.radius, 'Diameter': self.diameter, 'Circumference': self.circumference, 'Mass': self.volume, 'Volume': self.mass, 'Surface': self.surface}
        return self.planet


    def save(self):
        def read_json(filename):
            with open(filename, 'r') as f:
                return json.load(f)

        def write_json(filename, data):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        data = read_json(self.file)
        data['planets'].append(self.planet)

        write_json(self.file, data)
            



P = Planet(name="planet_2", density=1680, laan=0.007823236)
#P1 = P.create()
l = P.load()

print(l)