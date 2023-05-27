#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
class Person:
    approved_jobs = ["Sales", "Engineer", "Teacher", "ITC"]

    def __init__(self, name="", job=""):
        self.name = self.validate_name(name)
        self.job = self.validate_job(job)

    def validate_name(self, name):
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be a string between 1 and 25 characters.")
            return ""
        return name.title()

    def validate_job(self, job):
        if job not in self.approved_jobs:
            print("Job must be in the list of approved jobs.")
            return ""
        return job
