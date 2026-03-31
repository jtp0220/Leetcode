public class Test {
  private static final Solution solution = new Solution();

  private static final void printHeader(String problem_name){
    int maxLength = 100;
    int headerLength = maxLength - problem_name.length();
    String headerPiece = (headerLength > 0) ? "=".repeat(headerLength / 2) : "=====";


    System.out.println(String.format("%s [%s] %s\n", headerPiece, problem_name, headerPiece));
  }

  private static final void printExampleHeader(int number){
    System.out.println(String.format("%s Example %d %s", "-".repeat(20), number, "-".repeat(20)));
  }

  private static final void printResults(String string){
    System.out.println(String.format("results: %s\n", string));
  }

  public static final void test1456(){
    printHeader("1456. Maximum Number of Vowels in a Substring of Given Length");

    String s[] = {"abciiidef", "aeiou", "leetcode", "tryhard", "pdzndkhhoujpqyex", "tnfazcwrryitgacaabwm", "aababaa", "weallloveyou"};
    int k[] = {3, 2, 3, 4, 5, 4, 3, 7};

    for(int i = 0; i < s.length; i++){
      printExampleHeader(i + 1);
      int result = solution.maxVowels(s[i], k[i]);
      printResults(String.format("%d", result));
    }

  }
}
