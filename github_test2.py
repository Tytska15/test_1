users = [
    {"name": "Anna", "age": 25},
    {"name": "Bob", "age": -3},
    {"name": "John", "age": 130},
    {"name": "Kate", "age": 17},
]
valid = 0
invalid = 0

for user in users:
    age = user["age"]
    if age < 0 or age > 120:
        invalid += 1
    else:
        valid += 1

print("Valid", valid)
print("Invalid", invalid)

if invalid > 0:
    print("Test Failed")
else:
    print("Test Passed")

