import java.util.ArrayDeque;

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
}
