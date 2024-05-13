class Person:
    def __init__(self, name):
        """This defines a class called person"""
        self.name = ""

    def introduction(self):
        print("My name is", self.name)


Customer = Person()
"""This creates an instance of person called Customer."""
Customer.name = "John Smith"

Customer.introduction()

