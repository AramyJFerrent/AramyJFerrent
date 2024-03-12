```java
/**
 * Represents a book in the library.
 */
class Book {
    private String title; // Title of the book
    private String author; // Author of the book
    private String ISBN; // ISBN of the book
    private boolean available; // Availability status of the book

    /**
     * Constructs a new Book object with the given parameters.
     * @param title The title of the book.
     * @param author The author of the book.
     * @param ISBN The ISBN of the book.
     * @param available The availability status of the book.
     */
    public Book(String title, String author, String ISBN, boolean available) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.available = available;
    }

    /**
     * Returns the title of the book.
     * @return The title of the book.
     */
    public String getTitle() {
        return title;
    }

    /**
     * Returns the author of the book.
     * @return The author of the book.
     */
    public String getAuthor() {
        return author;
    }

    /**
     * Returns the ISBN of the book.
     * @return The ISBN of the book.
     */
    public String getISBN() {
        return ISBN;
    }

    /**
     * Returns the availability status of the book.
     * @return The availability status of the book.
     */
    public boolean isAvailable() {
        return available;
    }

    /**
     * Sets the availability status of the book.
     * @param available The new availability status of the book.
     */
    public void setAvailable(boolean available) {
        this.available = available;
    }

    /**
     * Returns a string representation of the book.
     * @return A string representation of the book.
     */
    @Override
    public String toString() {
        return "Title: " + title + ", Author: " + author + ", ISBN: " + ISBN + ", Available: " + available;
    }
}

/**
 * Represents a library management system.
 * Allows users to manage books in the library.
 * Author: [your name]
 */
public class LibraryManagementSystem {
    private static ArrayList<Book> books = new ArrayList<>();

    /**
     * Main method to run the library management system.
     * @param args The command line arguments.
     */
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

    /**
     * Adds a new book to the library.
     * @param title The title of the book.
     * @param author The author of the book.
     * @param ISBN The ISBN of the book.
     */
    private static void addBook(String title, String author, String ISBN) {
        books.add(new Book(title, author, ISBN, true));
    }

    /**
     * Displays all books in the library.
     */
    private static void displayBooks() {
        System.out.println("\nBooks in the library:");
        for (Book book : books) {
            System.out.println(book);
        }
    }

    /**
     * Adds a new book to the library based on user input.
     * @param scanner The scanner object to read user input.
     */
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

    /**
     * Removes a book from the library based on ISBN.
     * @param scanner The scanner object to read user input.
     */
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

    /**
     * Checks out a book from the library based on ISBN.
     * @param scanner The scanner object to read user input.
     */
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

    /**
     * Returns a book to the library based on ISBN.
     * @param scanner The scanner object to read user input.
     */
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
```
