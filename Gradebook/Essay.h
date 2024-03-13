/* 
 * This file contains the declaration of the Essay class, which represents an essay assessment in a student grading system. 
 * It inherits from the Assessment class and includes methods to get and set the essay's grade.
 */

#ifndef ESSAY_H
#define ESSAY_H

#include "Assessment.h"

class Essay : public Assessment {
public:
    // Constructor
    Essay(const std::string& name);
    // Method to get the essay's grade
    double getGrade() const;
    // Method to set the essay's grade, with bounds checking
    void setGrade(double newGrade);

private:
    double grade;
};

#endif
