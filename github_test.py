ages = [12, 25, 17, 40, 8, 19, 60, 14, 33]

adult_count = 0
child_count = 0
max_ages = ages[0]
min_ages = ages[0]
has_invalid = False

for age in ages:
    if age > 18:
        adult_count += 1
    else:
        child_count += 1
    if age > max_ages:
        max_ages = age
    if age < min_ages:
        min_ages = age
    if age < 0 or age > 120:
        has_invalid = True
    


print("Adults:", adult_count)
print("Children:", child_count)
print("Max age:", max_ages)
print("Min age:", min_ages)
print("Has invalid", has_invalid)





        

    