"""Acme report here"""
import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Generates products"""
    products = []
    for _ in range(num_products):
        name = ADJECTIVES[random.randint(0, 4)] + \
               ' ' + \
               NOUNS[random.randint(0, 4)]

        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0., 2.5)

        prod = Product(name=name,
                       price=price,
                       weight=weight,
                       flammability=flammability)
        products.append(prod)
    return products


def inventory_report(products):
    """Reprot inventory here"""
    product_names = set()
    prod_num = len(products)
    # if prod_num <= 0:
    #     return "No products!"

    ttl_price, ttl_weight, ttl_flam = 0, 0, 0
    for prod in products:
        product_names.add(prod.name)
        ttl_price += prod.price
        ttl_weight += prod.weight
        ttl_flam += prod.flammability

    avg_price = ttl_price / prod_num
    avg_weight = ttl_weight / prod_num
    avg_flam = ttl_flam / prod_num

    report = (len(product_names), avg_price, avg_weight, avg_flam)

    return report


if __name__ == '__main__':
    print(inventory_report(generate_products()))
