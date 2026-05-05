from typing import List
from collections import deque

class Solution:
    def isUnique(self, c: str, record: List[str]):
        for char in record:
            if(c == char):
                return False
        return True        
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if(len(s) == 0): return 0
        if(len(s) == 1): return 1
        
        n: int = 0

        record: List[str] = []
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if(self.isUnique(s[j], record)):
                    record.append(s[j])
                else:
                    n = max(n, len(record))
                    record.clear()
                    break
                
        return n
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [*nums1, *nums2]
        nums.sort()
        numsLen = len(nums)
        
        if(numsLen % 2 == 0):
            x = numsLen // 2
            y = x - 1
            return (nums[x] + nums[y]) / 2

        else:
            z = (numsLen - 1) // 2
            return nums[z]

    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        s = ''
        for w in words:
            s += w + ' '

        return s.strip()
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        d = dict()
        for n in nums:
            # Check for pair
            pair = k - n
            if pair in d:                
                if d[pair] > 0:
                    count += 1
                d[pair] -= 1
                if d[pair] == 0:
                    d.pop(pair)
            else:   
                # Update dictionary
                if n in d:
                    d[n] += 1
                else:
                    d[n] = 1
                      
        return count
        
    def productExceptSelfOld(self, nums: List[int]) -> List[int]:
        answer = []
        productNoZeros = 1
        productZeros = 1
        zeros = 0
        
        # Get total product
        for n in nums:
            if n != 0:
                productNoZeros *= n
                productZeros *= n
            else:
                productZeros *= n
                zeros += 1
        
        # Divide product by each i-th element
        for n in nums:
            if n != 0:
                answer.append(productZeros // n)
            else:
                if zeros > 1:
                    answer.append(0)
                else:
                    answer.append(productNoZeros)
    
        return answer
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        
        # 1st pass: apply prefixes 
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i] 
    
        # 2nd pass: calculate suffixes and apply
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
    
        return answer
    
    def findMaxAverage(self, nums: List[int], k:int) -> float:
        n = len(nums)
        max: float = 0
        sum: float = 0
        
        # Setup
        for i in range(k):
            sum += nums[i]
        max = sum / k
        
        # Find largest subarray
        for i in range(n - k):
            sum += nums[i + k]
            sum -= nums[i]
            new = sum / k
            if new > max: max = new
      

        return max
                
    def convert(self, s: str, numRows: int) -> str:
        d: dict[int, list[str]] = {}
        
        i = 0
        z = 0
        multiplier = 1    
        
        # We need to find out how big the diagonal on the zig-zag is. HOW?
    
        while i < len(s):
            # Calculate current row
            row = z % numRows
            
            # Store
            d.setdefault(row, []).append(s[i])

            # Set forward / backward
            if(z == 0):
                multiplier = 1
            if(z == numRows - 1):
                multiplier = -1

            # Update 
            z += 1 * multiplier
            i += 1

        # Join
        result = ""
        for key, arr in d.items():
            result += "".join(arr)
        
        return result

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # Index: the number of occurrences, value: the number that has that occurence
        occurrences = [0 for v in range(1001)]
        
        map: dict = {}
        
        # collect occurrences
        for v in arr:
            curr = map.get(v, 0)
            map[v] = curr + 1    
            
        # populate occurrences array
        for k in map:
            if(occurrences[map[k]] == 1):
                return False
            occurrences[map[k]] = 1
                    
        return True
    
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        freq1: dict = {}
        freq2: dict = {}
        
        for c in word1:
            f = freq1.get(c, 0)
            freq1[c] = f + 1
            
        for c in word2:
            f = freq2.get(c, 0)
            freq2[c] = f + 1

        # Words must have the same characters to be convertible
        if freq1.keys() != freq2.keys():
            return False
        
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True

    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows: dict = {}
        
        for row in grid:
            key = tuple(row)
            rows[key] = rows.get(key, 0) + 1
        
        cols: dict = {}
        
        # Find columns
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            key = tuple(col)
            cols[key] = cols.get(key, 0) + 1
    
        pairs = 0
        
        for row in rows:
            if row in cols:
                pairs += rows[row] * cols[row]
        
        return pairs
        
    def removeStars(self, s: str) -> str:
        # process the string backwards
        # build a result string
        # when you see a star, add to count
        # the next character you read, dont include it if count > 0
        # return
    
        # OR the stack way
        # from left to right process the string
        # build a result string
        # when you see a star, pop the last element you added
        # return

        stack = []

        for c in s:
            if c == '*':
                stack.pop(len(stack) - 1)

            if c != '*':
                stack.append(c)
            
        return "".join(stack)
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        result = []
        
        for a in asteroids:
            if(a >= 0):
                result.append(a)
                continue

            while(True):
                n = len(result)
                
                # if no asteroids, a lives
                if(n <= 0):
                    result.append(a)
                    break
                
                b = result[n - 1]
                
                # if b is in the same direction as a, no one dies            
                if(b < 0):
                    result.append(a)
                    break
                
                # if a is the same size as b, destroy both
                if(abs(a) == abs(b)):
                    result.pop()
                    break
                
                # if a is greater than b, destroy b and continue
                if(abs(a) > abs(b)):
                    result.pop()
                    continue
                    
                # if a is smaller than b, destroy a
                if(abs(a) < abs(b)):
                    break
                
        return result
    
    def decodeString(self, s: str) -> str:
        
        stack = []
        substring = ""
        
        for c in (s):
            if(c.isdigit()):
                stack.append(substring)
                stack.append(c)
                substring = ""
            elif(c  == "["):
                continue
            elif(c == "]"):
                n = int(stack.pop())
                print(f"n: {n}")
                prevString = stack.pop()
                substring = prevString + n * substring      
            else:
                substring += c
        return substring

    # TODO
    def longestPalindrome(self, s: str) -> str:
        pass

    # TODO        
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass

    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        
        keypad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
                
        # Example 1: [2, 3]
                
        def dfs(index: int, path: str):
            
            if index == len(digits):
                result.append(path)
                return
            
            letters = keypad[digits[index]]
            
            for letter in letters:
                dfs(index + 1, path + letter)
               
        dfs(0, "")
        
        return result
        
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def dfs(index: int, path: str, l: int, r: int):
            
            if index == n * 2:
                result.append(path)
                return 
        
            if l < n:
                dfs(index + 1, path + "(", l + 1, r + 1)
                
            if r > 0:
                dfs(index + 1, path + ")", l, r - 1)
            
            return
            
        dfs(0, "", 0, 0)
        
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result: List[List[int]] = []
        
        def dfs(index: int, path: List[int]):
            
            if(sum(path) == target):
                result.append(path)
                return
            
            if(sum(path) > target):
                return 
                        
            for i in range(index, len(candidates)):
                dfs(i, path + [candidates[i]])
        
        dfs(0, [])
        
        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        
        candidates.sort()
        
        def dfs(index: int, path: List[int], total: int):
            
            if(total == target):
                if path not in result:
                    result.append(path)
                return
            
            if(total > target):
                return 


            # Since candidates are sorted, we have ex. [1, 1, 1, 2, 2, 2, 3, 3, 3, ...]
            # At the current dfs level, we don't want to use the same number more than once since its inefficient
            # prev allows us to use a number once, and skip all other instances
            # this avoids creating any duplicates from the beginning
            prev = -1
            
            for i in range(index, len(candidates)):

                    if prev == candidates[i]:
                        continue
                    prev = candidates[i]
                    
                    # If total + ith element exceeds the target, then surely any (i + 1)th element will too since candidates are sorted
                    if total + candidates[i] > target:
                        break
                    
                    dfs(i + 1, path + [candidates[i]], total + candidates[i])
        
        dfs(0, [], 0)            
        
        return result
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []        
        d = {}

        for i in range(len(nums)):
            x = nums[i]

            if(x in d):
                return [d[x], i]
            y = target - x
            d[y] = i
            
        return result
        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #key: iterate backwards
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while(k > -1):
            x = nums1[i] if i > -1 else None
            y = nums2[j] if j > -1 else None
            
            if(x == None):
                nums1[k] = y
                j -= 1
            elif(y == None):
                nums1[k] = x
                i -= 1
            elif(x > y):
                nums1[k] = x
                i -= 1
            else:
                nums1[k] = y
                j -= 1
            k -= 1
            
# 933. Number of Recent Calls
class RecentCounter:
    def __init__(self):
        self.log: deque = deque()
    
    def ping(self, t: int) -> int:
        self.log.append(t)
        while(self.log[0] < t - 3000):
            self.log.popleft()
        return len(self.log)
