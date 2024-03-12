#include "Assessment.h"
#include "BadNameException.h"

Assessment::Assessment(const std::string& name) : name(name) {
    if (name.empty()) {
        throw BadNameException("Assessment name cannot be empty.");
    }
}

const std::string& Assessment::getName() const {
    return name;
}

void Assessment::setName(const std::string& name) {
    if (name.empty()) {
        throw BadNameException("Assessment name cannot be empty.");
    }
    this->name = name;
}
