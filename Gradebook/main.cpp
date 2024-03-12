#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "GradeBook.h"
#include "Essay.h"
#include "TeamProject.h"

int main() {
    std::ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open the input file." << std::endl;
        return 1;
    }

    GradeBook gradeBook;
    std::string courseName;
    std::string line;
    getline(inputFile, courseName);
    gradeBook.setName(courseName);

    while (getline(inputFile, line)) {
        std::istringstream iss(line);
        std::string studentName, type;
        double grade1, grade2;

        if (!(iss >> studentName >> type >> grade1)) {
            std::cerr << "Error reading line: " << line << std::endl;
            continue;
        }

        if (type == "e") {
            Essay* essay = new Essay(studentName);
            essay->setGrade(grade1);
            gradeBook.addAssessment(studentName, essay);
        }
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
        else {
            std::cerr << "Unknown assessment type: " << type << std::endl;
        }
    }

    gradeBook.printGrades();

    inputFile.close();

    return 0;
}
