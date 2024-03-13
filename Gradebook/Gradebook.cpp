/* 
 * This file contains the implementation of the GradeBook class, which manages student assessments and grades for a course.
 * It includes methods to set and get the course name, add assessments for students, calculate grades, and print grades.
 */

#include <iostream> 
#include <iomanip>
#include "GradeBook.h"
#include "UnknownStudentException.h"
#include "Assessment.h"

// Constructor
GradeBook::GradeBook() : courseName(""), studentAssessments() {}

// Set the name of the course
void GradeBook::setName(const std::string& newCourseName) {
    courseName = newCourseName;
}

// Get the name of the course
std::string GradeBook::getName() const {
    return courseName;
}

// Add an assessment for a student
void GradeBook::addAssessment(const std::string& studentName, Assessment* newAssessment) {
    studentAssessments[studentName].push_back(newAssessment);
}

// Calculate the grade for a student
double GradeBook::getGrade(const std::string& studentName) const {
    auto it = studentAssessments.find(studentName);
    if (it == studentAssessments.end()) {
        throw UnknownStudentException(studentName);
    }

    double totalGrade = 0.0;
    for (const Assessment* assessment : it->second) {
        totalGrade += assessment->getGrade();
    }

    return totalGrade / it->second.size();
}

// Print the grades for all students
void GradeBook::printGrades() const {
    std::cout << "Grades for " << courseName << std::endl;
    for (const auto& student : studentAssessments) {
        double grade = getGrade(student.first);
        std::cout << student.first << ": " << std::fixed << std::setprecision(2) << grade << std::endl;
    }
}
