import java.util.Scanner;

public class Leetcode {


  public static boolean runProblem(int problem_number){
    switch (problem_number) {
      case 1456:
        Test.test1456();
        break;

      default:
        return false;
    }
    return true;
  }



  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Leetcode Solutions (Java)");

    while(true){
      System.out.print("Type a problem number to run or q to quit: ");
      String input = scanner.nextLine();

      if(input.toLowerCase().equals("q")){
        scanner.close();
        return;
      }

      try {
        int problem = Integer.parseInt(input);
        runProblem(problem);
        continue;
      } catch(NumberFormatException e){
        System.err.print("Invalid input => ");
      }
    }
  }


}