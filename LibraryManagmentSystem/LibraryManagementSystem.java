import java.util.ArrayList;
import java.util.Scanner;

class Book {
    private String title;
    private String author;
    private String ISBN;
    private boolean available;

    public Book(String title, String author, String ISBN, boolean available) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.available = available;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getISBN() {
        return ISBN;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }

    @Override
    public String toString() {
        return "Title: " + title + ", Author: " + author + ", ISBN: " + ISBN + ", Available: " + available;
    }
}

public class LibraryManagementSystem {
    private static ArrayList<Book> books = new ArrayList<>();

    public static void main(String[] args) {
        addBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565");
        addBook("To Kill a Mockingbird", "Harper Lee", "9780061120084");

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nLibrary Management System");
            System.out.println("1. Display all books");
            System.out.println("2. Add a book");
            System.out.println("3. Remove a book");
            System.out.println("4. Check out a book");
            System.out.println("5. Return a book");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
	    scanner.nextLine();

            switch (choice) {
                case 1:
                    displayBooks();
                    break;
                case 2:
                    addNewBook(scanner);
                    break;
                case 3:
                    removeBook(scanner);
                    break;
                case 4:
                    checkOutBook(scanner);
                    break;
                case 5:
                    returnBook(scanner);
                    break;
                case 6:
                    System.out.println("Exiting program...");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addBook(String title, String author, String ISBN) {
        books.add(new Book(title, author, ISBN, true));
    }

    private static void displayBooks() {
        System.out.println("\nBooks in the library:");
        for (Book book : books) {
            System.out.println(book);
        }
    }

    private static void addNewBook(Scanner scanner) {
        System.out.print("Enter title: ");
        String title = scanner.nextLine();
        System.out.print("Enter author: ");
        String author = scanner.nextLine();
        System.out.print("Enter ISBN: ");
        String ISBN = scanner.nextLine();
        books.add(new Book(title, author, ISBN, true));
        System.out.println("Book added successfully.");
    }

    private static void removeBook(Scanner scanner) {
        System.out.print("Enter ISBN of the book to remove: ");
        String ISBN = scanner.next();
        for (Book book : books) {
            if (book.getISBN().equals(ISBN)) {
                books.remove(book);
                System.out.println("Book removed successfully.");
                return;
            }
        }
        System.out.println("Book not found.");
    }

    private static void checkOutBook(Scanner scanner) {
        System.out.print("Enter ISBN of the book to check out: ");
        String ISBN = scanner.next();
        for (Book book : books) {
            if (book.getISBN().equals(ISBN)) {
                if (book.isAvailable()) {
                    book.setAvailable(false);
                    System.out.println("Book checked out successfully.");
                } else {
                    System.out.println("Book is already checked out.");
                }
                return;
            }
        }
        System.out.println("Book not found.");
    }

    private static void returnBook(Scanner scanner) {
        System.out.print("Enter ISBN of the book to return: ");
        String ISBN = scanner.next();
        for (Book book : books) {
            if (book.getISBN().equals(ISBN)) {
                if (!book.isAvailable()) {
                    book.setAvailable(true);
                    System.out.println("Book returned successfully.");
                } else {
                    System.out.println("Book is already available.");
                }
                return;
            }
        }
        System.out.println("Book not found.");
    }
}
