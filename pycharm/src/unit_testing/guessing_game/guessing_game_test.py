import unittest

import guessing_game


class TestGuessingGame(unittest.TestCase):
    def test_game_1(self):
        guess = 5
        answer = 5
        result = guessing_game.run_guess(guess, answer)
        self.assertTrue(result)

    def test_game_2(self):
        guess = 5
        answer = 2
        result = guessing_game.run_guess(guess, answer)
        self.assertFalse(result)

    def test_game_3(self):
        guess = 5
        answer = 11
        result = guessing_game.run_guess(guess, answer)
        self.assertFalse(result)

    def test_game_4(self):
        guess = '5'
        answer = 11
        result = guessing_game.run_guess(guess, answer)
        self.assertIsInstance(result, TypeError)


if __name__ == '__main__':
    unittest.main()
