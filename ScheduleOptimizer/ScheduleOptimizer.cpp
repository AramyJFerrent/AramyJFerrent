#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cstdlib>

struct ClassSchedule {
    std::string className;
    std::string professorName;
    std::vector<std::string> meetingDays;
    int startTime;
    int endTime;
};

bool overlaps(const ClassSchedule& a, const ClassSchedule& b) {
    for (const auto& day : a.meetingDays) {
        if (std::find(b.meetingDays.begin(), b.meetingDays.end(), day) != b.meetingDays.end()) {
            if (a.startTime < b.endTime && b.startTime < a.endTime) {
                return true;
            }
        }
    }
    return false;
}

void assignSchedule(std::vector<ClassSchedule>& schedules) {
    std::vector<std::vector<bool>> scheduleMatrix(5, std::vector<bool>(12, false)); // 5 days, 12 hours (7am to 6pm)

    // Seed the random number generator
    std::srand(std::time(nullptr));

    for (auto& schedule : schedules) {
        bool scheduled = false;
        while (!scheduled) {
            size_t day = std::rand() % 5;
            size_t hour = std::rand() % 12;
            bool canSchedule = true;
            for (const auto& other : schedules) {
                if (&other != &schedule && overlaps(schedule, other)) {
                    canSchedule = false;
                    break;
                }
            }
            if (canSchedule) {
                schedule.meetingDays.push_back(day < 3 ? "MWF" : "TTh");
                schedule.startTime = 7 + hour;
                schedule.endTime = schedule.startTime + (day < 3 ? 1 : 1.5);
                scheduled = true;
            }
        }
    }
}

void outputSchedule(const std::vector<ClassSchedule>& schedules) {
    std::ofstream outfile("best_schedule.txt");
    if (outfile.is_open()) {
        for (const auto& schedule : schedules) {
            outfile << schedule.className << " with " << schedule.professorName << " meets on ";
            for (size_t i = 0; i < schedule.meetingDays.size(); ++i) {
                if (i != 0) outfile << ", ";
                outfile << schedule.meetingDays[i];
            }
            outfile << " from " << schedule.startTime << ":00 to " << schedule.endTime << ":00\n";
        }
        outfile.close();
        std::cout << "Schedule saved to best_schedule.txt\n";
    }
    else {
        std::cerr << "Unable to open file for output.\n";
    }
}

int main() {
    std::ifstream infile("sections.txt");
    if (!infile.is_open()) {
        std::cerr << "Unable to open file.\n";
        return 1;
    }

    std::vector<ClassSchedule> schedules;
    std::string className, professorName;
    while (infile >> className >> professorName) {
        ClassSchedule schedule;
        schedule.className = className;
        schedule.professorName = professorName;
        schedules.push_back(schedule);
    }
    infile.close();

    assignSchedule(schedules);
    outputSchedule(schedules);

    return 0;
}
