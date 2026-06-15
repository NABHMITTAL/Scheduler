from project import *

#print(len(projectList))

def projectSubMenu(projectNumber):
    selectedProject = projectList[projectNumber]
    print(f"\n=={selectedProject.title}==")
    if selectedProject.tasks != []:
        for i in selectedProject.tasks:
            i.display()
    else:
        print("No tasks found")
    while True:
        print("1. Add task")
        print("2. Delete Task")
        print("3. Exit to Main Menu")

        choice = input("Select an option")

        if choice == "1":
            selectedProject.enterTask()
        elif choice == "2":
            selectedProject.deleteTask()
        elif choice =="3":
            break
        else:
            print("Invalid Input")


while True:
    print("\n==Scheduler==")
    print("1. Create Project")
    print("2. Display Projects")
    print("3. Save")
    print("4. Choose Proect to edit")
    print("5: Delete Project")
    print("6. Exit")

    choice = input("Choice: ")
    if choice =="1":
        createProject()

    elif choice =="2":
        for project in projectList:
            project.displayProject()

    elif choice == "3":
        saveChanges()
        print("Changes saved or did it >:)")

    elif choice =="4":
        print("Select your project to edit ")
        serialCounter =1
        for projects in projectList:
            print(f"{serialCounter}. {projects.title}")
            serialCounter+=1
        projectArrayLength = len(projectList)
        try:
            projectChoice = int(input("Select project from menu ")) -1 #-1 to handle indexing
            if projectChoice<projectArrayLength and projectChoice>-1:
                projectSubMenu(projectChoice)
            else:
                print("Invalid input")
        except:
            print("Invaliud Input")

    elif choice == "5":
        deleteProject()

    elif choice == "6":
        break
    else:
        print("MF FUCK OFF")

