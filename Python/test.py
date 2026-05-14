from typing import *
from solution import Solution
import traceback
from ListNode import ListNode

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
    print(f"  Output: {output}")
    print(f"Expected: {expected}")
    print(f"  Passed: {output == expected}\n")

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
  
  def _test394():
    Test._print_header("394. Decode String")
    
    s = [
      "3[a]2[bc]",
      "3[a2][c]",
      "2[abc]3[cd]ef"
    ]
    
    expected = [
      "aaabcbc",
      "accaccacc",
      "abcabccdcdcdef"
    ]
    
    for i, _ in enumerate(s):
      Test._print_example_header(i + 1)
      result = Test.solution.decodeString(s[i])
      Test._print_result(result, expected[i])
  
  def _test5():
    Test._print_header("5. Longest Palindromic Substring")
    
    s = [
      "babad",
      "cbbd"
    ]
    
    expected = [
      "bab",
      "bb"
    ]
    
    for i, _ in enumerate(s):
      Test._print_example_header(i + 1)
      result = Test.solution.longestPalindrome(s[i])
      Test._print_result(result, expected[i])

  def _test79():
    Test._print_header("79. Word Search")
    
    board = [
      [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
      ]
    ]
    
    word = [
      "ABCCED"
    ]
    
    expected = [
      True
    ]
    
    for i, _ in enumerate(board):
      Test._print_example_header(i + 1)
      result = Test.solution.exist(board[i], word[i])
      Test._print_result(result, expected[i])

  def _test17():
    Test._print_header("17. Letter Combinations of a Phone Number")
    
    digits = [
      "23", "2"
    ]

    expected = [
      ["ad","ae","af","bd","be","bf","cd","ce","cf"],
      ["a","b","c"]
    ]
    
    for i in range(len(digits)):
      Test._print_example_header(i + 1)
      result = Test.solution.letterCombinations(digits[i])
      Test._print_result(result, expected[i])

  def _test22():
    Test._print_header("22. Generate Parentheses")
    
    n = [3, 1, 2]
    expected = [
      ["((()))","(()())","(())()","()(())","()()()"],
      ["()"],
      [ "(())","()()"]
    ]
    
    for i in range(len(n)):
      Test._print_example_header(i + 1)
      result = Test.solution.generateParenthesis(n[i])
      Test._print_result(result, expected[i])
    
  def _test39():
    Test._print_header("39. Combination Sum")
    
    candidates = [
      [2,3,6,7],
      [2,3,5],
      [2]
    ]
    
    target = [
      7, 8, 1
    ]
    
    expected = [
      [[2,2,3],[7]],
      [[2,2,2,2],[2,3,3],[3,5]],
      []
    ]
    
    for i in range(len(candidates)):
      Test._print_example_header(i + 1)
      result = Test.solution.combinationSum(candidates[i], target[i])
      Test._print_result(result, expected[i])
    
  def _test40():
    Test._print_header("39. Combination Sum")
    
    candidates = [
      [10,1,2,7,6,1,5],
      [2,5,2,1,2],
    ]
    
    target = [
      8, 5
    ]
    
    expected = [
      [[1,1,6],[1,2,5],[1,7],[2,6]],
      [[1,2,2,],[5]]
    ]
    for i in range(len(candidates)):
      Test._print_example_header(i + 1)
      result = Test.solution.combinationSum2(candidates[i], target[i])
      Test._print_result(result, expected[i])
    
  def _test1():
    Test._print_header("1. Two Sum")
    nums = [
      [2,7,11,15],
      [3,2,4],
      [3,3]
    ]
    
    target = [9, 6, 6]
    
    expected = [
      [0, 1],
      [1, 2],
      [0, 1]
    ]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.twoSum(nums[i], target[i])
      Test._print_result(result, expected[i])
    
  def _test88():
    Test._print_header("88. Merge Sorted Array")
    
    nums = [
      [
        [1,2,3,0,0,0],
        [2,5,6],
      ],
      [
        [1],
        []
      ],
      [
        [0],
        [1]
      ]
    ]
    
    mn = [[3, 3],[1, 0],[0,1]]
    
    expected = [[1,2,2,3,5,6], [1], [1]]
  
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      Test.solution.merge(nums[i][0], mn[i][0], nums[i][1], mn[i][1])
      Test._print_result(nums[i][0], expected[i])
  
  def _test46():
    Test._print_header("46. Permutations")
    
    nums = [
      [1,2,3],
      [0,1],
      [1]
    ]
    
    expected = [
      [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
      [[0,1],[1,0]],
      [[1]]
    ]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.permute(nums[i])
      Test._print_result(result, expected[i])
  
  def _test47():
    Test._print_header("47. Permutations II")

    nums = [
      [1,1,2],
      [1,2,3],
      [3,3,0,3]
    ]
    
    expected = [
      [[1,1,2],[1,2,1],[2,1,1]],
      [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
      [[0,3,3,3],[3,0,3,3],[3,3,0,3],[3,3,3,0]]
    ]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.permuteUnique(nums[i])
      Test._print_result(result, expected[i])
  
  def _test494():
    Test._print_header("494. Target Sum")
    
    nums = [
      [1,1,1,1,1],
      [1]
    ]
    
    target = [3, 1]
    expected = [5, 1]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.findTargetSumWays(nums[i], target[i])
      Test._print_result(result, expected[i])
  
  def _test392():
    Test._print_header("392. Is Subsequence")
    
    input = [
      ["abc", "ahbgdc"],
      ["axc", "ahbgdc"]
    ]

    expected = [
      True, False
    ]

    for i in range(len(input)):
      Test._print_example_header(i + 1)
      result = Test.solution.isSubsequence(input[i][0], input[i][1])
      Test._print_result(result, expected[i])

  def _test70():
    Test._print_header("70. Climbing Stairs")
    
    n = [2, 3]
    expected = [2, 3]
    for i in range(len(n)):
      Test._print_example_header(i + 1)
      result = Test.solution.climbStairs(n[i])
      Test._print_result(result, expected[i])
  
  def _test983():
    Test._print_header("983. Minimum Cost For Tickets")
    
    days = [
      [1,4,6,7,8,20],
      [1,2,3,4,5,6,7,8,9,10,30,31],
      [1],
      [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28] # 3x6 + 13*2
    ]
    
    costs = [
      [2,7,15],
      [2,7,15],
      [2,7,15],
      [3,13,45]
    ]
    
    expected = [11, 17, 2, 44]
    
    for i in range(len(days)):
      Test._print_example_header(i + 1)
      result = Test.solution.mincostTickets(days[i], costs[i])
      Test._print_result(result, expected[i])
    
  def _test322():
    Test._print_header("322. Coin Change")
    
    coins = [
      [1,2,5],
      [2],
      [1]
    ]
    
    amount = [11, 3, 0]
    
    expected = [3, -1, 0]
    
    for i in range(len(coins)):
      Test._print_example_header(i + 1)
      result = Test.solution.coinChange(coins[i], amount[i])
      Test._print_result(result, expected[i])
    
  def _test518():
    Test._print_header("518. Coin Change II")
    
    amount = [5, 3, 10]
    coins = [
      [1,2,5],
      [2],
      [10]
    ]
    expected = [4,0,1]
    
    for i in range(len(amount)):
      Test._print_example_header(i + 1)
      result = Test.solution.change(amount[i], coins[i])
      Test._print_result(result, expected[i])
  
  def _test649():
    Test._print_header("649. Dota2 Senate")
    
    senate = ["RD", "RDD", "RRDDD"]
    expected = ["Radiant", "Dire", "Radiant"]
    
    for i in range(len(senate)):
      Test._print_example_header(i + 1)
      result = Test.solution.predictPartyVictory(senate[i])
      Test._print_result(result, expected[i])
      
  def _test2095():
    Test._print_header("2095. Delete the Middle Node of a Linked List")
    
    head = [
      [1,3,4,7,1,2,6],
      [1,2,3,4],
      [2,1],
      [1]
    ]
    
    expected = [
      [1,3,4,1,2,6],
      [1,2,4],
      [2],
      []
    ]
    
    for i in range(len(head)):
      Test._print_example_header(i + 1)
      result = Test.solution.deleteMiddle(ListNode.buildLL(head[i]))
      Test._print_result(ListNode.LLtoArray(result), expected[i])
    
  def _test328():
    Test._print_header("328. Odd Even Linked List")
    head = [
      [1,2,3,4,5],
      [2,1,3,5,6,4,7]
    ]
    
    expected = [
      [1,3,5,2,4],
      [2,3,6,7,1,5,4]
    ]
    
    for i in range(len(head)):
      Test._print_example_header(i + 1)
      result = Test.solution.oddEvenList(ListNode.buildLL(head[i]))
      Test._print_result(ListNode.LLtoArray(result), expected[i])
    
  def _test206():
    Test._print_header("206. Reverse Linked List")
    head = [
      [1,2,3,4,5],
      [5,4,3,2,1],
      []
    ]
    
    expected = [
      [5,4,3,2,1],
      [1,2,3,4,5],
      []
      ]
    
    for i in range(len(head)):
      Test._print_example_header(i + 1)
      result = Test.solution.reverseList(ListNode.buildLL(head[i]))
      Test._print_result(ListNode.LLtoArray(result), expected[i])
    
  def _test7():
    Test._print_header("7. Reverse Integer")
    x = [123,-123, 120, 1020304]
    expected = [321, -321, 21, 4030201]
    
    for i in range(len(x)):
      Test._print_example_header(i + 1)
      result = Test.solution.reverse(x[i])
      Test._print_result(result, expected[i])
  
  def _test27():
    Test._print_header("27. Remove Element")
    
    nums = [
      [3,2,2,3],
      [0,1,2,2,3,0,4,2],
      [],
      [1],
      [2]
    ]
    
    val = [3, 2, 1, 1, 1]
        
    expected = [
      [2,[2,2]],
      [5,[0,1,4,0,3]],
      [0,[]],
      [0,[]],
      [1,[2]]
    ]
        
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.removeElement(nums[i], val[i])
      Test._print_result(f"{result}, {nums[i][0:len(expected[i][1])]}",f"{expected[i][0]}, {expected[i][1]}")
    
  def _test26():
    Test._print_header("26. Remove Duplicates from Sorted Array")
    
    nums = [
      [1,1,2],
      [0,0,1,1,1,2,2,3,3,4],
      [0,0,1,1,1,1,2,3,3]
    ]
    
    expected = [
      [2, [1,2]],
      [5,[0,1,2,3,4]],
      [4, [0,1,2,3]]
    ]
    
    for i in range(len(nums)):
     Test._print_example_header(i + 1)
     result = Test.solution.removeDuplicates(nums[i])
     Test._print_result(f"{result}, {nums[i][0:len(expected[i][1])]}", f"{expected[i][0]}, {expected[i][1]}")
    
  def _test80():
    Test._print_header("80. Remove Duplicates from Sorted Array II")
    
    nums = [
      [1,1,1,2,2,3],
      [0,0,1,1,1,1,2,3,3]
    ]
    
    expected = [
      [5, [1,1,2,2,3]],
      [7,[0,0,1,1,2,3,3]]
    ]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.removeDuplicates2(nums[i])
      Test._print_result(f"{result}, {nums[i][0:len(expected[i][1])]}", f"{expected[i][0]}, {expected[i][1]}")
  
  def _test189():
    Test._print_header("189. Rotate Array")
    
    nums = [
      [1,2,3,4,5,6,7],
      [-1,-100,3,99]
    ]
    
    k = [3, 2]
    
    expected = [
      [5,6,7,1,2,3,4],
      [3,99,-1,-100]
    ]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      Test.solution.rotate(nums[i], k[i])
      Test._print_result(nums[i], expected[i])
    
  def _test121():
    Test._print_header("121. Best Time to Buy and Sell Stock")

    prices = [
      [7,1,5,3,6,4],
      [7,6,5,3,1]
    ]
    
    expected = [5, 0]
    
    for i in range(len(prices)):
      Test._print_example_header(i + 1)
      result = Test.solution.maxProfit(prices[i])
      Test._print_result(result, expected[i])
  
  def _test122():
    Test._print_header("122. Best Time to Buy and Sell Stock II")

    prices = [
      [7,1,5,3,6,4],
      [1,2,3,4,5],
      [7,6,4,3,1]
    ]
    
    expected = [7, 4, 0]
    
    for i in range(len(prices)):
      Test._print_example_header(i + 1)
      result = Test.solution.maxProfit2(prices[i])
      Test._print_result(result, expected[i])
  
  def _test55():
    Test._print_header("55. Jump Game")
    
    nums = [
      [2,3,1,1,4],
      [3,2,1,0,4],
      [0],
      [2,5,0,0]
    ]
    
    expected = [True, False, True, True]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.canJump(nums[i])
      Test._print_result(result, expected[i])
  
  def _test45():
    Test._print_header("45. Jump Game II")
    
    nums = [
      [2,3,1,1,4],
      [2,3,0,1,4]
    ]
    
    expected = [2,2]
    
    for i in range(len(nums)):
      Test._print_example_header(i + 1)
      result = Test.solution.jump(nums[i])
      Test._print_result(result, expected[i])
  
  def _test274():
    Test._print_header("274. H-Index")
    
    citations = [
      [3,0,6,1,5],
      [1,3,1],
      [100],
      [0],
      [0,0]
    ]
    
    expected = [3,1,1,0,0]
    
    for i in range(len(citations)):
      Test._print_example_header(i + 1)
      result = Test.solution.hIndex(citations[i])
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
  problems[394] = _test394
  problems[5] = _test5
  problems[79] = _test79
  problems[17] = _test17
  problems[22] = _test22
  problems[39] = _test39
  problems[40] = _test40
  problems[1] = _test1
  problems[88] = _test88
  problems[46] = _test46
  problems[47] = _test47
  problems[494] = _test494
  problems[392] = _test392
  problems[70] = _test70
  problems[983] = _test983
  problems[322] = _test322
  problems[518] = _test518
  problems[649] = _test649
  problems[2095] = _test2095
  problems[328] = _test328
  problems[206] = _test206
  problems[7] = _test7
  problems[27] = _test27
  problems[26] = _test26
  problems[80] = _test80
  problems[189] = _test189
  problems[121] = _test121
  problems[122] = _test122
  problems[55] = _test55
  problems[45] = _test45
  problems[274] = _test274
  
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
      print(f"{problem} threw an exception:\n")
      traceback.print_exc()  
  