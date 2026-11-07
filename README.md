# Gradebook (ORIGINAL)

## 1. What is the general purpose of your program?
This program lets a user store their grades for each class, view their grades and averages, and calculate their overall GPA (4.0 scale). Users can get a quick summary of how they're doing in school.

## 2. Who are 2 possible expected users of your program? How does your program target them?
Students can add grades as they get them back, see which class is their best and worst, and check their GPA. Parents can check in on how their child is doing in each class. With the best/worst class feature, they can quickly see which classes their kids may need extra help on. For students and parents, the numbered menu makes it easy to check their information without having to understand code.

## 3. Consider all features of your program. Name one non-negotiable of your project and one feature that is nice-to-have. Why do you feel this is the case?
I think adding grades is a non-negotiable. A gradebook has to be able to take in new grades or else it can only show the same starting data forever. It is a feature that makes program more realistically usable. Every other feature (averages, GPA, best/worst subject) relies on the grades being up to date if this were to actually be used by teachers or students. 

Showing the best and worst subjects is a nice-to-have feature because it shows the users quickly where they're doing well and where they may need help. However, you could also just check that on your own by looking at the averages for each class.

## 4. What are two improvements or additional features that could be included in future iterations of your project? What value would they add?
One possible improvement is saving the grades to a CSV data file. Right now, when the program closes, all the grades are lost and the everything resets. Saving them to a CSV file would let users keep their gradebook. A CSV file can also be used to make charts and to let administrators or dpeartment heads analyze the grades and make course improvements.

Another possible improvement would be the ability to support for multiple students. Right now, the program only tracks one person's grades. Letting a teacher create a gradebook for each student in the class lets them enter grades for everyone and compare class averages. This would make the program a tool for teachers alongside parents and students. Teachers can even use this to calculate things like curves for tests. This feature would come along with saving the grades to a CSV file.

# EXTENSION

## 1. Identify the type of data we are working with. Identify at least two categories the data could fit into and why.

The data we are working with is the grades for school subjects, where each subject has a list of number grades.
The data is structured data because it is organized in a set format. Each line of the csv file is a subject follow by the grades (separated by commas). Since it follows the same pattern, it can easily be read by the program in gradebook.py and can be read into a dictionary.

The data is also quantitative data because the grades are numbers and we can perform mathematical equations on them such as finding averages and GPA. However, the subject names are qualitative and categorical since they are more like labels, not numbers.


## 2. How do we handle our data in terms of the 5 C’s?
### a. Collect:
I typed my sample grades set into grades.csv. User can also collect new data in the program by adding grades (option 4)

### b. Cache:
The data is stored in the grades.csv file so it is saved between runs. While it runs, it's kept in the gradebook dictionary. But when the user decides to quit the program, the dictionary is written back to grades.csv

### c. Clean:
load_grades() converts the grades from strings to floats so we can do math to find vals such as average and GPA. Subject input uses .lower() and .strip() to standardize inputs and ignore extra spacing or differnt casing. The program checks if subjects/grades exist before removing and deletes subjects that don't have any grades left (after removing) so that there won't be any issues when divided by zero.

### d. Conclude:
The program calculates the average for each subjects, finds best and worst subjects, and converts averages to GPAs to get an overall GPA

### e. Convey:
The results are shown to the user through options on the main menu. It can print average for each subject, best/worst subjects, and overall GPA (stated above). It also can print each subject's grades and averages but conveying it through a chart/visual representation with Xs and *s. Visualizing the grades (option 6) shows grades where X = 50% and each * = 5%.

## 3. What other questions can we ask about the data we’ve collected and analyzed? What is left to be desired?

### a. Other questions:
Are my grades going up or down over time? (pattern)
What grade do I need on the next assignment to achieve a user-set goal?
Which are my best tests and worst tests (which assignments are pulling my average down)?

### b. What's left to be desired:
There are no dates or assignment names so we cannot identify assignments, we just have the grades.
All grades count the same. In real classes quizzes are less weight than tests for example.
Some classes count more for GPA like AP, Honors classes
The visual representation (visualize_grades) loses data by rounding down to the nearest 5%.
Only tracks one student