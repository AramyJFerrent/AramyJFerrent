#include <iostream> 
#include <iomanip>
#include "GradeBook.h"
#include "UnknownStudentException.h"
#include "Assessment.h"


GradeBook::GradeBook() : courseName(""), studentAssessments() {}

void GradeBook::setName(const std::string& newCourseName) {
    courseName = newCourseName;
}

std::string GradeBook::getName() const {
    return courseName;
}

void GradeBook::addAssessment(const std::string& studentName, Assessment* newAssessment) {
    studentAssessments[studentName].push_back(newAssessment);
}

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

void GradeBook::printGrades() const {
    std::cout << "Grades for " << courseName << std::endl;
    for (const auto& student : studentAssessments) {
        double grade = getGrade(student.first);
        std::cout << student.first << ": " << std::fixed << std::setprecision(2) << grade << std::endl;
    }
}
