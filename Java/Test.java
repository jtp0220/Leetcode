import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Test {
  private static final Map<Integer, Runnable> problems = new LinkedHashMap<>();
  private static final Solution solution = new Solution();

  static {
    problems.put(1456, Test::test1456);
    problems.put(1004, Test::test1004);
    problems.put(1493, Test::test1493);
    problems.put(643, Test::test643);
    problems.put(283, Test::test283);
    problems.put(1732, Test::test1732);
    problems.put(392, Test::test392);
    problems.put(11, Test::test11);
    problems.put(1679, Test::test1679);
    problems.put(724, Test::test724);
    problems.put(2215, Test::test2215);
    problems.put(1207, Test::test1207);
  }

  // ============================ PRINT METHODS ============================
  private static final void printHeader(String problem_name){
    int maxLength = 100;
    int headerLength = maxLength - problem_name.length();
    String headerPiece = (headerLength > 0) ? "=".repeat(headerLength / 2) : "=====";


    System.out.println(String.format("%s [%s] %s\n", headerPiece, problem_name, headerPiece));
  }

  private static final void printExampleHeader(int number){
    System.out.println(String.format("%s Example %d %s", "-".repeat(20), number, "-".repeat(20)));
  }

  private static final void printResult(String output, String expected){
    System.out.println(String.format("Output: %s\n" + (expected.isEmpty() ? "" : "Expected: %s\n"), output, expected));
  }

  public static final void showProblems(){
    System.out.println("=".repeat(55));
    System.out.println("Problems:");
    int i = 0;
    int rowSize = 10;
    for(int key : problems.keySet()){
      System.out.print(key + ((i++ == problems.size() - 1) ? "\n" : (i % rowSize == 0) ? " " : ", "));
      if(i % rowSize == 0 && i < problems.size()) System.out.println();
    }
  }

  public static boolean run(int problem_number){
    Runnable problem = problems.get(problem_number);
    if(problem == null) return false;
    problem.run();
    return true;
  }

  // ============================ TEST METHODS ============================
  private static final void test1456(){
    printHeader("1456. Maximum Number of Vowels in a Substring of Given Length");

    String s[] = {"abciiidef", "aeiou", "leetcode", "tryhard", "pdzndkhhoujpqyex", "tnfazcwrryitgacaabwm", "aababaa", "weallloveyou"};
    int k[] = {3, 2, 3, 4, 5, 4, 3, 7};
    int expected[] = {3, 2, 2, 1, 2, 3, 2, 4};
    for(int i = 0; i < s.length; i++){
      printExampleHeader(i + 1);
      int result = solution.maxVowelsOptimized(s[i], k[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }

  }

  private static final void test1004(){
    printHeader("1004. Max Consecutive Ones III");

    int nums[][] = {
      {1,1,1,0,0,0,1,1,1,1,0},
      {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1},
      {1,1,1,1,0,0,0,1,1,1,1,1,1,1,1},
      {0,0,0,1}
    };

    int k[] = {2, 3, 2, 4};

    int expected[] = {6,10, 10, 4};

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      int result = solution.longestOnes(nums[i], k[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }
  }

  private static final void test1493(){
    printHeader("1493. Longest Subarray of 1's After Deleting One Element");

    int nums[][] = {
      {1,1,0,1},
      {0,1,1,1,0,1,1,0,1},
      {1,1,1}
    };

    int expected[] = {3, 5, 2};

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      int result = solution.longestSubarray(nums[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }
  }

  private static final void test643(){
    printHeader("643. Maximum Average Subarray I");

    int nums[][] = {
      {1,12,-5,-6,50,3},
      {5},
      {-1}
    };

    int k[] = {4, 1, 1};
    double expected[] = { 12.75, 5.0, -1.0};

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      double result = solution.findMaxAverage(nums[i], k[i]);
      printResult(String.format("%.5f", result), String.format("%.5f", expected[i]));
    }


  }

  private static final void test283(){
    printHeader("283. Move Zeroes");

    int nums[][] = {
      {0,1,0,3,12},
      {0},
      {1, 0}
    };

    int expected[][] = {
      {1,3,12,0,0},
      {0},
      {1, 0}
    };

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      solution.moveZeroes(nums[i]);
      printResult(Arrays.toString(nums[i]), Arrays.toString(expected[i]));
    }
  }

  private static final void test1732(){
    printHeader("1732. Find the Highest Altitude");

    int gain[][] = {
      {-5,1,5,0,-7},
      {-4,-3,-2,-1,4,3,2}
    };

    int expected[] = {1, 0};

    for(int i = 0; i < gain.length; i++){
      printExampleHeader(i + 1);
      int result = solution.largestAltitude(gain[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }

  }

  private static final void test392(){
    printHeader("392. Is Subsequence");

    String s[] = {"abc", "axc"};
    String t[] = {"ahbgdc", "ahbgdc"};
    boolean expected[] = {true, false};

    for(int i = 0; i < s.length; i++){
      printExampleHeader(i + 1);
      boolean result = solution.isSubsequence(s[i], t[i]);
      printResult(Boolean.toString(result), Boolean.toString(expected[i]));
    }
  }

  private static final void test11(){
    printHeader("11. Container With Most Water");

    int height[][] = {
      {1,8,6,2,5,4,8,3,7},
      {1,1}
    };

    int expected[] = {49, 1};

    for(int i = 0; i < height.length; i++){
      printExampleHeader(i + 1);
      int result = solution.maxArea(height[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }

  }

  private static final void test1679(){
    printHeader("1679. Max Number of K-Sum Pairs");

    int nums[][] = {
      {1,2,3,4},
      {3,1,3,4,3}
    };

    int k[] = {5, 6};

    int expected[] = {2, 1};

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      int result = solution.maxOperations(nums[i], k[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }
  }

  private static final void test724(){
    printHeader("724. Find Pivot Index");

    int nums[][] = {
      {1,7,3,6,5,6},
      {1,2,3},
      {2,1,-1}
    };

    int expected[] = {3, -1, 0};

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      int result = solution.pivotIndex(nums[i]);
      printResult(Integer.toString(result), Integer.toString(expected[i]));
    }
  }

  private static final void test2215(){
    printHeader("2215. Find the Difference of Two Arrays");

    int nums[][][] = {
      {
        {1,2,3},
        {2,4,6},
      },
      {
        {1,2,3,3},
        {1,1,2,2},
      }
    };

    List<List<List<Integer>>> expected = new ArrayList<>();
    expected.add(Arrays.asList(
      Arrays.asList(1, 3), Arrays.asList(4, 6)
    ));
    expected.add(Arrays.asList(
      Arrays.asList(3), new ArrayList<>()
    ));

    for(int i = 0; i < nums.length; i++){
      printExampleHeader(i + 1);
      List<List<Integer>> result = solution.findDifference(nums[i][0], nums[i][1]);
      printResult(result.toString(), expected.get(i).toString());
    }


  }

  private static final void test1207(){
    printHeader("1207. Unique Number of Occurences");

    int arr[][] = {
      {1,2,2,1,1,3},
      {1,2},
      {-3,0,1,-3,1,1,1,-3,10,0}
    };

    boolean expected[] = {true, false, true};

    for(int i = 0; i < arr.length; i++){
      printExampleHeader(i + 1);
      boolean result = solution.uniqueOccurences(arr[i]);
      printResult(Boolean.toString(result), Boolean.toString(expected[i]));
    }
  }

}