# Task 1

class Country(object):
    def __init__(self, name: str, population: int, capital: str):
        self.name = name 
        self.population = population
        self.capital = capital

    def __str__(self):
        return f"{self.name} population is {self.population} and capital is {self.capital}."
    def increase_population(self, increase_value: int):
        self.population = self.population + increase_value
        return self.population
japan = Country('Japan', 14000000, 'Tokyo')
print(japan)
print(japan.increase_population(100000))
print(japan)    

# Task 2

class Country(object):
    def __init__(self, name: str, population: int): # creating first country 
        self.name = name
        self.population = population
    def add(self, another_country):                 # creating fuction that combines two countries
        self.name = f'{self.name} {another_country.name}'    # combining names
        self.population = self.population + another_country.population  # combining population
        return self
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)    # implement the new method of combining two countries
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)

# Task 3

class Country(object):
    def __init__(self, name: str, population: int) -> None:
        self.name = name
        self.population = population

    def __add__(self, another_country):
        self.name = f'{self.name} {another_country.name}'
        self.population = self.population + another_country.population
        return self
    
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)   

# Task 4

class Car(object):                                       
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, increase_value: int):  # creating function that increases speed
        self.speed = self.speed + increase_value
        return self.speed
    def break_(self, decrease_value: int):      # creating fuction that decreases speed
        if self.speed >= decrease_value:        # checking if decreased speed more than 0 - the speed can't be a negative number
            self.speed = self.speed - decrease_value
        else:
            self.speed = 0                     # if speed less than decrease value, decreased speed is always 0, avoiding negative numbers 
        return self.speed                 
my_honda = Car('Honda', 'Civic', 2012, 70)        
print(my_honda.accelerate(5))
print(my_honda.break_(5))


