class Product:
    all = []

    def __init__(self, title: str, description: str, price: float, quantity: int):
        self.title = title
        self.description = description
        self._price = price
        self.quantity = quantity

        Product.all.append(self)

    def __str__(self):
        return f"{self.title}, {self._price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def make_product(cls, title, description, price, quantity):
        for product in cls.all:
            if product.title == title:
                print("Уже есть такой товар")
                product.quantity += quantity
                product.price = price
                return product
        prod = cls(title, description, price, quantity)
        # cls.all.append(prod)
        return prod

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self._price:
                answer = input(f"Старая цена: {self._price}, новая цена: {new_price}\nПонизить цену? Введите 'y' для подтверждения и 'n' для отмены\n")
                if answer == "y":
                    self._price = new_price
            else:
                self._price = new_price
        else:
            print("Введена некорректная цена")

    def __add__(self, other):
        return self._price * self.quantity + other._price * other.quantity

#
# prod1 = Product('Мяч', 'для футбола', 50.5, 10)
# assert prod1.title == 'Мяч'
# assert prod1.description == 'для футбола'
# assert prod1.price == 50.5
# assert prod1.quantity == 10
#
# prod2 = Product.make_product("Кукла", "Фарфоровая", 100.00, 50)
# prod3 = Product.make_product("Пирамидка", "Деревянная", 70.25, 30)
# print(prod2 + prod3)
#
# print(prod2)
# print(prod3)
# print(Product.all)
#
# prod4 = Product.make_product("Кукла", "Фарфоровая", 110.00, 30)
# print(prod4)
# print(Product.all)
#
# prod5 = Product.make_product("Пирамидка", "Деревянная", 60, 70)
# print(prod5)
# print(Product.all)
#
# prod6 = Product.make_product("Test", "Test", 60, 70)
# print(prod6)
# print(Product.all)
#
# prod1.price = 100
# print(prod1.price)
# prod1.price = 90
# print(prod1.price)
# prod1.price = 0
# print(prod1.price)
