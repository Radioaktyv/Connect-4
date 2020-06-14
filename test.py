import main
import unittest
import numpy
class TestColors(unittest.TestCase):
    def setUp(self):
        self.color = main.Colors()

    def test_BLACK(self):
        self.assertEqual(self.color.BLACK, (0, 0, 0))

    def test_BLUE(self):
        self.assertEqual(self.color.BLUE, (0, 0, 255))

    def test_RED(self):
        self.assertEqual(self.color.RED, (255, 0, 0))

    def test_YELLOW(self):
        self.assertEqual(self.color.YELLOW, (255, 255, 0))

    def test_BACKGROUND(self):
        self.assertEqual(self.color.BACKGROUND, (0, 0, 123))

    def test_CHOICE_BACKGROUND(self):
        self.assertEqual(self.color.CHOICE_BACKGROUND, (0, 150, 255))


class test_functions(unittest.TestCase):
     def test_make_a_move(self):
        array = numpy.zeros([main.ROW_COUNT, main.COLUMN_COUNT])
        test_array = [[0, 0, 0, 0, 0, 0, -1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        main.make_a_move(array, -1, 0)
        for i in range(main.COLUMN_COUNT):
            for j in range(main.ROW_COUNT):
                self.assertEqual(array[i][j], test_array[i][j])
     def test_next_turn(self):
         turn = 1
         self.assertEqual(-1*main.next_turn(turn), turn)
     def test_winning_move(self):
         test_array = [[ 0,  0,  0,  0, -1,  1, -1],
                        [ 0,  0,  0,  0,  0, -1,  1],
                         [ 0,  0,  0,  0,  0,  1,  1],
                         [ 0,  0,  0,  0,  1, -1, -1],
                         [ 0,  0,  0,  1, -1,  1, -1],
                         [ 0,  0,  0,  0,  0,  0,  0],
                         [ 0,  0,  0,  0, 0,  0,  0]]

         self.assertEqual(main.winning_move(test_array, 1), True)
     def test_check_draw(self):
         test_array =  [[ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0, -1,  1, -1,  1, -1,  1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1]]
         self.assertEqual(main.check_draw(test_array), False)
if __name__ == '__main__':
    unittest.main()