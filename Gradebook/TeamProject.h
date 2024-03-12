#ifndef TEAMPROJECT_H
#define TEAMPROJECT_H

#include "Assessment.h"

class TeamProject : public Assessment {
public:
    TeamProject(const std::string& name);
    double getGrade() const override;

    double getIndividualGrade() const;
    double getTeamGrade() const;
    void setIndividualGrade(double newGrade);
    void setTeamGrade(double newGrade);

private:
    double individualGrade;
    double teamGrade;
};

#endif
