numbers = [5, 12, 7, 20, 3, 8, 15, 2, 30]

count = 0
summa = 0
max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    if n > 10:
        count += 1
    if n <= 10:
        summa += n
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n
        
print("Max:", max_num)
print("Min:", min_num)
print(count)
print(summa)



numbers = [3, 10, 5, 8, 20, 7, 6, 15, 2]

count_even = 0
sum_odd = 0
max_even = None
min_odd = None

for n in numbers:
    if n % 2 == 0:
        count_even += 1
        
        if max_even is None or n > max_even:
            max_even = n
    else:
        sum_odd += n
        
        if min_odd is None or n < min_odd:
            min_odd = n

print("Count even:", count_even)
print("Sum odd:", sum_odd)
print("Max even:", max_even)
print("Min odd:", min_odd)

        

    