class Product:
    all = []

    def __init__(self, title: str, description: str, price: float, quantity: int):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.all.append(self)


# print(Product.all)
