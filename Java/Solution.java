import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {
  public int maxVowels(String s, int k){
    int max = 0;
    String vowels = "aeiou";
    ArrayDeque<Boolean> DQ = new ArrayDeque<>(3);
    int vowelCount = 0;

    for(int i = 0; i < s.length(); i++){
      boolean isVowel = vowels.contains(String.valueOf(s.charAt(i)));

      if(DQ.size() < k){
        if(isVowel){
          DQ.add(true);
          vowelCount++;
        } else {
          DQ.add(false);
        }
      } else {          
        boolean poppedIsVowel = DQ.removeFirst();

        if(isVowel){
          DQ.add(true);
          vowelCount += (poppedIsVowel) ? 0 : 1;
        } else {
          DQ.add(false);
          vowelCount -= (poppedIsVowel) ? 1 : 0;
        }
      }
              
      if(vowelCount >= k) return k;
      max = Math.max(max, vowelCount);

    }
    return max;  
  }

  private boolean isVowel(char c){
    return "aeiou".indexOf(c) != -1;
  }

  public int maxVowelsOptimized(String s, int k){

    int max = 0;
    int count = 0;
    int p = 0;

    for(int i = 0; i < s.length(); i++){
      if(isVowel(s.charAt(i))) count++;

      if(i - p >= k){
        if(isVowel(s.charAt(p))) count--;
        p++;
      }

      max = Math.max(max, count);
      
    }
    
    return max;
  }

  public int longestOnes(int[] nums, int k){
    int max = 0;
    int count = 0;
    int p = 0;

    for(int i = 0; i < nums.length; i++){
      if(nums[i] == 0) count++;

      while(count > k){
        if(nums[p] == 0) count--;
        p++;
      }

      max = Math.max(max, i - p + 1);
    }

    return max;
  }

  public int longestSubarray(int[] nums){
    int max = 0;
    int count = 0;
    int p = 0;

    for(int i = 0; i < nums.length; i++){
      if(nums[i] == 0) count++;

      while(count > 1){
        if(nums[p] == 0) count--;
        p++;
      }

      max = Math.max(max, i - p);
    }

    return max;
  }

  public double findMaxAverage(int[] nums, int k){
    double max = Double.NEGATIVE_INFINITY;
    double sum = 0;
    int p = 0;

    for(int i = 0; i < nums.length; i++){
      sum += nums[i];

      if(i - p + 1 >= k){
        max = Math.max(max, sum / k);
        sum -= nums[p];
        p++;
      }
    }

    return max;
  }

  public void moveZeroes(int[] nums){
    
    int p = 0;
    
    for(int i = 0; i < nums.length; i++){
      if(nums[i] != 0){
        while(nums[p] != 0 && p < i){
          p++;
        }

        nums[p] = nums[i];        
        if(i != p) nums[i] = 0;
      }
    }
  }

  public int largestAltitude(int[] gain){
    int max = 0;
    int point = 0;

    for(int i = 0; i < gain.length; i++){
      point += gain[i];
      max = Math.max(max, point);
    }


    return max;
  }

  public boolean isSubsequence(String s, String t){
    // two pointers
    int i = 0; 
    int j = 0;

    while(i < t.length() && j < s.length()){
      if(t.charAt(i++) == s.charAt(j)) j++;
    }

    if(j == s.length()) return true;
    return false;
  }

  public int maxArea(int[] height){
    int max = 0;

    int l = 0;
    int r = height.length - 1;

    while(l < r){
      max = Math.max(max, (r - l) * Math.min(height[l], height[r]));
     
      if(height[l] < height[r]){
        l++;
      } else {
        r--;
      }
    }
    return max;
  }

  public int maxOperations(int[] nums, int k){
    int count = 0;
    Map<Integer, Integer> M = new HashMap<>();

    for(int i = 0; i < nums.length; i++){
      int x = nums[i];
      int y = k - x;

      if(M.containsKey(y) && M.get(y) > 0){
        M.put(y, M.get(y) - 1);
        count++;
      } else {
        M.put(x, M.getOrDefault(x, 0) + 1);
      }
    }

    return count;
  }

  public int pivotIndex(int[] nums){
    int pivot = -1;
    int rightSum = 0;

    // Get sum of array
    for(int i = 0; i < nums.length; i++) rightSum += nums[i];

    // Find pivot
    int leftSum = 0;

    for(int i = 0; i < nums.length; i++){
      if(leftSum == rightSum - nums[i]) return i;
      leftSum += nums[i];
      rightSum -= nums[i];
    }
    
    return pivot;
  }
}
