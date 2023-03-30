import unittest


class ATestCase(unittest.TestCase):

    def setUp(self):
        print(__name__, "setUp")

    def test_A(self):
        print(__name__, "test_A")
