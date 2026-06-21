import json
class Task():  #task class with constructor , marlDone, display, toDict, fromDict
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.done = False
    
    def markDone(self):
        self.done = True
    
    def display(self):
        if self.done == True:
            print(f"\t [ X ] {self.title} | Priority: {self.priority}\n")
        else:
            print(f"\t [    ] {self.title} | Priority: {self.priority}\n")

    def rename(self):
        renameInput = input("Enter New Name")
        self.title = renameInput

    def toDict(self):
        return{
             "title": self.title,
            "priority": self.priority,
            "complete": self.done
        }
    
    @classmethod
    def fromDict(cls,data):
        task = cls(
            data["title"],
            data["priority"],
        )

        task.done = data["complete"]
        return task

def  loadProject(): #for bringing json to python
    print("Loading...")
    loadArray = []
    try:
        with open("projectList.json","r") as file:
            loadedData = json.load(file)
        for data in loadedData:
            loadArray.append(Project.projectFromDict(data))
        return loadArray
    except Exception as e:
        print("LOAD ERROR:", e)
        return []

projectList=[]


# def displayTasks(): #for listing tasks test function (old too lazy to delete)
#     for task in taskArray:
#         task.display()

class Project(): #project class under construction
    def __init__(self,Title):
        self.title = Title
        self.tasks = []

    def  enterTask(self): # for taking input of tasks
        try:
            print("input Done in Title to finsh givng the input")
            while True:
                title = input("Enter a Task Title: ")
                if title == "":
                    print("Invalid Input")
                    continue
                elif title == "Done":
                    break
                else:
                    priority = int(input("Enter a Task Priority: "))
                    if priority<=10 and priority>=1:
                        newTask = Task(title,priority) 
                        self.tasks.append(newTask)
                    else:
                        print("Invalid Input")
        except:
            print("Invalid input")

    def deleteTask(self): #deleting task based on id will be changed later
        try:
            item = int(input("Enter Serial Number in range to delete "))
            if item-1>-1 and item-1<len(self.tasks):
                del self.tasks[int(item)-1]
            else:
                print("Invalid Input")
        except:
            print("Invalid Input bruh")

    def rename(self):
        renameInput = input("Enter New Name")
        self.title = renameInput

#i am going crazy
    def displayProject(self):
        print(f"\n Project: {self.title}\n")
        for i in self.tasks:
            i.display()

    def projectToDict(self):
        dictator = [] #array to store the shit to send to dictionary
        for i in self.tasks:
            dictator.append(i.toDict())
        return{
            "projectTitle": self.title,
            "tasks":dictator            
        }

    @classmethod
    def projectFromDict(cls,data):
        loadedTaskArray = []
        try:
            project = cls(data["projectTitle"],)

            for stuff in data["tasks"]:
                loadedTaskArray.append(Task.fromDict(stuff))
            project.tasks = loadedTaskArray
            return project
        except Exception as e:
            print(e)

def createProject():
    print("Enter Project Names when prompte and input Done when finished ")
    while True:
        name = input("Enter Project Name ")
        if name == "":
            print("Invalid Input")
        elif name == "Done":
            break
        else:
            newProject = Project(name)
            projectList.append(newProject)

def saveChanges(): #sending tasks in pythton to json will be changed to work with projects
    #ask for permission before replacing
    saveData = []
    for project in projectList:
        saveData.append(project.projectToDict())
    with open("projectList.json","w") as file:
           json.dump(saveData,file,indent=4)

def deleteProject(): 
    try:
        item = int(input("Enter Serial Number in range to delete "))
        if item-1>-1 and item-1<len(projectList):
            del projectList[int(item)-1]
        else:
            print("Invalid Input")
    except:
        print("Invalid Input bruh")


try:
    projectList = loadProject()
except:
    projectList = []   #security case if array is empty