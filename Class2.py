class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

    def is_valid_age(self):
        return self.age >=0 and self.age <= 120
    
    def is_child(self):
         return self.age < 18
    
users = [
    User("Anna", 25),
    User("Kate", 15),
    User("Bob", -5),
    User("John", 130),
    User("Mike", 45),
]
has_invalid = False
child_count = 0
adult_count = 0

for u in users:
    if not u.is_valid_age():
        has_invalid = True
    if u.age <= 18:
         child_count += 1
    else:
         adult_count += 1
print("Children", child_count)
print("Adults:", adult_count)

if has_invalid:
        print("Test Failed")
else:
        print("Test Passed")
