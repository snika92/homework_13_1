from src.Product import Product
from src.Order import BaseEntity


class Category(BaseEntity):
    amount_of_categories = 0
    amount_of_products = 0
    all = []

    def __init__(self, title: str, description: str, products=None) -> None:
        self.title = title
        self.description = description
        if products is None:
            self.__products = []
        else:
            self.__products = products

        Category.amount_of_categories += 1
        Category.amount_of_products += len(self.__products)
        Category.all.append(self)

    def __len__(self):
        quantity_of_products = 0
        for product in self.__products:
            quantity_of_products += product.quantity
        return quantity_of_products

    def __str__(self):
        return f"{self.title}, количество продуктов: {self.__len__()} шт."

    @property
    def products(self):
        list_of_products = []
        for product in self.__products:
            list_of_products.append(f"{product.title}, {product.price} руб. Остаток: {product.quantity} шт.")
        return list_of_products
        # return self.__products

    # @products.setter
    # def products(self, obj_product):
    #     self.__products.append(obj_product)
    #     Category.amount_of_products += 1

    def add_product(self, product: Product):
        """ Add product to products list """
        if not issubclass(type(product), Product):
            raise TypeError
        if product not in self.__products:
            self.__products.append(product)
            Category.amount_of_products += 1


# prod1 = Product("Мяч", "Футбольный", 50.50, 10)
# prod2 = Product("Кукла", "Фарфоровая", 100.00, 50)
# prod3 = Product("Пирамидка", "Деревянная", 70.25, 30)
# cat1 = Category("Игрушки", "для детей", [prod1, prod2, prod3])
#
# # print(Category.amount_of_categories)
# # print(Category.amount_of_products)
# # print(Category.all)
# #
# # print(cat1.products)
# prod4 = Product("Машинка", "Легковая", 100.00, 150)
# print(prod4)
# print(cat1)
# cat1.products = prod4
# print(cat1.products)
# print(cat1)
