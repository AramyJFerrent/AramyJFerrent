/* 
 * This file contains the implementation of the TeamProject class, which represents a team project assessment in a student grading system. 
 * It includes methods to calculate the overall grade for the project, as well as methods to get and set individual and team grades.
 */

#include "TeamProject.h"

// Constructor
TeamProject::TeamProject(const std::string& name) : Assessment(name), individualGrade(0.0), teamGrade(0.0) {}

// Calculate the overall grade for the project
double TeamProject::getGrade() const {
    return (individualGrade + teamGrade) / 2;
}

// Get the individual grade
double TeamProject::getIndividualGrade() const {
    return individualGrade;
}

// Get the team grade
double TeamProject::getTeamGrade() const {
    return teamGrade;
}

// Set the individual grade with bounds checking
void TeamProject::setIndividualGrade(double newGrade) {
    if (newGrade < 0.0) {
        individualGrade = 0.0;
    }
    else if (newGrade > 4.0) {
        individualGrade = 4.0;
    }
    else {
        individualGrade = newGrade;
    }
}

// Set the team grade with bounds checking
void TeamProject::setTeamGrade(double newGrade) {
    if (newGrade < 0.0) {
        teamGrade = 0.0;
    }
    else if (newGrade > 4.0) {
        teamGrade = 4.0;
    }
    else {
        teamGrade = newGrade;
    }
}
