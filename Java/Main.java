import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("\nLeetcode Solutions (Java)\n");
    Test.showProblems();

    while(true){
      System.out.println("=".repeat(55));
      System.out.println("\nMenu:\n - [number] to run a problem\n - q to quit\n - p to show problems");
      System.out.print("\nInput: ");
      String input = scanner.nextLine();

      if(input.toLowerCase().equals("q")){
        scanner.close();
        return;
      }

      if(input.toLowerCase().equals("p")){
        System.out.println();
        Test.showProblems();
        continue;
      }

      try {
        int problem = Integer.parseInt(input);
        System.out.println();
        Test.run(problem);
        continue;
      } catch(NumberFormatException e){
        System.err.println("\nPlease enter a valid menu option.\n");
      }
    }
  }
}