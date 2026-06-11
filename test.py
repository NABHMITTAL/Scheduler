from project import Task,Project

print("=== Testing Project Display ===")

p = Project("Test")
p1 = Project("Code")

print("\n\n ------Object Formation------")
p.tasks.append(Task("1", "Homework", 2))
p.tasks.append(Task("2", "Study", 1))
p.tasks.append(Task("3","Help",3))

p1.tasks.append(Task("1", "Homework", 2))
p1.tasks.append(Task("2", "Study", 1))
p1.tasks.append(Task("3","Help",3))

print("\n\n ------Project Display------")

p.displayProject()
p1.displayProject()

print("\n\n ------Project to dict------")
data = p.projectToDict()
print(data)

print("\n\n ------Project from dict------")
p2 = Project.projectFromDict(data)
p2.displayProject()
