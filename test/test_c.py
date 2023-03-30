import unittest


class CTestCase(unittest.TestCase):

    def setUp(self):
        print(__name__, "setUp")

    def test_C(self):
        print(__name__, "test_B")
