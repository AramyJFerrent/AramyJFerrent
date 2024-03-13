/* 
 * This file contains the implementation of the UnknownStudentException class, which is used to represent exceptions related to unknown students in the program. 
 * It includes a constructor that takes a student name as input and a method to retrieve the exception message.
 */

#include "UnknownStudentException.h"

// Constructor
UnknownStudentException::UnknownStudentException(const std::string& studentName)
    : studentName(studentName) {}

// Method to retrieve the exception message
const char* UnknownStudentException::what() const noexcept {
    return ("Unknown student: " + studentName).c_str();
}
