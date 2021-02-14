import unittest

import main


class TestMain(unittest.TestCase):
    def test_do_stuff_1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 10)

    def test_do_stuff_3(self):
        test_param = 'test'
        result = main.do_stuff(test_param)
        self.assertEqual(result, ValueError)

    def test_do_stuff_4(self):
        test_param = 'test'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))


unittest.main()
