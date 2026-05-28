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

try:
    with open("taskList.json","r") as file:
        tasks = json.load(file)
except:
    task = []

def  enterTask():
    while True:
        taskIn = input("Enter a Task and Enter Done to finish inputting")
        if taskIn == "Done":
            break
        else:
          tasks.append(taskIn)

def deleteTask():
    try:
        item = input("Enter Serial Number in range to delete")
        del tasks[int(item)-1]
    except:
        print("Invalid Input bruh")

def  showTask():
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

def saveChanges():
    #ask for permission before replacing
    with open("taskList.json","w") as file:
        json.dump(tasks,file)

