

# my_dict = {
#     "A":"my alphabet A",
#     "B":"my alphabet B",
#     "C":"my alphabet C",
#     "D":"my alphabet D"
# }

# print(my_dict["A"])

# for thing in my_dict:
#     print(my_dict[thing])


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for i in student_scores:
    score = student_scores[i]
    
    if score >= 91:
        grade = "Outstanding"
    elif score >=81:
        grade = "Exceeds Expectations"
    elif score >=71:
        grade =  "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[i] = grade
    
    
print(student_grades)
