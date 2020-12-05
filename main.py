# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


name = "Tugay Kerimoğlu"
lectures = ["Signals & Systems: 0", "Linear Algebra: 1", "AI: 2", "Network: 3", "Circuits and Electronics: 4"]
mycourses = []


def lectureschoose():
    global mycourses
    global lectures

    while True:
        print(lectures)
        index = int(input("Please enter your course code: "))
        mycourses.append(lectures[index])
        print("Your Courses: ")
        print(mycourses)

        isenough = input("Do you want to add another course?(Y/N)")
        if isenough == "Y":
            continue
        elif isenough == "N":
            if len(mycourses)<3:
                print("You failed in class")
            break


for i in range(3):
    if name == input("Enter your name and surname: "):
        print("Welcome!")

        lectureschoose()
        break
    elif i == 2:
        print("Please try again later")
        break
    else:
        print("Try Again")


exam = mycourses[int(input("Choose one course to take an exam by course index: "))]




grades= {"Midterm": int(input("Enter your Midterm mark: ")), "Final": int(input("Enter your Final mark: ")), "Project": int(input("Enter your Project mark: "))}

mid = (grades["Midterm"]/100)*30
fin=(grades["Final"]/100)*50
pro=(grades["Midterm"]/100)*20

finalscore = mid+fin+pro

if finalscore < 30:
    print("You Failed!!! FF")
elif finalscore < 50:
    print("DD")
elif finalscore <70:
    print("CC")
elif finalscore <90:
    print("BB")
else:
    print("AA")
