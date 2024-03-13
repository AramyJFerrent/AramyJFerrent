/* 
 * This file contains the declaration of the Assessment class, which represents an assessment (e.g., exam, quiz, project) in a student grading system. 
 * It includes a pure virtual method to get the grade of the assessment, as well as methods to get and set the assessment's name.
 */

#ifndef ASSESSMENT_H
#define ASSESSMENT_H

#include <string>

class Assessment {
public:
    // Constructor
    Assessment(const std::string& name);
    // Virtual destructor
    virtual ~Assessment() = default;

    // Pure virtual method to get the grade
    virtual double getGrade() const = 0;

    // Getter for name
    const std::string& getName() const;
    // Setter for name
    void setName(const std::string& name);

private:
    std::string name;
};

#endif
