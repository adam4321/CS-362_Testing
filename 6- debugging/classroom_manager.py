"""
CS362 Assignment 4
File Under test
Edited starting on Tues Feb 11 2020
@author: Adam Wright
"""

# Student class
class Student:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = []

    def get_full_name(self):
        return str(self.first_name + " " + self.last_name)

    def submit_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments

    def get_assignment(self, name):
        for a in self.assignments:
            if a.name == name:
                return a

    def get_average(self):
        sum_grades = 0
        total_assignments = 0
        for a in self.assignments:
            if a.grade != -1:
                sum_grades = sum_grades + a.grade
                total_assignments = total_assignments + a.max_score
        if total_assignments != 0:
            average = sum_grades / total_assignments
            return average
        else:
            return 0

    def remove_assignment(self, name):
        for a in self.assignments:
            if a.name == name:
                self.assignments.remove(a)

# Assignment class
class Assignment:
    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = -1

    def assign_grade(self, grade):
        self.grade = grade
        if self.grade > self.max_score:
            self.grade = -1
