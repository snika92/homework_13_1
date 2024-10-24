class Category:
    amount_of_categories = 0
    amount_of_products = 0
    all = []

    def __init__(self, title: str, description: str, products: list) -> None:
        self.title = title
        self.description = description
        self.products = products

        Category.amount_of_categories += 1
        Category.amount_of_products += len(self.products)
        Category.all.append(self)

    def add_products(self, product):
        self.products.append(product)
        Category.amount_of_products += 1
