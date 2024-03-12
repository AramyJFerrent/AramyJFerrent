#ifndef BADNAMEEXCEPTION_H
#define BADNAMEEXCEPTION_H

#include <exception>
#include <string>

class BadNameException : public std::exception {
public:
    BadNameException(const std::string& message);
    const char* what() const noexcept override;
private:
    std::string message;
};

#endif
