from pawpal_system import Pet, PetTask, UserPreferences, Scheduler, Planner

# Create pet
pet = Pet("Buddy")

# Add tasks (INTENTIONALLY include conflict + recurring)
t1 = PetTask("Walk", 30, 3, "Exercise", time="10:00", frequency="daily")
t2 = PetTask("Feed", 10, 5, "Food", time="10:00", frequency="daily")  # SAME TIME → conflict
t3 = PetTask("Play", 20, 2, "Fun", time="12:00")

pet.addTask(t1)
pet.addTask(t2)
pet.addTask(t3)

scheduler = Scheduler()
preferences = UserPreferences(availableTime=40, preferredTime="Morning")

# ---------------- ORIGINAL TASKS ----------------
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

# ---------------- CONFLICT DETECTION ----------------
conflicts = scheduler.detectConflicts(pet.getTasks())

if conflicts:
    print("\n⚠️ Conflicts detected:")
    for a, b in conflicts:
        print(f"- {a.name} and {b.name} are both scheduled at {a.time}")
else:
    print("\nNo conflicts found.")

# ---------------- RECURRING TASK TEST ----------------
print("\nMarking 'Feed' task complete...")
new_task = t2.mark_complete()

if new_task:
    print("New recurring task created:")
    print(new_task.getDetails())

# ---------------- GENERATE PLAN ----------------
planner = Planner(pet, preferences, scheduler)
plan = planner.createPlan()

print("\nGenerated Plan:")
for t in plan:
    print(t.getDetails())

print("\nExplanation:")
print(planner.explainPlan())