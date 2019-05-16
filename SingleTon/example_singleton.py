#!/bin/python


class Myclass:

    my_instance = None
    age = 18

    def __new__(self):
        if self.my_instance:
            return self.my_instance()
        else:
            return Myclass()

    def set_min_age(self, age):
        self.age = age

    def get_min_age(self):
        print self.age
        return self.age


mc1 = Myclass()
mc1.get_min_age()
mc1.set_min_age(21)
mc1.get_min_age()


mc2 = Myclass()
mc2.get_min_age()
