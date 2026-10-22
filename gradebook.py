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
#calcs average of grades for a subject and prints (rounded to 2 decimal values)
def print_average(subject):
    grades = gradebook[subject]
    #can use sum to add grades and divide by the quantity of values (length)
    average = sum(grades)/len(grades)
    #get it to round to 2 places
    average = round(average * 100) / 100
    print(subject + " average: " + str(average))

#4. print_grades(subject):
#prints all grades for chosen subject
def print_grades(subject):
    grades = gradebook[subject]
    #create empty string
    result = ""
    #add each grade w/ spacing commas
    for i in range(len(grades)):
        result = result + str(grades[i])
        #dont add comma for the last one
        if i < len(grades)-1:
            result = result + ", "
    print(subject + " grades: " + result)

#5. print_all_averages():
#prints all subjects and their averages
#indicate best and worst subjects (based on avgs) by keeping track while looping
def print_all_averages():
    # use the first subject as the starting point for best and worst
    first = list(gradebook.keys())[0]
    first_grades = gradebook[first]
    best = first
    worst = first
    best_avg = sum(first_grades) / len(first_grades)
    best_avg = round(best_avg * 100) / 100
    worst_avg = best_avg

    for subject in gradebook:
        grades = gradebook[subject]
        average = sum(grades)/len(grades)
        average = round(average * 100) / 100
        print(subject + ": " + str(average))
        if average > best_avg:
            best_avg = average
            best = subject
        if average < worst_avg:
            worst_avg = average
            worst = subject
    print("Best subject: " + best)
    print("Worst subject: " + worst)
    




def main():
    #testing add_grade method:
    add_grade("Math", 100)
    add_grade("Physics", 88)
    print(gradebook) 
    #testing print_average:
    print_average("Math")
    #testing print_grades:
    print_grades("English")
    print_grades("Comp Sci")
    #testing print_all_averages:
    print_all_averages()

if __name__ == "__main__":
    main()