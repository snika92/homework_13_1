import json
import os
from src.Category import Category
from src.Product import Product


product_file = os.path.join('..', 'src', 'products.json')


def make_objects(file):
    with open(file, encoding='utf8') as json_file:
        data = json.load(json_file)
    for category in data:
        list_of_products = []
        for product in category["products"]:
            prod_obj = Product(product["name"], product["description"], product["price"], product["quantity"])
            list_of_products.append(prod_obj)
        cat_obj = Category(category["name"], category["description"], list_of_products)
    # print(cat_obj.all)
    # print(list_of_products)
    # print(prod_obj.all)


make_objects(product_file)
