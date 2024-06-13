<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/TheGrotShop/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/thegrotshop/black-and-white-circle-256.png" alt="TheGrotShop logo" />
    </a>
    <br />
    <a href="https://github.com/TheGrotShop/NQueens-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/TheGrotShop/NQueens-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/TheGrotShop/NQueens-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package">
        <img src="https://img.shields.io/github/created-at/TheGrotShop/NQueens-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/TheGrotShop/NQueens-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/TheGrotShop/NQueens-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/TheGrotShop/NQueens-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/TheGrotShop/NQueens-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/TheGrotShop/NQueens-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/TheGrotShop/NQueens-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

The N-Queens problem is a classic challenge often encountered in programming interviews and academic settings. The challenge is to place N
queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

## Problem Statement
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answers in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' indicates a queen and '.' indicates an empty space.

## Example
For n = 4, the possible solutions are:

```
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```
## Approach and Algorithms

### Backtracking Algorithm

The most common approach to solve the N-Queens problem is using backtracking. The backtracking algorithm incrementally builds candidates to the 
solution and abandons a candidate as soon as it determines that the candidate cannot possibly lead to a valid solution.

Steps:
1. `Initialize the Board`: Start with an empty N×N board.
2. `Place the Queen`: Try to place the queen in the first row and proceed to place subsequent queens.
3. `Check Validity`: For each queen placement, check if it conflicts with already placed queens.
4. `Backtrack if Necessary`: If placing a queen leads to no solution, remove the queen (backtrack) and try the next position.
5. `Store the Solution`: If a valid configuration is found (N queens placed), store the board configuration.
6. `Repeat`: Continue this process until all possible configurations have been tried.

### Challenges

#### Board Representation

The board can be represented using a 2D list where each cell is either 'Q' or '.'.

#### Checking Conflicts

Efficiently checking for conflicts is crucial:

1. `Row Check`: Ensuring no other queens are in the same row.
2. `Column Check`: Ensuring no other queens are in the same column.
3. `Diagonal Check`: Ensuring no other queens are on the same diagonal.

### Optimization
Using sets to track occupied columns and diagonals can speed up the conflict check process.

### Concurrency with ThreadPoolExecutor
To optimize solving the problem for larger n, the solution leverages concurrency with ThreadPoolExecutor:

* Each thread starts solving the problem for a different column in the first row.
* This parallel approach can significantly reduce the time to find all solutions.

## Our Solution

This solution came frome one of our *Free Friday Challenges*, where we pick random interview challenges during our downtime to write solutions to.

### Installation

```
pip install wolfsoftware.NQueens
```

### Usage

```
usage: nqueens [-h] [-v] [-V] [board_size]

See solutions to the NQueens problem.

positional arguments:
  board_size     Size of the board (default is 8 for the Eight Queens puzzle) (default: 8)

flags:
  -h, --help     Show this help message and exit
  -v, --verbose  Enable verbose output - show the actual boards (default: False)
  -V, --version  Show program's version number and exit.

The N Queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other.
```

## Summary
The N-Queens problem is a fascinating and complex challenge that requires a deep understanding of recursion, backtracking, and optimization techniques.
By leveraging multi-threading, this implementation efficiently finds all possible solutions for a given board size. Understanding and implementing the
N-Queens problem is a valuable exercise for improving problem-solving skills and algorithmic thinking.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
