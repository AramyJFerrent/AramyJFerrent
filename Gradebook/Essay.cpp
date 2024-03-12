#include "Essay.h"

Essay::Essay(const std::string& name) : Assessment(name), grade(0.0) {}

double Essay::getGrade() const {
    return grade;
}

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
