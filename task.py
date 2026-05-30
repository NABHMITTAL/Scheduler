import json
class Task():
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

def  loadTask():
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
    taskArray = []

def  enterTask():
    print("input Done in Title to finsh givng the input")
    while True:
        taskId = input("Enter a Task id")
        title = input("Enter a Task Title")
        priority = int(input("Enter a Task Priority"))
        if title == "Done":
            break
        else:
            newTask = Task(taskId,title,priority) 
            taskArray.append(newTask)

def deleteTask():
    try:
        item = input("Enter Serial Number in range to delete")
        del taskArray[int(item)-1]
    except:
        print("Invalid Input bruh")

def saveChanges():
    #ask for permission before replacing
    saveData = []
    for task in taskArray:
        saveData.append(task.toDict())

    with open("taskList.json","w") as file:
           json.dump(saveData,file)

def displayTasks():
    for task in taskArray:
        task.display()