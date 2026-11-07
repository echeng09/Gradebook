#gradebook dictionary
#key is subject, value is list of grades
#now starts empty (w/ extension project), gets filled in from grades.csv by load_grades()
gradebook = {}

#EXTENSION: load_grades():
#reads grades.csv and saves into gradebook
def load_grades():
    #I searched up how to do this (forgot how to use the csv file)
    #EXTENSION: if file doesn't exist start w/ empty gradebook
    try:
        file = open("grades.csv", "r")
    except FileNotFoundError:
        print("grades.csv was not found, starting with an empty gradebook")
        return
    for line in file:
        parts = line.split(",")
        subject = parts[0]
        grades = []
        for i in range(1, len(parts)):
            grades.append(float(parts[i]))
        gradebook[subject] = grades
    file.close()




#add_grade(subject, grade):
#add a grade to subjects list
#if subject isn't in gradebook yet, creates the subject first and then adds the grade
def add_grade(subject, grade):
    #create empty list if subject not in gradebook yet
    #EXTENSION: let user know new subject was created
    if subject not in gradebook:
        gradebook[subject] = []
        print("New class " + subject + " created")
    #add grade to subject list
    gradebook[subject].append(grade)

#print_average(subject):
#calcs average of grades for a subject and prints (rounded to 2 decimal values)
def print_average(subject):
    #EXTENSION: if no grades, divides by zero so need to fix that
    if len(gradebook[subject]) == 0:
        print(subject + " has no grades yet, so no average yet")
        return
    grades = gradebook[subject]
    #can use sum to add grades and divide by the quantity of values (length)
    average = sum(grades)/len(grades)
    #get it to round to 2 places 
    #average = round(average * 100) / 100
    average = round(average, 2)
    print(subject + " average: " + str(average))

#print_grades(subject):
#prints all grades for chosen subject
def print_grades(subject):
    #EXTENSION: tell user if class has no grades
    if len(gradebook[subject]) == 0:
        print(subject + " has no grades yet")
        return
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

#print_all_averages():
#prints all subjects and their averages
#indicate best and worst subjects (based on avgs) by keeping track while looping
def print_all_averages():
    #EXTENSION: shows nothing if gradebook is empty so fixes that
    if len(gradebook) == 0:
        print("no grades in the gradebook yet, add one w/ option 4")
        return
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
    
#get_GPA():
#returns GPA across all subjects on a 4.0 scale
#converts each subject's avg to grade points using the chart, then averages those points
def get_GPA():
    #EXTENSION: cannot calc GPA w/o subjects bc divides by zero
    if len(gradebook) == 0:
        print("no grades yet, gpa cannot yet be calculated")
        return 0
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

#interactive main menu with options for user
#old testing calls listed as comments
def main():
    #load grades from csv before show menu
    load_grades()
    #loop
    while True:
        #user choices
        print("GRADEBOOK MAIN MENU")
        print("1. Show all classes and averages")
        print("2. Show all grades for a class")
        print("3. Show GPA")
        print("4. Add a grade")
        print("5. Quit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            print_all_averages()
        elif choice == "2":
            #EXTENSION: shows current subjects
            print("Enter a subject from the following options: ")
            print("[" + ", ".join(gradebook.keys()) + "]")
            
            #ask for class
            #EXTENSION: lower so works for diff cases
            subject = input("Which class? ").lower()

            if subject in gradebook:
                print_grades(subject)
            else:
                print("That class isn't in the gradebook.")
                #show valid classes so user knows what to type (like how ls works in terminal)
                print("Available classes: " + ", ".join(gradebook.keys()))

        elif choice == "3":
            print("Your GPA: " + str(get_GPA()))
        elif choice == "4":
            #EXTENSION: shows list
            print("Enter a subject from the following options or enter a new subject: ")
            print("[" + ", ".join(gradebook.keys()) + "]")
            
            #EXTENSION: now handles all cases
            #use strip to remove spaces and lower for caps as extension

            user_subject = input("Which class? ").strip().lower()
            #EXTENSION: no blank names
            if user_subject == "":
                print("Failed, class name cannot be blank")
            else:
                #must type the num (0-100 or 100+ w/ extra credit)
                user_grade = float(input("What grade? "))
                add_grade(user_subject, user_grade)
                print("Added " + str(user_grade) + " to " + user_subject + ".")
        elif choice == "5":
            #EXTENSION: save the grades on CSV before quitting
            file = open("grades.csv", "w")
            for subject in gradebook:
                line = subject
                for grade in gradebook[subject]:
                    line = line + "," + str(grade)
                file.write(line + "\n")
            file.close()
            print("Grades saved! Bye :)")
            break
        else: 
            print("Try again.")
        print("Returning to main menu...")
        print()


    #OLD TESTING BELOW:
    #test load_grades:
    #load_grades()
    #print(gradebook)
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