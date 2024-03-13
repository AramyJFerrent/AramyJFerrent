/* 
 * This file contains the implementation of the Assessment class, which represents an assessment (e.g., exam, quiz, project) in a student grading system. 
 * It includes methods to get and set the assessment's name, as well as a pure virtual method to get the grade of the assessment.
 */

#include "Assessment.h"
#include "BadNameException.h"

// Constructor
Assessment::Assessment(const std::string& name) : name(name) {
    if (name.empty()) {
        throw BadNameException("Assessment name cannot be empty.");
    }
}

// Getter for name
const std::string& Assessment::getName() const {
    return name;
}

// Setter for name
void Assessment::setName(const std::string& name) {
    if (name.empty()) {
        throw BadNameException("Assessment name cannot be empty.");
    }
    this->name = name;
}
