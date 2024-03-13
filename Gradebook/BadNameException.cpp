/* 
 * This file contains the implementation of the BadNameException class, which is used to represent exceptions related to bad names (e.g., empty names) in the program. 
 * It includes a constructor that takes a message as input and a method to retrieve the exception message.
 */

#include "BadNameException.h"

// Constructor
BadNameException::BadNameException(const std::string& message) : message(message) {}

// Method to retrieve the exception message
const char* BadNameException::what() const noexcept {
    return message.c_str();
}
