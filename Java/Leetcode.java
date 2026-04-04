import java.util.Scanner;

public class Leetcode {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Leetcode Solutions (Java)");
    Test.showProblems();

    while(true){
      System.out.print("Type a problem number to run or q to quit: ");
      String input = scanner.nextLine();

      if(input.toLowerCase().equals("q")){
        scanner.close();
        return;
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