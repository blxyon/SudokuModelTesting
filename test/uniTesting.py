import unittest
import operator
import numpy as np
import modules.app.sudoku_ortools as sor


sudokus = np.load("data/sudokus.npy")
solutions = np.load("data/sudoku_solutions.npy")

class TestSudoku(unittest.TestCase):
    def test_easy(self):
        r = range(0,5)
        for i in r:
            sudoku = sudokus[i].copy()
            sudoku_solved=sor.sudoku_solver(sudoku)
            np.testing.assert_array_equal(solutions[i], sudoku_solved)
            
    def test_medium(self):
        r = range(5,10)
        for i in r:
            sudoku = sudokus[i].copy()
            sudoku_solved=sor.sudoku_solver(sudoku)
            np.testing.assert_array_equal(solutions[i], sudoku_solved)
    def test_invalid(self):
        r=range(10,15)
        for i in r:
            sudoku = sudokus[i].copy()
            sudoku_solved=sor.sudoku_solver(sudoku)
            np.testing.assert_array_equal(solutions[i], sudoku_solved)

    def test_complex(self):
        r=range(15,20)
        for i in r:
            sudoku = sudokus[i].copy()
            sudoku_solved=sor.sudoku_solver(sudoku)
            np.testing.assert_array_equal(solutions[i], sudoku_solved)

    # def test_divide(self):
    #     self.assertEqual(calc.divide(10, 5), 2)
    #     self.assertEqual(calc.divide(-1, 1), -1)
    #     self.assertEqual(calc.divide(-1, -1), 1)
    #     self.assertEqual(calc.divide(5, 2), 2.5)

    #     with self.assertRaises(ValueError):
    #         calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
# # Load sudokus
# sudokus = np.load("data/sudokus.npy")
# #print("Shape of one sudoku array:", sudokus[0].shape, ". Type of array values:", sudokus.dtype)

# # Load solutions
# solutions = np.load("data/sudoku_solutions.npy")

# r=range(0,20)
# for i in r:
# 	sudoku = sudokus[i].copy()
# 	print("This is sudoku number", i)
# 	print(sudoku)
# 	print("This is solution for s number", i)
# 	print(solutions[i])
# 	your_solution=swor.sudoku_solver(sudoku)
# 	print("This is your solution for sudoku number", i)
# 	print(your_solution)
# 	print("Is your solution correct?")
# 	print(np.array_equal(your_solution, solutions[i]))

# for i in r:
# 	sudoku = sudokus[i].copy()
# 	print("This is sudoku number", i)
# 	print(sudoku)
# 	print("This is solution for s number", i)
# 	print(solutions[i])
# 	your_solution=sor.solveSudoku(sudoku)
# 	print("This is your solution for sudoku number", i)
# 	print(your_solution)
# 	print("Is your solution correct?")
# 	print(np.array_equal(your_solution, solutions[i]))
