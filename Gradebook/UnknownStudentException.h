/* 
 * This file contains the declaration of the UnknownStudentException class, which is used to represent exceptions related to unknown students in the program. 
 * It inherits from std::exception and includes a constructor that takes a student name as input, as well as a method to retrieve the exception message.
 */

#ifndef UNKNOWNSTUDENTEXCEPTION_H
#define UNKNOWNSTUDENTEXCEPTION_H

#include <exception>
#include <string>

class UnknownStudentException : public std::exception {
public:
    // Constructor
    UnknownStudentException(const std::string& studentName);
    // Method to retrieve the exception message
    const char* what() const noexcept override;
private:
    std::string studentName;
};

#endif
