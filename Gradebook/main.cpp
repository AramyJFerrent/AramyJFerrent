/* 
 * This file contains the main function, which reads student assessments from an input file and calculates and prints the grades using the GradeBook class.
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "GradeBook.h"
#include "Essay.h"
#include "TeamProject.h"

int main() {
    // Open the input file
    std::ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open the input file." << std::endl;
        return 1;
    }

    // Create a GradeBook object
    GradeBook gradeBook;
    std::string courseName;
    std::string line;
    // Read the course name from the first line of the input file
    getline(inputFile, courseName);
    gradeBook.setName(courseName);

    // Read student assessments from the input file
    while (getline(inputFile, line)) {
        std::istringstream iss(line);
        std::string studentName, type;
        double grade1, grade2;

        // Parse student name, assessment type, and grades from the line
        if (!(iss >> studentName >> type >> grade1)) {
            std::cerr << "Error reading line: " << line << std::endl;
            continue;
        }

        // Create and add an Essay assessment if the type is 'e'
        if (type == "e") {
            Essay* essay = new Essay(studentName);
            essay->setGrade(grade1);
            gradeBook.addAssessment(studentName, essay);
        }
        // Create and add a TeamProject assessment if the type is 'tp'
        else if (type == "tp") {
            if (!(iss >> grade2)) {
                std::cerr << "Error reading line: " << line << std::endl;
                continue;
            }
            TeamProject* teamProject = new TeamProject(studentName);
            teamProject->setIndividualGrade(grade1);
            teamProject->setTeamGrade(grade2);
            gradeBook.addAssessment(studentName, teamProject);
        }
        // Handle unknown assessment types
        else {
            std::cerr << "Unknown assessment type: " << type << std::endl;
        }
    }

    // Print the grades
    gradeBook.printGrades();

    // Close the input file
    inputFile.close();

    return 0;
}
