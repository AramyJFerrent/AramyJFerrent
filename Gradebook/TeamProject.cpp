#include "TeamProject.h"

TeamProject::TeamProject(const std::string& name) : Assessment(name), individualGrade(0.0), teamGrade(0.0) {}

double TeamProject::getGrade() const {
    return (individualGrade + teamGrade) / 2;
}

double TeamProject::getIndividualGrade() const {
    return individualGrade;
}

double TeamProject::getTeamGrade() const {
    return teamGrade;
}

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
