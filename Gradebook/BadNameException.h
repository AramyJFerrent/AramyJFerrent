/* 
 * This file contains the declaration of the BadNameException class, which is used to represent exceptions related to bad names (e.g., empty names) in the program. 
 * It inherits from std::exception and includes a constructor that takes a message as input, as well as a method to retrieve the exception message.
 */

#ifndef BADNAMEEXCEPTION_H
#define BADNAMEEXCEPTION_H

#include <exception>
#include <string>

class BadNameException : public std::exception {
public:
    // Constructor
    BadNameException(const std::string& message);
    // Method to retrieve the exception message
    const char* what() const noexcept override;
private:
    std::string message;
};

#endif
