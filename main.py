from pawpal_system import Pet, PetTask, UserPreferences, Scheduler, Planner

# Create a pet
pet = Pet("Buddy")

# Create tasks
task1 = PetTask("Walk", 30, 3, "Exercise")
task2 = PetTask("Feed", 10, 5, "Food")
task3 = PetTask("Play", 20, 2, "Fun")

# Add tasks to pet
pet.addTask(task1)
pet.addTask(task2)
pet.addTask(task3)

# Create user preferences
preferences = UserPreferences(availableTime=40, preferredTime="Morning")

# Create scheduler and planner
scheduler = Scheduler()
planner = Planner(pet, preferences, scheduler)

# Generate plan
plan = planner.createPlan()

# Print schedule
print("Today's Schedule:\n")

for task in plan:
    print(task.getDetails())

# Print explanation
print("\nExplanation:")
print(planner.explainPlan())