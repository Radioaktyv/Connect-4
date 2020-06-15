import main
import unittest
import numpy


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

         self.assertTrue(main.winning_move(test_array, 1))
     def test_check_draw(self):
         test_array =  [[ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0, -1,  1, -1,  1, -1,  1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1],
                        [ 0,  1, -1,  1, -1,  1, -1]]
         self.assertFalse(main.check_draw(test_array))
if __name__ == '__main__':
    unittest.main()
