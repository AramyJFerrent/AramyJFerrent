/* 
 * This file contains the declaration of the TeamProject class, which represents a team project assessment in a student grading system. 
 * It inherits from the Assessment class and includes methods to calculate the overall grade for the project, as well as methods to get and set individual and team grades.
 */

#ifndef TEAMPROJECT_H
#define TEAMPROJECT_H

#include "Assessment.h"

class TeamProject : public Assessment {
public:
    // Constructor
    TeamProject(const std::string& name);
    // Method to calculate the overall grade for the project
    double getGrade() const override;

    // Getter for individual grade
    double getIndividualGrade() const;
    // Getter for team grade
    double getTeamGrade() const;
    // Setter for individual grade
    void setIndividualGrade(double newGrade);
    // Setter for team grade
    void setTeamGrade(double newGrade);

private:
    double individualGrade;
    double teamGrade;
};

#endif
