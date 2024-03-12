package mortgageestimator;

import java.util.Scanner;

/**
 * A program to estimate mortgage payments based on user input.
 * Author: aramy
 */
public class MortgageEstimator {

    /**
     * Main method to run the mortgage estimator program.
     * @param args The command line arguments.
     */
    public static void main(String[] args) {

        // Initialize scanner and variables
        Scanner in = new Scanner(System.in);
        double principal = 0; // Principal amount of the loan
        double interestRate = 0; // Annual interest rate
        int years = 0; // Number of years for the loan

        // Checks if double or integer was entered for necessary values
        System.out.print("Enter principal: ");
        if (in.hasNextDouble()) {
            principal = in.nextDouble();
        } else {
            System.out.println("Error, Double was not entered");
            System.exit(0);
        }

        System.out.print("Enter interest rate: ");
        if (in.hasNextDouble()) {
            interestRate = in.nextDouble();
        } else {
            System.out.println("Error, Double was not entered");
            System.exit(0);
        }

        System.out.print("Enter years for loan: ");
        if (in.hasNextInt()) {
            years = in.nextInt();
        } else {
            System.out.println("Error, Integer was not entered");
            System.exit(0);
        }

        // Initialize and set variable with formulas
        int n = years * 12; // Number of monthly payments
        double r = interestRate / (12 * 100); // Monthly interest rate

        // Find and print single payment and total paid values
        double singlePayment = principal * (r / (1 - (Math.pow(r + 1, -n))));
        double totalPaid = singlePayment * n;
        System.out.printf("Single Payment: %.2f\n", singlePayment);
        System.out.printf("Total Amount Paid: %.2f\n", totalPaid);
    }
}

