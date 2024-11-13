from abc import ABC, abstractmethod

from src.Product import Product


class BaseEntity(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"{self.__class__.__name__}('{self.product.title}', {self.quantity}, {self.total_price})"
