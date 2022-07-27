"""Test your acme modules with unittest"""
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        """Test default stealability() being 'Kinda stealable.'"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

    def test_explode(self):
        """Test default explode() being '...boom!'"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """This is report test"""
    def test_default_num_products(self):
        """Test default number of products being 30"""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test names being legal"""
        products = generate_products()
        for prod in products:
            names = prod.name.split()
            self.assertTrue(names[0] in ADJECTIVES)
            self.assertTrue(names[1] in NOUNS)


if __name__ == '__main__':
    unittest.main()
