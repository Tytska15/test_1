class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >=18
    
    def is_valid_age(self):
        return self.age >= 0 and self.age <= 120
    
u1 = User("Anna", 25)
u2 = User("Kate", 15)
u3 = User("Bob", -5)
u4 = User("John", 130)

print(u1.name, u1.is_adult())
print(u2.name, u2.is_adult())
print(u3.name, u3.is_valid_age())
print(u4.name, u4.is_valid_age())
