package mortgageestimator;

import java.util.Scanner;
/**
 *
 * @author aramy
 */
public class MortgageEstimator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        //initialize scanner and variables
        Scanner in = new Scanner(System.in);
        double principal = 0;
        double interestRate = 0;
        int years = 0;
        
        //Checks if double or integer was entered for necessary values
        System.out.print("Enter principal: ");
        if(in.hasNextDouble()) {
            principal = in.nextDouble();
        }
        else {
            System.out.println("Error, Double was not entered");
            System.exit(0);
        }
        
        System.out.print("Enter interest rate: ");
        if(in.hasNextDouble()) {
            interestRate = in.nextDouble();
        }
        else {
            System.out.println("Error, Double was not entered");
            System.exit(0);
        }
        
        System.out.print("Enter years for loan: ");
        if(in.hasNextInt()) {
            years = in.nextInt();
        }
        else {
            System.out.println("Error, Integer was not entered");
            System.exit(0);
        }
        
        //initialize and set variable with formulas
        int n = years * 6;
        double r = interestRate / (6 * 100);
                
        //find and print single payment and total paid values
        double singlePayment = principal *(r /(1 - (Math.pow(r + 1, -n))));
        double totalPaid = singlePayment * n;
        System.out.printf("Single Payment: %.2f\n", singlePayment);
        System.out.printf("Total Amount Paid: %.2f\n", totalPaid);  
    }        
}
  
