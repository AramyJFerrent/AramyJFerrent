#include "UnknownStudentException.h"

UnknownStudentException::UnknownStudentException(const std::string& studentName)
    : studentName(studentName) {}

const char* UnknownStudentException::what() const noexcept {
    return ("Unknown student: " + studentName).c_str();
}
