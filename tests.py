import unittest

from game.game import Game


class TestFactorial(unittest.TestCase):

    def test_frames_quantity(self):
        game = Game()
        game.run()

        self.assertEqual(len(game.frames), 10)

    def test_strike_1_handling(self):
        """
        Frames: 1     2    3     4     5     6     7     8     9     10
               10 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 |
        10 + 1 + 1 = 12
        2 = 14
        2 = 16
        2 = 18
        2 = 20
        2 = 22
        2 = 24
        2 = 26
        2 = 28
        2 = 30
        """
        print('!!!test_strike_1_handling')
        game = Game()
        game.points = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        game.run()

        self.assertEqual(game.score, 30)

    def test_strike_2_handling(self):
        """
        Frames: 1    2    3     4     5     6     7     8     9     10
               10 | 10 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 |
        10 + 10 + 1 = 21
        10 + 1 + 1 = 33
        2 = 35
        2 = 37
        2 = 39
        2 = 41
        2 = 43
        2 = 45
        2 = 47
        2 = 49
        """
        print('!!!test_strike_2_handling')
        game = Game()
        game.points = [10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        game.run()

        self.assertEqual(game.score, 49)

    def test_strike_3_handling(self):
        """
        Frames: 1    2    3    4     5     6     7     8     9     10
               10 | 10 | 10 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 |
        10 + 10 + 10 = 30
        10 + 10 + 1 = 51
        10 + 1 + 1 = 63
        2 = 65
        2 = 67
        2 = 69
        2 = 71
        2 = 73
        2 = 75
        2 = 77
        """
        print('!!!test_strike_3_handling')
        game = Game()
        game.points = [10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        game.run()

        self.assertEqual(game.score, 77)

    def test_strike_at_end_handling(self):
        """
        Frames: 1     2     3    4     5     6     7     8     9     10
               1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 10, 10, 10 |
        2 = 2
        2 = 4
        2 = 6
        2 = 8
        2 = 10
        2 = 12
        2 = 14
        2 = 16
        2 = 18
        10 + 10 + 10 = 48
        """
        print('!!!test_strike_at_end_handling')
        game = Game()
        game.points = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10]
        game.run()

        self.assertEqual(game.score, 48)

    def test_1_spare_handling(self):
        """
        Frames: 1     2     3     4     5     6     7     8     9     10
               3,7 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 |
        (3 + 7) + 1 = 11
        2 = 13
        2 = 15
        2 = 17
        2 = 19
        2 = 21
        2 = 23
        2 = 25
        2 = 27
        2 = 29
        """
        print('!!!test_1_spare_handling')
        game = Game()
        game.points = [3, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        game.run()

        self.assertEqual(game.score, 29)

    def test_spare_2_handling(self):
        """
        Frames: 1     2     3     4     5     6     7     8     9     10
               3,7 | 3,7 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 |
        (3 + 7) + 3 = 13
        (3 + 7) + 1 = 24
        2 = 26
        2 = 28
        2 = 30
        2 = 32
        2 = 34
        2 = 36
        2 = 38
        2 = 40
        """
        print('!!!test_spare_2_handling')
        game = Game()
        game.points = [3, 7, 3, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        game.run()

        self.assertEqual(game.score, 40)

    def test_spare_at_end_handling(self):
        """
        Frames: 1     2     3    4     5     6     7     8     9     10
               1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 1,1 | 3, 7, 10 |
        2 = 2
        2 = 4
        2 = 6
        2 = 8
        2 = 10
        2 = 12
        2 = 14
        2 = 16
        2 = 18
        (3 + 7) + 10 = 38
        """
        print('!!!test_spare_at_end_handling')
        game = Game()
        game.points = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 7, 10]
        game.run()

        self.assertEqual(game.score, 38)


if __name__ == '__main__':
    unittest.main()
