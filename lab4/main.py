tasks = {}

n = int(input("Enter number of tasks: "))

# input alma
for i in range(n):
    name = input("Enter task name: ")

    print("How many dependencies for", name, "? ", end="")
    dep_count = int(input())

    deps = []
    for j in range(dep_count):
        print("Enter dependency", j + 1, ": ", end="")
        d = input()
        deps.append(d)

    tasks[name] = deps

# TASK STRUCTURE
print("TASK STRUCTURE:")
for task in tasks:
    print(task, "->", tasks[task])

# INITIAL TASKS
print("INITIAL TASKS (no dependencies):")
found = False
for task in tasks:
    if tasks[task] == []:
        print(task)
        found = True

if found == False:
    print("None")

# EXECUTION ORDER
print("EXECUTION ORDER:")

completed = set()
order = []
completed_count = 0

while completed_count < n:
    progress = False

    for task in tasks:
        if task not in completed:

            deps = tasks[task]
            all_done = True

            for dep in deps:
                if dep not in completed:
                    all_done = False
                    break

            if all_done:
                order.append(task)
                completed.add(task)
                completed_count = completed_count + 1
                progress = True

    if progress == False:
        print("No task can be started.")
        print("ERROR: Circular dependency detected!")
        print("These tasks could not be completed:")

        for task in tasks:
            if task not in completed:
                print(task)
        break

# başarılıysa
if completed_count == n:
    step = 1
    for t in order:
        print("Step", step, ":", t)
        step = step + 1

    print("ALL TASKS COMPLETED SUCCESSFULLY")
