grade = float(input("Enter the grade in the decimal system: "))

if grade >= 9.5:
    alphabetic_grade = 'A+'
    fourth_system_grade = '10'
elif grade >= 8.5:
    alphabetic_grade = 'A'
    fourth_system_grade = '9'
elif grade >= 7.5:
    alphabetic_grade = 'B+'
    fourth_system_grade = '8'
elif grade >= 6.5:
    alphabetic_grade = 'B'
    fourth_system_grade = '7'
elif grade >= 5.5:
    alphabetic_grade = 'C'
    fourth_system_grade = '6'
elif grade >= 4.5:
    alphabetic_grade = 'D'
    fourth_system_grade = '5'
else:
    alphabetic_grade = 'F'
    fourth_system_grade = '0'

print("Alphabetic Grade:", alphabetic_grade)
print("4th System Grade:", fourth_system_grade)