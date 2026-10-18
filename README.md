
## Hi there 👋, My name is Aramy Ferrent
![](https://miro.medium.com/v2/resize:fit:3200/0*MPoz9YzJq7jMdbfh)

I am a Computer Science student at The Pennsylvania State University pursuing a Bachelor's degree. I am skilled in C++, Java, and MySQL, with a strong foundation in programming principles. Currently I am a sophomore, eager to apply and expand my knowledge in a professional environment. This repository includes programs and projects I have completed so far in my career.



Skills: C++, Java, MySQL



[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/aramyf)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40'>](https://www.linkedin.com/in/aramy-ferrent-aa1953272?/)  


## CaesarCipher
#### This C++ program implements a Caesar cipher encryption and decryption system. It defines functions for encrypting and decrypting a user-provided string using a specified offset key. The `encrypt` function shifts alphabetic characters in the input string by the offset amount, maintaining the case and wrapping around the alphabet. Non-alphabetic characters are left unchanged. The `decrypt` function reverses the encryption by shifting the characters in the opposite direction. The program also reverses the original input string and prints the reversed version. Overall, the code showcases string manipulation and pointer arithmetic in C++ to perform encryption, decryption, and string reversal operations.

## CollegeFootballScorePredictor
#### This Python project predicts the final score of every FBS college football game during the season, along with each team's win probability and an 80% range for its points. It starts each team from a preseason prior fitted on past seasons (last year's rating, program history and returning production that counts transfer-portal arrivals), rates every offense, defense and special-teams unit from opponent-adjusted play-by-play efficiency (EPA) with garbage time removed, gives FCS opponents ratings of their own, blends the result with the betting line, and simulates each game 10,000 times drive by drive, overtime included, to get realistic scores. A scheduled GitHub Action refreshes the data, refits the model, re-predicts upcoming games and grades finished ones every day and several times on Saturdays, so it keeps itself current through the season. A walk-forward backtest over 2016 to 2025 scores it against the closing betting line, overall and by kind of game. See [CollegeFootballScorePredictor](CollegeFootballScorePredictor) and the [latest predictions](CollegeFootballScorePredictor/predictions/README.md).

## DoubleLinkedList
#### This C++ program defines a `DoubleLinkedList` class for a doubly linked list. It manages the list with `head` and `tail` pointers and a `count` of nodes. Nodes store an integer `data` value and pointers to the `next` and `prev` nodes. The class provides methods to insert, merge, and remove nodes, access elements by index, and display the list in forward or reverse order.

## Gradebook
#### This C++ program reads student grade information from a file ("input.txt") where each line contains a student's name, an assessment type ("e" for Essay or "tp" for Team Project), and corresponding grades. It utilizes the `GradeBook`, `Essay`, and `TeamProject` classes to manage and store the grades. For each line in the input file, the program extracts the student's name, assessment type, and grade(s), then creates either an `Essay` or `TeamProject` object based on the assessment type, sets the grade(s), and adds the assessment to the `GradeBook` object. Finally, it prints out the grades for each student using the `printGrades` method of the `GradeBook` class.

## LibraryManagementSystem
#### This Java program implements a basic library management system using a menu-driven interface. It defines a `Book` class with attributes for title, author, ISBN, and availability, and a `LibraryManagementSystem` class that manages a list of books. Users can add new books, remove existing ones, check out books (marking them as unavailable), return books (marking them as available), and display all books in the library. The program uses a Scanner object to handle user input and provides a simple yet functional system for managing a library's collection of books.

## MortgageEstimator
#### This Java program, `MortgageEstimator`, allows users to estimate their monthly mortgage payments based on the principal amount, interest rate, and the number of years for the loan. It first prompts the user to enter these values, ensuring that the principal and interest rate are valid doubles and the number of years is a valid integer. It then calculates the monthly payment using the formula for a fixed-term mortgage and computes the total amount paid over the loan term. Finally, it displays the calculated monthly payment and total amount paid, providing users with a rough estimate of their mortgage expenses.

## NFLScorePredictor
#### This Python project predicts the final score of every NFL game during the season, along with each team's win probability and an 80% range for its points. It rates every offense, defense and special-teams unit from opponent-adjusted play-by-play efficiency (EPA) using ridge regression toward a preseason prior, adjusts for the projected starting quarterback, home field, rest and forecast wind, blends the result with the betting line, and simulates each game 10,000 times drive by drive to get realistic scores. A scheduled GitHub Action refreshes the data, refits the model, re-predicts upcoming games and grades finished ones every day, so it keeps itself current through the season. A walk-forward backtest over 2015 to 2025 scores it against the closing betting line. See [NFLScorePredictor](NFLScorePredictor) and the [latest predictions](NFLScorePredictor/predictions/README.md).

## NHLScorePredictor
#### This Python project predicts the final score of every NHL game during the season, along with each team's win probability, the chance of overtime and an 80% range for its goals. It rates every team from score-and-venue-adjusted expected goals (from its own frozen shot model) and actual goals using ridge regression toward a preseason prior, values each starting goalie by goals saved above expected (projecting the starter from recent usage and back-to-backs when he is not yet named), adds home ice, rest and an Elo edge in a Poisson goal-rate model, blends the result with goal rates backed out of the betting line, and simulates each game 10,000 times minute by minute, with pulled goalies, empty-net goals, three-on-three overtime and shootouts. A scheduled GitHub Action refreshes the data, refits the model, re-predicts the next few days of games and grades finished ones several times a day, so it keeps itself current through the season. A walk-forward backtest over 2016-17 to 2025-26 scores it against Elo and a goals-only Poisson model. See [NHLScorePredictor](NHLScorePredictor) and the [latest predictions](NHLScorePredictor/predictions/README.md).

## ScheduleOptimizer
#### This C++ program reads course information from a file named `sections.txt`, where each line contains a course name and a professor's last name. It then assigns each course a schedule, ensuring that no professor teaches two different classes at the same time. The program randomly assigns each course to meet on either Monday, Wednesday, and Friday for 1 hour each day, or on Tuesday and Thursday for 1.5 hours each day, between 7am and 6pm. The final schedule, including the course name, professor's name, meeting days, start time, and end time, is then saved to a file named `best_schedule.txt`.
