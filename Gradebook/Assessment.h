#ifndef ASSESSMENT_H
#define ASSESSMENT_H

#include <string>

class Assessment {
public:
    Assessment(const std::string& name);
    virtual ~Assessment() = default;

    virtual double getGrade() const = 0;

    const std::string& getName() const;
    void setName(const std::string& name);

private:
    std::string name;
};

#endif
