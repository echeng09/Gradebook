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
    #average = round(average * 100) / 100
    average = round(average, 2)
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
    best_avg = round(best_avg, 2)
    worst_avg = best_avg

    for subject in gradebook:
        grades = gradebook[subject]
        average = sum(grades)/len(grades)
        average = round(average, 2)
        print(subject + ": " + str(average))
        if average > best_avg:
            best_avg = average
            best = subject
        if average < worst_avg:
            worst_avg = average
            worst = subject
    print("Best subject: " + best)
    print("Worst subject: " + worst)
    
#6. get_GPA():
#returns GPA across all subjects on a 4.0 scale
#converts each subject's avg to grade points using the chart, then averages those points
def get_GPA():
    tot = 0
    for subject in gradebook:
        grades = gradebook[subject]
        avg = sum(grades)/len(grades)
        avg = round(avg, 2)
        #convert average to GPA
        #A
        if avg >= 92.5:
            points = 4.0 
        #A-
        elif avg >= 89.5 and avg <= 92.49:
            points = 3.7 
        #B
        elif avg >= 79.5 and avg <= 89.49:
            points = 3.0
        #C
        elif avg >= 69.5 and avg <= 79.49:
            points = 2.0
        #D
        elif avg >= 65 and avg <= 69.49:
            points = 1.0
        else:
            points = 0
        tot = tot + points
    #rounding gpa to 2 decimals (i think that's what it usually is???)
    return round(tot/len(gradebook),2)



def main():
    #loop
    while True:
        #user choices
        print("GRADEBOOK MAIN MENU")
        print("1. Show all classes and averages")
        print("2. Show all grades for a class")
        print("3. Show GPA")
        print("4. Add a grade")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print_all_averages()
        elif choice == "2":
            #ask for class
            subject = input("Which class? ")
            print_grades(subject)
        elif choice == "3":
            print("Your GPA: " + str(get_GPA()))
        elif choice == "4":
            user_subject = input("Which class? ")
            user_grade = float(input("What grade? "))
            add_grade(user_subject, user_grade)
            print("Added " + str(user_grade) + " to " + user_subject + ".")
        else: 
            print("Try again.")
        print("Returning to main menu...")
        print()


    #OLD TESTING BELOW:
    #testing add_grade method:
    #add_grade("Math", 100)
    #add_grade("Physics", 88)
    #print(gradebook) 
    #testing print_average:
    #print_average("Math")
    #testing print_grades:
    #print_grades("English")
    #print_grades("Comp Sci")
    #testing print_all_averages:
    #print_all_averages()
    #test get_GPA:
    #print(get_GPA())

if __name__ == "__main__":
    main()