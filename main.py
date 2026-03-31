from pawpal_system import Pet, PetTask, UserPreferences, Scheduler, Planner

# Create pet
pet = Pet("Buddy")

# Add tasks (OUT OF ORDER)
t1 = PetTask("Walk", 30, 3, "Exercise", time="10:00")
t2 = PetTask("Feed", 10, 5, "Food", time="08:00")
t3 = PetTask("Play", 20, 2, "Fun", time="12:00")

pet.addTask(t1)
pet.addTask(t2)
pet.addTask(t3)

scheduler = Scheduler()
preferences = UserPreferences(availableTime=40, preferredTime="Morning")

print("Original Tasks:")
for t in pet.getTasks():
    print(t.getDetails())

# ---------------- SORT BY TIME ----------------
sorted_tasks = scheduler.sortByTime(pet.getTasks())

print("\nSorted by Time:")
for t in sorted_tasks:
    print(t.getDetails())

# ---------------- FILTER ----------------
filtered_tasks = scheduler.filterTasks(pet.getTasks(), min_priority=3)

print("\nFiltered Tasks (priority >= 3):")
for t in filtered_tasks:
    print(t.getDetails())

# ---------------- GENERATE PLAN ----------------
planner = Planner(pet, preferences, scheduler)
plan = planner.createPlan()

print("\nGenerated Plan:")
for t in plan:
    print(t.getDetails())

print("\nExplanation:")
print(planner.explainPlan())