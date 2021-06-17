from random import randint


class House:
    def __init__(self, number):
        self.number = number
        self.population = randint(1, 100)


class Street:
    def __init__(self, number):
        self.number = number
        self.houses = []
        self.house_gen()

    def house_gen(self):
        for i in range(randint(5, 20)):
            self.houses.append(House(i))

    def add_house(self, name):
        house = House(self)
        self.houses[name] = house
        return house


class City:
    def __init__(self, name):
        self.name = name
        self.streets = []
        self.street_gen()

    def street_gen(self):
        for i in range(randint(1, 10)):
            self.streets.append(Street(i))

    def remove_street(self, name):
        del self.streets[name]

    def add_street(self, name):
        street = Street(self)
        self.streets[name] = street
        return street

    def city_table(self):
        print(self.name)
        print('Street', 'House', 'Population')
        for street in self.streets:
            for house in street.houses:
                print(f'{street.number}      {house.number}      {house.population}')


city = City('The US is going metric inch by inch... ')
city.city_table()
