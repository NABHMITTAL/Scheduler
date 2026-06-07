import json
class Task():  #task class with constructor , marlDone, display, toDict, fromDict
    def __init__(self,id,title,priority):
        self.title = title
        self.priority = priority
        self.done = False
        self.id = id
    
    def markDone(self):
        self.done = True
    
    def display(self):
        print(f"{self.id}. {self.title} | Priority: {self.priority} | Status: {self.done}")

    def toDict(self):
        return{
            "id": self.id,
             "title": self.title,
            "priority": self.priority,
            "complete": self.done
        }
    
    @classmethod
    def fromDict(cls,data):
        task = cls(
            data["id"],
            data["title"],
            data["priority"],
        )

        task.done = data["complete"]
        return task

def  loadTask(): #for bringing json to python
    loadArray = []
    try:
        with open("taskList.json","r") as file:
            loadedData = json.load(file)
        for data in loadedData:
            loadArray.append(Task.fromDict(data))
        return loadArray
    except:
        return []
    
try:
    taskArray = loadTask()
except:
    taskArray = []   #security case if array is empty

def saveChanges(): #sending tasks in pythton to json will be changed to work with projects
    #ask for permission before replacing
    saveData = []
    for task in projectList:
        saveData.append(task.toDict())

    with open("taskList.json","w") as file:
           json.dump(saveData,file)

def displayTasks(): #for listing tasks test function (never used)
    for task in taskArray:
        task.display()

class Project(): #project class under construction
    def __init__(self,Title):
        self.title = Title
        self.tasks = []

    def  enterTask(self): # for taking input of tasks
        print("input Done in Title to finsh givng the input")
        while True:
            taskId = input("Enter a Task id")
            title = input("Enter a Task Title")
            priority = int(input("Enter a Task Priority"))
            if title == "Done":
                break
            else:
                newTask = Task(taskId,title,priority) 
                self.tasks.append(newTask)

    def deleteTask(self): #deleting task based on id will be changed later
        try:
            item = input("Enter Serial Number in range to delete")
            del self.tasks[int(item)-1]
        except:
            print("Invalid Input bruh")
#i am going crazy

projectList=[]


def createProject():
    print("Enter Project Names when prompte and input Done when finished")
    while True:
        name = input("Enter Project Name")
        if name == "Done":
            break
        else:
            newProject = Project(name)
            projectList.append(newProject)


# t = Task("1", "Test task", 3)
# t.display()                                                        #   test subject

# data = t.toDict()
# t2 = Task.fromDict(data)
# t2.display

# p = Project("Test")
# # p.tasks.append(Task("1", "A", 1))
# # p.tasks.append(Task("2", "B", 2))
# # print(p.title)
# # for t in p.tasks:
# #     t.display()
# p.enterTask()