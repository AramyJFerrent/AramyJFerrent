#include "BadNameException.h"

BadNameException::BadNameException(const std::string& message) : message(message) {}

const char* BadNameException::what() const noexcept {
    return message.c_str();
}
