import unittest


class BTestCase(unittest.TestCase):

    def setUp(self):
        print(__name__, "setUp")

    def test_B(self):
        print(__name__, "test_B")
