/* 
 * Name: [Your Name]
 * Course: [Course Number and Section]
 * Project: [Project Number]
 * 
 * File Contents / Structure:
 * This file contains the implementation of the Essay class, which represents an essay assessment in a student grading system. 
 * It includes methods to get and set the essay's grade.
 */

#include "Essay.h"

// Constructor
Essay::Essay(const std::string& name) : Assessment(name), grade(0.0) {}

// Getter for grade
double Essay::getGrade() const {
    return grade;
}

// Setter for grade
void Essay::setGrade(double newGrade) {
    if (newGrade < 0.0) {
        grade = 0.0;
    }
    else if (newGrade > 4.0) {
        grade = 4.0;
    }
    else {
        grade = newGrade;
    }
}
