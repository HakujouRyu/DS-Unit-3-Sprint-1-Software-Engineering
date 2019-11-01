#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_explode(self):
        """Test default product explode being '...boom!'."""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')

    def test_default_product_stealability(self):
        """Test default product stealability being 'Kinda stealable.'."""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_num_products(self):
        """which checks that it really does receive a list of length 30"""
        report = generate_products()
        self.assertEqual(len(report), 30)

    def test_legal_names(self):
        """which checks that the generated names"""
        report = generate_products()
        self.assertIn(report[0].name.split()[0], (NOUNS + ADJECTIVES))


if __name__ == '__main__':
    unittest.main()
