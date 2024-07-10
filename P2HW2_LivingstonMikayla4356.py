# Mikayla A. Livingston 
# 07/10/24
# P2HW2
# Assignment assess student understanding of Lists



print("This program calculates and displays grade average\n")

#Request information

modOne = float(input("Enter grade for Module 1: "))
modTwo = float(input("Enter grade for Module 2: "))
modThree = float(input("Enter grade for Module 3: "))
modFour = float(input("Enter grade for Module 4: "))
modFive = float(input("Enter grade for Module 5: "))
modSix = float(input("Enter grade for Module 6: "))
print()

print("\n------------Results------------")

# program to find the lowest grade
# number list

listOne = [modOne,modTwo,modThree,modFour,modFive,modSix]

# sorting of the grade lists

listOne.sort()

# retrieving lowest grade
print("Lowest Grade:", min(listOne))

# retrieving highest grade

print(f"Highest Grade:", max(listOne))

# adding grades for sum or total

print("Sum of Grades:", sum(listOne))

# getting our average of grades

print('Average:', sum(listOne)/len(listOne))

print("\n----------------------------------")
