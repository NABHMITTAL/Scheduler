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
        print("3. Mark Complete")
        print("4. Rename Task")
        print("5. Exit to Main Menu")

        choice = input("Select an option")

        if choice == "1":
            selectedProject.enterTask()
            saveChanges()
            if selectedProject.tasks != []:
                for i in selectedProject.tasks:
                    i.display()
        
        elif choice == "2":
            selectedProject.deleteTask()
            saveChanges()
            if selectedProject.tasks != []:
                for i in selectedProject.tasks:
                    i.display()
            else:
                print("No tasks found")

        
        elif choice == "3":
            if selectedProject.tasks != []:
                for i in selectedProject.tasks:
                    i.display()
                
                print("\n Select Task to mark Complete: ")
                taskChoice = int(input())
                try:
                    if taskChoice>0 and taskChoice<=len(selectedProject.tasks):
                        selectedTask = selectedProject.tasks[taskChoice-1]
                        selectedTask.markDone()
                        saveChanges()
                except:
                    print("Invalid Input")
            else:
                print("No tasks found")

        elif choice == "4":
            taskChoice = int(input())
            if taskChoice>0 and taskChoice<=len(selectedProject.tasks):
                selectedTask = selectedProject.tasks[taskChoice-1]
                selectedTask.rename()
                saveChanges()
                for i in selectedProject.tasks:
                    i.display()

        elif choice =="5":
            break
        else:
            print("Invalid Input")


while True:
    print("\n==Scheduler==")
    print("1. Create Project")
    print("2. Display Projects")
    print("3. Save")
    print("4. Choose Proect to edit")
    print("5. Delete Project")
    print("6. Rename Project")
    print("7. Exit")

    choice = input("Choice: ")
    if choice =="1":
        createProject()
        saveChanges()
        for project in projectList:
            project.displayProject()

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
                saveChanges()
                for project in projectList:
                    project.displayProject()
            else:
                print("Invalid input")
        except:
            print("Invaliud Input")

    elif choice == "5":
        deleteProject()
        saveChanges()
        for project in projectList:
            project.displayProject()

    elif choice == "6":
        projectChoice = int(input())
        if projectChoice>0 and projectChoice<=len(projectList):
            selectedProject = projectList[projectChoice-1]
            selectedProject.rename()
            saveChanges()
            for project in projectList:
                project.displayProject()
        else:
            print("Invalid Input")

    elif choice == "7":
        break
    else:
        print("Invalid Input")

