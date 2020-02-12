"""
CS362 Assignment 4
Unit test file for classroom_manager.py
Created on Tues Feb 11 2020
@author: Adam Wright
"""

import classroom_manager
from unittest import TestCase

class Test_Student(TestCase):
    def set_up(self):
        # Set up test student values
        self.id = 4123
        self.first_name = "Adam"
        self.last_name = "Wright"
        self.assignments = []

        # Create a test student and test assignment
        self.test_student = classroom_manager.Student(4123, "Adam", "Wright")
        self.test_assignment = classroom_manager.Assignment("Assignment4", 100)
        self.test_assignment2 = classroom_manager.Assignment("Assignment5", 100)

    def test_init(self):
        self.set_up()

        # Test that the test student holds the set up values
        self.assertEqual(self.id, self.test_student.id)
        self.assertEqual(self.first_name, self.test_student.first_name)
        self.assertEqual(self.last_name, self.test_student.last_name)
        self.assertEqual(self.assignments, self.test_student.assignments)

    def test_get_full_name(self):
        self.set_up()
        test_full_name = "Adam Wright"

        # Test that get full name returns the correct format
        self.assertEqual(test_full_name, self.test_student.get_full_name())

    def test_submit_assignment(self):
        self.set_up()

        # Test that assignments list is initially empty
        self.assertEqual(self.assignments, self.test_student.assignments)

        # Submit the test assignment
        self.test_student.submit_assignment(self.test_assignment)

        # Test that assignments list contains the submitted assignment
        self.assignments = [self.test_assignment]
        self.assertEqual(self.assignments, self.test_student.assignments)

    def test_get_assignments(self):
        self.set_up()

        # Submit two test assignments
        self.test_student.submit_assignment(self.test_assignment)
        self.test_student.submit_assignment(self.test_assignment2)

        # Return the current assignments
        test_getter = self.test_student.get_assignments()

        # Check that the test list equals the test student's list
        self.assertEqual(self.test_student.assignments, test_getter)

    def test_get_assignment(self):
        self.set_up()
        self.test_student.submit_assignment(self.test_assignment)

        # Return the named assignment
        test_getter = self.test_student.get_assignment(self.test_assignment.name)

        # Check that the returned assignment equals the test assignment
        self.assertEqual(self.test_assignment, test_getter)

        # Check for a non-existing assignment
        test_getter = self.test_student.get_assignment("foo")
        self.assertEqual(test_getter, None)

    def test_get_average(self):
        self.set_up()



    def test_remove_assignment(self):
        self.set_up()


class Test_Assignment(TestCase):
    def set_up(self):
        self.name = "Assignment4"
        self.max_score = 100
        self.grade = -1

        # Create a test assignment instance
        self.test_assignment = classroom_manager.Assignment("Assignment4", 100)

    def test_init(self):
        self.set_up()

        # Local instance to test against
        local_assignment = classroom_manager.Assignment("Assignment4", 100)

        # Test that the local assignment and the setup up assignment have the same props set
        self.assertEqual(local_assignment.name, self.test_assignment.name)
        self.assertEqual(local_assignment.max_score, self.test_assignment.max_score)
        self.assertEqual(local_assignment.grade, self.test_assignment.grade)

    def test_assign_grade(self):
        self.set_up()

        # Create a test assignment with a proper grade
        self.test_assignment.assign_grade(98)
        self.assertEqual(self.test_assignment.grade, 98)

        # Create a test assignment with an out of range grade
        test_assignment2 = classroom_manager.Assignment("Assignment5", 100)
        test_assignment2.assign_grade(101)

        self.assertEqual(test_assignment2.grade, -1)

        # Create a test assignment with a full grade
        test_assignment2 = classroom_manager.Assignment("Assignment5", 100)
        test_assignment2.assign_grade(100)

        self.assertEqual(test_assignment2.grade, 100)
