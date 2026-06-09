from task import Task,Project

print("=== Testing Project Display ===")

p = Project("Test")

print("\n\n ------Object Formation works------")
p.tasks.append(Task("1", "Homework", 2))
p.tasks.append(Task("2", "Study", 1))
p.tasks.append(Task("3","Help",3))

print("\n\n ------Project Display------")

p.displayProject()

print("\n\n ------Project to dict------")
data = p.projectToDict()
print(data)

print("\n\n ------Project from dict------")
p2 = Project.projectFromDict(data)
p2.displayProject()
