#1. gradebook dictionary
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

#3. print_average(subject):
#Prints average of grades for a subject and prints (rounded to 2 decimal values)
def print_average(subject):
    grades = gradebook[subject]
    #can use sum to add grades and divide by the quantity of values (length)
    average = sum(grades)/len(grades)
    #get it to round to 2 places
    average = round(average * 100) / 100
    print(subject + " average: " + str(average))


def main():
    #testing print_average:
    print_average("Math")

if __name__ == "__main__":
    main()