import main
import numpy
import unittest



class Test_functions(unittest.TestCase):
    def test_make_a_move(self):
        array = numpy.zeros([main.ROW_COUNT, main.COLUMN_COUNT])
        test_array = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 0]]
        main.make_a_move(array, -1, 0)
        for i in range(main.ROW_COUNT):
            for j in range(main.COLUMN_COUNT):
                self.assertEqual(array[i][j], test_array[i][j])

    def test_next_turn(self):
        self.assertEqual(main.next_turn(main.PLAYER), main.AI)

    def test_winning_move(self):
        test_array = [[0, 0, 0, 0, -1, 1, -1],
                      [0, 0, 0, 0, 0, -1, 1],
                      [0, 0, 0, 0, 0, 1, 1],
                      [0, 0, 0, 0, 1, -1, -1],
                      [0, 0, 0, 1, -1, 1, -1],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        self.assertTrue(main.winning_move(test_array, 1))

    def test_check_draw(self):
        test_array = [[0, 0, 0, 0, 0, 0, 0],
                      [1, 1, -1, 1, -1, 1, -1],
                      [1, 1, -1, 1, -1, 1, -1],
                      [1, -1, 1, -1, 1, -1, 1],
                      [-1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1],
                      [-1, 1, -1, 1, -1, 1, -1]]
        self.assertFalse(main.check_draw(test_array))

    def test_make_a_move_ai(self):
        test_array = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0]]
        array = numpy.zeros([main.ROW_COUNT, main.COLUMN_COUNT])
        main.make_a_move_ai(array, 6, 3, main.AI)
        for i in range(main.COLUMN_COUNT):
            for j in range(main.ROW_COUNT):
                self.assertEqual(array[i][j], test_array[i][j])

    def test_list_valid_locations(self):
        valid_locations = [0, 1, 2, 3, 4, 5, 6]
        test_valid_locations = []
        test_array = numpy.zeros([main.ROW_COUNT, main.COLUMN_COUNT])
        self.assertEqual(valid_locations, main.list_valid_locations(test_array))

    def test_check_valid_location(self):
        test_array = numpy.zeros([main.ROW_COUNT, main.COLUMN_COUNT])
        for i in range(main.ROW_COUNT):
            self.assertTrue(main.check_valid_location(test_array, i))


if __name__ == '__main__':
    unittest.main()
