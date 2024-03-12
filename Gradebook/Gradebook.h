#ifndef GRADEBOOK_H
#define GRADEBOOK_H

#include <string>
#include <map>
#include <vector>

class Assessment;

class GradeBook {
public:
    GradeBook();
    virtual ~GradeBook() = default;

    void setName(const std::string& newCourseName);
    std::string getName() const;

    void addAssessment(const std::string& studentName, Assessment* newAssessment);
    double getGrade(const std::string& studentName) const;

    void printGrades() const;

private:
    std::string courseName;
    std::map<std::string, std::vector<Assessment*>> studentAssessments;
};

#endif
