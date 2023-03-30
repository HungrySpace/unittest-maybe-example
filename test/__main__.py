import unittest

from test_a import ATestCase
from test_b import BTestCase
from test_c import CTestCase


def migrations_db():
    pass


def drop_db():
    pass


def run_all_test():
    test_loader = unittest.TestLoader()
    test_classes = [
        ATestCase,
        BTestCase,
        CTestCase
    ]

    suites = []
    for test_class in test_classes:
        suite = test_loader.loadTestsFromTestCase(test_class)
        suites.append(suite)

    big_suite = unittest.TestSuite(suites)
    unittest.TextTestRunner().run(big_suite)


if __name__ == '__main__':
    migrations_db()
    run_all_test()
    drop_db()
