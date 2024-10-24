import pytest
from src.Product import Product


def test_product():
    prod1 = Product('Мяч', 'для футбола', 50.5, 10)
    assert prod1.title == 'Мяч'
    assert prod1.description == 'для футбола'
    assert prod1.price == 50.5
    assert prod1.quantity == 10
