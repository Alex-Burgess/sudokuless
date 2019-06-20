import pytest
from solve_puzzle import common


def test_get_row():
    test_puzzle = [
        [1, 2, 3, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 8, 9]
    ]

    first_row = common.get_row(test_puzzle, 0)
    assert first_row == [1, 2, 3, 0, 0, 0, 0, 0, 0], "First row did not match expected values."

    last_row = common.get_row(test_puzzle, 8)
    assert last_row == [0, 0, 0, 0, 0, 0, 7, 8, 9], "Last row did not match expected values."


def test_get_column():
    test_puzzle = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]

    first_column = common.get_column(test_puzzle, 0)
    assert first_column == [1, 2, 3, 0, 0, 0, 0, 0, 0], "First column did not match expected values."

    last_column = common.get_column(test_puzzle, 8)
    assert last_column == [0, 0, 0, 0, 0, 0, 7, 8, 9], "Last column did not match expected values."


def test_get_grid():
    test_puzzle = [
        [1, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]

    first_grid = common.get_grid(test_puzzle, 0)
    assert first_grid == [1, 2, 3, 0, 0, 0, 0, 0, 0], "First grid did not match expected values."

    last_grid = common.get_grid(test_puzzle, 8)
    assert last_grid == [0, 0, 7, 0, 0, 8, 0, 0, 9], "Last grid did not match expected values."


def test_grid_top_left_cell_number():
    grid1 = common.grid_top_left_cell_number(0)
    assert grid1 == [0, 0], "Grid 1 coordinates did not match expected values."

    grid9 = common.grid_top_left_cell_number(8)
    assert grid9 == [6, 6], "Grid 9 coordinates did not match expected values."


def test_get_grid_number():
    test_puzzle = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]

    grid_num = common.get_grid_number(test_puzzle, 0, 0)
    assert grid_num == 0, "Grid number for row 0, col 0 should be 0."

    grid_num = common.get_grid_number(test_puzzle, 1, 1)
    assert grid_num == 0, "Grid number for row 1, col 1 should be 0."

    grid_num = common.get_grid_number(test_puzzle, 2, 2)
    assert grid_num == 0, "Grid number for row 2, col 2 should be 0."

    grid_num = common.get_grid_number(test_puzzle, 3, 3)
    assert grid_num == 4, "Grid number for row 3, col 3 should be 4."

    grid_num = common.get_grid_number(test_puzzle, 8, 8)
    assert grid_num == 8, "Grid number for row 8, col 8 should be 8."


def test_cell_contains_number():
    test_puzzle = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
    result = common.cell_contains_number(test_puzzle, 0, 0)
    assert result, "Cell in row 0, col 0 countains a value."

    result = common.cell_contains_number(test_puzzle, 0, 1)
    assert not result, "Cell in row 0, col 1 does not countain a value."

    result = common.cell_contains_number(test_puzzle, 8, 8)
    assert result, "Cell in row 8, col 8 countains a value."