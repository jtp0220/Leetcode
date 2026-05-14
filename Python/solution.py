from typing import List
from typing import Optional
from collections import deque
from ListNode import ListNode
import math

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

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(indices: set, path: List[int]):
            
            if(len(path) == len(nums)):
                result.append(path)
                return
            
            for i in range(len(nums)):
                if i in indices:
                    continue
                dfs(indices + (i,), path + [nums[i]])
        
        dfs((), [])
        return result
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        def dfs(indices: set, path: List[int]):
            if(len(path) == len(nums)):
                result.append(path)
                return
            
            prev = -11
            for i in range(len(nums)):
                if nums[i] == prev:
                    continue

                if i in indices:
                    continue
            
                prev = nums[i]
                
                dfs(indices + (i,), path + [nums[i]])
            
    
        dfs((), [])
        return result
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def dfs(index: int, total: int):
            if index == len(nums): 
                if total == target:
                    return 1
                return 0
            
            if (index, total) in dp:
                return dp[(index, total)]
         
            dp[index, total] = dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
            return dp[index, total]
        
        return dfs(0, 0)    
    
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        while (i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)
        
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        
        def dfs(steps: int) -> int:
            if steps in dp:
                return dp[steps]
            
            if(steps == n):
                return 1
            
            if(steps > n):
                return 0
        
            dp[steps] = dfs(steps + 1) + dfs(steps + 2)
            return dp[steps]
        
        return dfs(0)
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        dp = {}
        
        # Sub problem: From day 0, what is the minium cost
        def dfs(i: int):
            # From day n minimum cost is 0 since index range is [0, n - 1]
            if i == n:
                return 0
            
            # Check if we've computed already
            if i in dp:
                return dp[i]
        
            dp[i] = float("inf") # We need this for our loop since we are chaining min(curr, k) instead of min(x, y, z)
            
            # purpose of this loop is to update i up to a day we can't cover yet
            for d, c in zip([1,7, 30], costs):
                j = i
                
                # with d, we can cover up to days[i] + d days which costs c, so we want to find c + dfs(days[i] + d + 1)
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
                
            return dp[i]
            
        return dfs(0)
        
    def mincostTickets_attempt1(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = {}
        
        # The sub problem is "from day 0, the cheapest cost is x"
        def dfs(day: int, totalCost: int, i: int):
            # New path found
            if i == n:
                return totalCost
            
            # Check memo
            if i in dp:
                return dp[i]
            
            # how much coverage did our choice give us? (1,7, 30)
            while i < n:                
                # day i is not covered
                if(days[i] > day):
                    i += 1
                    break
                i += 1
            
            # Get min of all possible paths
            dp[i] = min(
                dfs(day + 1, totalCost + costs[0], i),
                dfs(day + 7, totalCost + costs[1], i),
                dfs(day + 30, totalCost + costs[2], i)
            )
                        
            return dp[i]
        
        return dfs(0, 0, 0)
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        
        def dfs(a: int):

            # base case
            if a == amount:
                return 0
            
            if a > amount:
                return float("inf")

            # check memo
            if a in dp:
                return dp[a]    
        
            dp[a] = float("inf")
            
            for c in coins:
                dp[a] = min(dp[a], 1 + dfs(a + c))

            return dp[a]
        
        result = dfs(0)
        
        return result if result != float("inf") else -1
   
    def change(self, amount: int, coins: List[int]):

        dp = {}

        # Subproblem: If I have an amount a, how many ways from here can I reach the total amount using coins from [0, i]
        def dfs(i: int, a: int):
            
            if a == amount:
                return 1
        
            if a > amount:
                return 0
    
            if i == len(coins):
                return 0
            
            if (i, a) in dp:
                return dp[(i, a)]
        
            dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return dp[(i, a)]
        
        return dfs(0,0)   
  
    def predictPartyVictory(self, senate: str) -> str:
        queue: deque = deque()
        
        parties = {"R" : 0, "D": 0}
        banned = {"R" : 0, "D": 0}
        
        # load queue
        for s in senate:
            parties[s] += 1
            queue.append(s)
        
        winner = ""
        
        # Run rounds
        while(winner == ""):    
            m = sum(parties.values())
            
            # Play round
            for _ in range(m):
                s = queue.popleft()
                            
                # Check banned
                if banned[s] > 0:
                    parties[s] -= 1
                    banned[s] -= 1
                    continue

                if s == "R":
                    if parties["D"] == 0:
                        winner = "Radiant"
                    else:
                        banned["D"] += 1

                if s == "D":
                    if parties["R"] == 0:
                        winner = "Dire"
                    else:
                        banned["R"] += 1

                queue.append(s)

                            

        return winner
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        
        # Get length of list
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        # base case
        if n == 1:
            return None
        
        # Calculate i
        i = (n // 2) - 1
        
        # Go up to i
        cur = head
        j = 0
        
        while j < i:
            j += 1
            cur = cur.next
                
        # Transfer
        prev = cur
        cur = cur.next
        prev.next = cur.next
        
        return head
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base cases
        if not head:
            return None
        
        if not head.next:
            return head
        
        odd = head
        even = head.next

        evenHead = even

        # while (odd.next and odd.next.next) or (even.next and even.next.next):
        #     if(odd.next and odd.next.next):
        #         odd.next = odd.next.next
        #         odd = odd.next

        #     if(even.next):
        #         if(even.next.next):           
        #             even.next = even.next.next
        #             even = even.next
        #         else:
        #             even.next = None

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode):
            if not node:
                return None
            
            if not node.next:
                return node
            
            newHead: ListNode = reverse(node.next)
            curr = newHead  
            while curr.next:
                curr = curr.next
            curr.next = node
            node.next = None
            return newHead
        return reverse(head)
        
    def reverse(self, x: int) -> int:
        digits = []
        sign = -1 if x < 0 else 1
        x = abs(x)
                
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        for i, d in enumerate(digits):
            x += d * pow(10, len(digits) - i - 1)
            if x > 2**31 - 1:
                return 0
                            
        return x * sign
        
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
    
        count = 0
        
        for i in range(n - 1, -1, -1):
            # check if cur element == val
            if(nums[i] != val):
                continue
            
            # if element == val then swap until its at the end of the list
            j = i
            while(j < n - 1 - count):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1
                
            # increment count
            count += 1
                        
        return n - count

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        dup = {}
        
        # First pass: count the number of occurences for each unique element
        for num in nums:
            dup[num] = dup.get(num, 0) + 1
                    
        # Second pass: Iterate in reverse, bubble duplicates to back of array with swapping
        count = 0
        for i in range(n - 1, -1, -1):
            val = nums[i]
            
            if dup[val] == 1:
                continue
            dup[val] -= 1
            j = i
            while j < n - 1 - count:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1
            count += 1         

        return n - count

    def removeDuplicates2(self, nums: List[int]) -> int:
        n = len(nums)
        
        dup = {}
        
        # First pass: count the number of occurences for each unique element
        for num in nums:
            dup[num] = dup.get(num, 0) + 1
                    
        # Second pass: Iterate in reverse, bubble duplicates to back of array with swapping
        count = 0
        for i in range(n - 1, -1, -1):
            val = nums[i]
            
            if dup[val] < 3:
                continue
            dup[val] -= 1
            j = i
            while j < n - 1 - count:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1
            count += 1         

        return n - count
    
    def rotate(self, nums: List[int], k: int) -> None:

        d = {}
        
        for i in range(len(nums)):
            
            # get k-step index
            j = (i + k) % len(nums)

            # store nums[j] in d
            d[j] = nums[j]
            
            # if i in d then pop or get nums[i] and set nums[j]
            nums[j] = d.pop(i) if i in d else nums[i]

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = r = 0
        
        while r < len(prices):
            if(prices[l] < prices[r]):
                profit = max(profit, prices[r] - prices[l])
            
            if(prices[r] < prices[l]):
                l = r
            r += 1
            
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if(prices[i] > prices[i - 1]):
                profit += prices[i] - prices[i - 1]
                
        return profit

    def canJump(self, nums: List[int]) -> bool:

        dp = {}

        # Sub problem: Can I reach the end from index i?  
        def dfs(i: int):
            if i >= len(nums) - 1:
                return True
                    
            if i in dp:
                return dp[i]

            dp[i] = False
            
            # Try every step from index i
            for j in range(nums[i], 0, -1):
                dp[i] = dfs(i + j)
                if dp[i]:
                    return True
            return dp[i]
    
        return dfs(0)

    def jump(self, nums: List[int]) -> int:

        dp = {}

        # Sub problem: From i, what is the minimum number of jumps it takes to reach the end
        def dfs(i: int):
            if i >= len(nums) - 1:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = float("inf")

            j = 1
            while j <= nums[i]:                    
                dp[i] = min(dp[i], 1 + dfs(i + j))
                j += 1
            return dp[i]
                    
        return dfs(0)

    def hIndex(self, citations: List[int]) -> int:
        # Genius idea: 2 pointer solution
        # Use sorted array
        # Start with l at i=0 and r at i=n-1
        # Compare citations[l] with the number of elements between l and r inclusive
        # if citations[l] < (r - l + 1) then l++
        # loop until l == r
        # But actually if we simplify, we dont even need 2 pointers we can just use current index and iterate one loop
        
        # O(n log n)
        citations.sort()
        
        h = 0
        
        # O(n)
        for i in range(len(citations)):
            h = min(citations[i], len(citations) - i)
            if citations[i] >= len(citations) - i:
                break        
        return h
    
    
# 933. Number of Recent Calls
class RecentCounter:
    def __init__(self):
        self.log: deque = deque()
    
    def ping(self, t: int) -> int:
        self.log.append(t)
        while(self.log[0] < t - 3000):
            self.log.popleft()
        return len(self.log)
