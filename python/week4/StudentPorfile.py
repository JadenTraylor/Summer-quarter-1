student = {}

studentName = input("Enter your student's name:")
student["Name"] = studentName


age = {}

studentAge = input("Enter your student's age:")
student["Age"] = studentAge

studentGrade = input("Enter student's grade:")
student["Grade"] = studentGrade

hobbies = []
hobby = input("Enter your student's hobby; Type 'done' when done").lower()
hobbies.append(hobby)

while hobby != "done":
    hobby = input("Enter your student's hobby; Type 'done' when done").lower()
    hobbies.append(hobby)

student["Hobbies"] = hobbies

print(student)

