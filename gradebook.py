#1. Gradebook dictionary
#key is subject, value is list of grades
gradebook = {"Math": [60, 30, 70, 57], "English": [88, 90, 93], "History": [82, 87, 90], "Comp Sci": [90, 87, 75, 80]}

#2. add_grade(subject, grade):
#add a grade to subjects list
#if subject isn't in gradebook yet, creates the subject first and then adds the grade
def add_grade(subject, grade):
    #create empty list if subject not in gradebook yet
    if subject not in gradebook:
        gradebook[subject] = []
    #add grade to subject list
    gradebook[subject].append(grade)
    


def main():
    #testing add_grade method:
    add_grade("Math", 100)
    add_grade("Physics", 88)
    print(gradebook) 


if __name__ == "__main__":
    main()