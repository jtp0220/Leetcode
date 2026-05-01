from typing import *
from solution import Solution
class Test:
  solution = Solution()
  problems: dict = {}

  # ============================ PRINT METHODS ============================
  @staticmethod
  def _print_header(problem_name: str):
    max_length = 100
    header_length = max_length - len(problem_name)
    header_piece = "=" * (header_length // 2) if header_length > 0 else "====="
    print(f"{header_piece} [{problem_name}] {header_piece}\n")
 
  @staticmethod 
  def _print_example_header(number: int):
    print(f"{'-' * 20} Example {number} {'-' * 20}")
  
  @staticmethod
  def _print_result(output: str, expected: str = ""):
    print(f"Output: {output}\n" + (f"Expected: {expected}\n" if expected is not None else ""))

  # ============================ TEST METHODS ============================
  @staticmethod
  def _test1679():
    Test._print_header("1679. Max Number of K-Sum Pairs")

    nums = [
      [1,2,3,4],
      [3,1,3,4,3]
    ]
    
    k = [5,6]
    expected = [2, 1]
    
    for i, _ in enumerate(nums):
      Test._print_example_header(i + 1)
      result = Test.solution.maxOperations(nums[i], k[i])
      Test._print_result(result, expected[i])

  @staticmethod
  def _test238():
    Test._print_header("238. Product of Array Except Self")
    nums = [
      [1,2,3,4],
      [-1, 1, 0, -3, 3],
      [0,0]
    ]

    expected = [
      [24,12,8,6],
      [0,0,9,0,0],
      [0,0]
    ]
    for i, _ in enumerate(nums):
      Test._print_example_header(i + 1)
      result = Test.solution.productExceptSelf(nums[i])
      Test._print_result(result, expected[i])
  
  @staticmethod
  def _test643():
    Test._print_header("643. Maximum Average Subarray I")
    nums = [
      [1,12,-5,-6,50,3],
      [5]
    ]

    k = [4,1]

    expected = ["12.75000", "5.00000"]
    
    for i, _ in enumerate(nums):
      Test._print_example_header(i + 1)
      result = Test.solution.findMaxAverage(nums[i], k[i])
      Test._print_result(result, expected[i])

  @staticmethod
  def _test6():
    Test._print_header("6. Zigzag Conversion")
    s = ["PAYPALISHIRING", "PAYPALISHIRING"]
    numRows = [3, 4]
    expected = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI"]
    
    for i, _ in enumerate(s):
      Test._print_example_header(i + 1)
      result = Test.solution.convert(s[i], numRows[i])
      Test._print_result(result, expected[i])

  @staticmethod
  
  def _test1207():
    Test._print_header("1207. Unique Number of Occurrences")
    
    arr = [
      [1,2,2,1,1,3]
    ]
    
    expected = [True]
    
    for i, _ in enumerate(arr):
      Test._print_example_header(i + 1)
      result = Test.solution.uniqueOccurrences(arr[i])
      Test._print_result(result, expected[i])
    
  def _test1657():
    Test._print_header("1657. Determine if Two Strings Are Close")
    
    words = [
      ["abc", "bca"],
      ["a", "aa"]
    ]    
    
    expected = [True, False]
    
    for i, _ in enumerate(words):
      Test._print_example_header(i + 1)
      result = Test.solution.closeStrings(words[i][0], words[i][1])
      Test._print_result(result, expected[i])

  def _test2352():
    Test._print_header("2352. Equal Row and Column Pairs")
    
    grid = [
      [
        [3,2,1],
        [1,7,6],
        [2,7,7]
      ],
      [
        [3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]
      ],
      [
        [3,1,2,2],
        [1,4,4,4],
        [2,4,2,2],
        [2,5,2,2]
      ]
    ]

    expected = [1,3,3]
    
    for i, _ in enumerate(grid):
      Test._print_example_header(i + 1)
      result = Test.solution.equalPairs(grid[i])
      Test._print_result(result, expected[i])
      
  def _test2390():
    Test._print_header("2390. Removing Stars From a String")
    
    s = [
      "leet**cod*e",
      "erase*****",
    ]
    
    expected = [
      "lecoe",
      ""
    ]

    for i, _ in enumerate(s):
      Test._print_example_header(i + 1)
      result = Test.solution.removeStars(s[i])
      Test._print_result(result, expected[i])

  def _test735():
    Test._print_header("735. Asteroid Collision")
    
    asteroids = [
      [5,10,-5],
      [8,-8],
      [10,2,-5]
    ]
    
    expected = [
      [5,10],
      [],
      [10]
    ]

    for i, _ in enumerate(asteroids):
      Test._print_example_header(i + 1)
      result = Test.solution.asteroidCollision(asteroids[i])
      Test._print_result(result, expected[i])
    
  # ============================ STORE PROBLEMS ============================ 
  problems[1679] = _test1679
  problems[238] = _test238
  problems[643] = _test643
  problems[6] = _test6
  problems[1207] = _test1207
  problems[1657] = _test1657
  problems[2352] = _test2352
  problems[2390] = _test2390
  problems[735] = _test735
  
  @staticmethod
  def show_problems():
    print("=" * 55)
    print("Problems: ")
    row_size = 10
    keys = list(Test.problems.keys())

    for i, key in enumerate(keys):
      if i == len(keys) - 1:
        end = "\n"
      elif (i + 1) % row_size == 0:
        end = " "
      else:
        end = ", "

      print(key, end=end)
      
      if (i + 1) % row_size == 0 and i < len(keys) - 1:
        print()
    
  @staticmethod
  def run(problem: int):
    try:
      Test.problems[problem]()
    except Exception as e:
      print(f"{problem} threw {e}\n")  
  