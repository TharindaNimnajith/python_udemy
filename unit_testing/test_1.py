import unittest

import main


class TestMain(unittest.TestCase):
    def test_do_stuff_1(self):
        print('test_do_stuff_1_')
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        print('test_do_stuff_2_')
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertNotEqual(result, 10, msg='Negative test case!')

    def test_do_stuff_3(self):
        print('test_do_stuff_3_')
        test_param = 'test'
        result = main.do_stuff(test_param)
        self.assertNotEqual(result, ValueError)

    def test_do_stuff_4(self):
        print('test_do_stuff_4_')
        test_param = 'test'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff_5(self):
        print('test_do_stuff_5_')
        test_param = 'test'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_6(self):
        print('test_do_stuff_6_')
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number.')

    def test_do_stuff_7(self):
        print('test_do_stuff_7_')
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number.')

    def test_do_stuff_8(self):
        print('test_do_stuff_8_')
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()


# run single test files
# py test_1.py
# py test_2.py

# run all test files
# py -m unittest
# py -m test

# -v means verbose
# py test_1.py -v
# py test_2.py -v
# py -m unittest -v
# py -m test -v
