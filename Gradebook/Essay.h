#ifndef ESSAY_H
#define ESSAY_H

#include "Assessment.h"

class Essay : public Assessment {
public:
    Essay(const std::string& name);
    double getGrade() const;
    void setGrade(double newGrade);

private:
    double grade;
};

#endif
