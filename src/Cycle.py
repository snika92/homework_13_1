from Category import Category
from Product import Product


class Cycle:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value < len(self.category.products) - 1:
            self.current_value += 1
            return self.category.products[self.current_value]
        else:
            raise StopIteration


prod1 = Product("Мяч", "Футбольный", 50.50, 10)
prod2 = Product("Кукла", "Фарфоровая", 100.00, 50)
prod3 = Product("Пирамидка", "Деревянная", 70.25, 30)
cat1 = Category("Игрушки", "для детей", [prod1, prod2, prod3])


for product in Cycle(cat1):
    print(product)

