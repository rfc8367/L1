import csv


class Product:
    def __init__(self, name, bev_type, price):
        self.name = str(name)
        self.bev_type = bev_type
        self.price = float(price)

    @property
    def product_name(self):
        if self.name is None:
            raise NameError('Invalid selection. Please, enter name of product')
        return self.name

    @property
    def product_type(self):
        if self.bev_type == 'coffee':
            return 'coffee'
        elif self.bev_type == 'tea':
            return 'tea'
        else:
            raise NameError('Invalid selection. You have to choose coffee or tea')

    @property
    def product_price(self):
        return self.price

    def __repr__(self):
        return f'{self.name}: {self.bev_type}, Price: {self.price}'


class Store:
    def __init__(self):
        self.product_list = []
        self.transactions = []

    def add_item(self, row, quantity):
        product = Product(row['Наименование'], row['Тип'], row['Цена'])
        self.product_list = ([product] * quantity)

    def import_file(self):
        with open('inventory.csv', 'r') as inventory:
            reader = csv.DictReader(inventory)
            for row in reader:
                self.add_item(row, 5)

    def all_products(self):
        for product in self.product_list:
            product.all_product()

    def total_price(self):
        total_price = 0
        for product in self.product_list:
            total_price += product.price
        return total_price

    def sell_item(self, product):
        if product in self.product_list:
            self.transactions.append(product)
        else:
            raise NameError('Invalid item')

    def total_item(self):
        total_items = 0
        for product in self.product_list:
            total_items += product.price
        return total_items


store = Store()
store.import_file()
store.all_products()
latte_coffee = Product('Латте', "coffee", 34.0)
store.add_item(latte_coffee)
store.sell_item(latte_coffee)
store.total_item()

print(latte_coffee)
print(store.total_price())
print(store.total_item())
