from typing import List

class Solutions:
    # --- 3. Longest Substring Without Repeating Characters ---
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
    
    # --- 4. Median of Two Sorted Arrays ---
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
    
    # --- 1679. Max Number of K-Sum Pairs ---
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

    # --- 238. Product of Array Except Self ---
    def productExceptSelfOld(self, nums: List[int]) -> List[int]:
        answer = []
        productNoZeros = 1
        productZeros = 1
        zeros = 0
        
        # Get total product
        for n in nums:
            if not n is 0:
                productNoZeros *= n
                productZeros *= n
            else:
                productZeros *= n
                zeros += 1
        
        # Divide product by each i-th element
        for n in nums:
            if not n is 0:
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
    
    def test238(self):
        nums1 = [1,2,3,4]
        nums2 = [-1, 1, 0, -3, 3]
        nums3 = [0,0]
    
        print("--- 238. Product of Array Except Self ---")
        print(f"Result 1: {self.productExceptSelf(nums1)} (Expected: [24,12,8,6])")
        print(f"Result 2: {self.productExceptSelf(nums2)} (Expected: [0,0,9,0,0])")
        print(f"Result 3: {self.productExceptSelf(nums3)} (Expected: [0,0])") 

    # --- 643. Maximum Average Subarray I ---
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
                

    def test643(self):
        nums1 = [1,12,-5,-6,50,3]
        k1 = 4
        nums2 = [5]
        k2 = 1
        
        print("--- 643. Maximum Average Subarray I ---")
        print(f"Result 1: {self.findMaxAverage(nums1, k1)} (Expected: 12.75000)")
        print(f"Result 2: {self.findMaxAverage(nums2, k2)} (Expected: 5.00000)")

def main():
    S = Solutions()
    
    print("Enter a problem number: ", end="")
    str = input()
    
    match str:
        case "1679": S.test1679()
        case "238": S.test238()
        case "643": S.test643()
        case _:
            exit()
    
if __name__ == "__main__":
    main()