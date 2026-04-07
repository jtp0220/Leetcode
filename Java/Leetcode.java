import java.util.Scanner;

public class Leetcode {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Leetcode Solutions (Java)");
    Test.showProblems();

    while(true){
      System.out.println("=".repeat(50));
      System.out.println("Menu:\n - [number] to run a problem\n - q to quit\n - p to show problems:");
      System.out.print("\nInput: ");
      String input = scanner.nextLine();

      if(input.toLowerCase().equals("q")){
        scanner.close();
        return;
      }

      if(input.toLowerCase().equals("p")){
        Test.showProblems();
        continue;
      }

      try {
        int problem = Integer.parseInt(input);
        Test.run(problem);
        continue;
      } catch(NumberFormatException e){
        System.err.print("Invalid input => ");
      }
    }
  }
}