from singleton_decorator import singleton


@singleton
class Person:

    person_details = None

    def __init__(self, *args, **kwargs):
        key_list = ["name", "age", "gender"]
        result = kwargs
        if args:
            for arg in args:
                result[key_list[args.index(arg)]] = arg
        self.person_details = result

    def get_person_details(self):
        return self.person_details


p1 = Person("P1 sushrut", age="18", gender="male")
p2 = Person("P2 sushrut", "18", "male")
p3 = Person(name="sushrut", age="18", gender="male")

print "P1 personal details ", p1.get_person_details()
print "P2 personal details ", p2.get_person_details()
print "P3 personal details ", p3.get_person_details()