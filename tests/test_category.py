import pytest
from src.Category import Category


def test_category():
    cat1 = Category('Овощи', 'полезно', ['Огурец', 'Морковь', 'Капуста', 'Тыква'])
    assert cat1.title == 'Овощи'
    assert cat1.description == 'полезно'
    assert cat1.products == ['Огурец', 'Морковь', 'Капуста', 'Тыква']
    assert cat1.amount_of_categories == 1
    assert cat1.amount_of_products == 4

    cat2 = Category("Игрушки", "для детей", ["мяч", "кукла", "машинка"])
    assert cat2.amount_of_categories == 2
    assert cat2.amount_of_products == 7

    cat3 = Category("Фрукты", "витаминизация", ["яблоко", "апельсин", "банан", "виноград"])
    assert cat3.amount_of_categories == 3
    assert cat3.amount_of_products == 11
