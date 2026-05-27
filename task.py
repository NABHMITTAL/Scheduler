import json
tasks = []

def  enterTask():
        
    while True:
        taskIn = input("Enter a Task and Enter Done to finish inputting")
        if taskIn == "Done":
            break
        else:
          tasks.append(taskIn)

def deleteTask():
    item = input("Enter Serial Number to delete")
    del tasks[int(item)-1]

def  showTask():
    with open("taskList.json","r") as file:
        printList = json.load(file)
        for i in range(len(printList)):
            print(i+1, tasks[i])

def saveChanges():
    #ask for permission before replacing
    with open("taskList.json","w") as file:
        json.dump(tasks,file)

