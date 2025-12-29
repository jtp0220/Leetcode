from typing import List

class Solutions:
    # --- 3. Longest Substring Without Repeating Characters
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
    
    # --- 4. Median of Two Sorted Arrays
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

    # --- 151. Reverse Words in a String
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        s = ''
        for w in words:
            s += w + ' '

        return s.strip()
    
    # --- 1679. Max Number of K-Sum Pairs
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
        
    def test1679(self):
        nums1 = [1,2,3,4]
        k1 = 5
        nums2 = [3,1,3,4,3]
        k2 = 6
        
        print("--- 1679. Max Number of K-Sum Pairs ---")
        print(f"Result 1: {self.maxOperations(nums1, k1)} (Expected: 2)")
        print(f"Result 2: {self.maxOperations(nums2, k2)} (Expected: 1)")

S = Solutions()
S.test1679()