#ifndef UNKNOWNSTUDENTEXCEPTION_H
#define UNKNOWNSTUDENTEXCEPTION_H

#include <exception>
#include <string>

class UnknownStudentException : public std::exception {
public:
    UnknownStudentException(const std::string& studentName);
    const char* what() const noexcept override;
private:
    std::string studentName;
};

#endif
