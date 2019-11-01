#!/usr/bin/env python

from random import randint, sample, uniform, choice
from acme import Product


def generate_products(num_items=30):
    """generate a given number of products (default 30),
        randomly, and return them as a list

    Keyword Arguments:
        num_items {int} -- [nummber of products to be generated]
        (default: {30})

    Returns:
        [list] -- [list of objects, all products]
    """
    adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    products = []
    for item in range(num_items):
        products.append(
            Product(
                name=f"{choice(adj)} {choice(noun)}",
                weight=randint(5, 100),
                price=randint(5, 100),
                flammability=uniform(0.0, 2.5)
            )
        )
    return products


def inventory_report(products):
    """
        takes a list of products, and prints a "nice" summary of
        Number of unique product names in the product list
        Average (mean) price, weight, and flammability of listed products
    """
    names = []
    prices = []
    weights = []
    flame_levels = []
    for item in products:
        names.append(item.name)
        prices.append(item.price)
        weights.append(item.weight)
        flame_levels.append(item.flammability)
    avg_price = (sum(prices) / len(prices))
    avg_weight = (sum(weights) / len(weights))
    avg_flammability = (sum(flame_levels) / len(flame_levels))
    print(f'ACME CORPORATION OFFICIAL INVENTORY REPORT'
           f'\nUnique product names: {len(set(names))}'
            f'\nAverage price: {avg_price}'
            f'\nAverage weight: {avg_weight}'
            f'\nAverage flammability: {avg_flammability}')


# Useful to use with random.sample to generate names #But I did it difdferently
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

if __name__ == '__main__':
    inventory_report(generate_products())
