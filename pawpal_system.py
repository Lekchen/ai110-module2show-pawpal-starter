from dataclasses import dataclass, field
from typing import List


@dataclass
class PetTask:
    name: str
    duration: int
    priority: int
    type: str
    time: str = "09:00"
    completed: bool = False

    def getDetails(self):
        """Return task details as a formatted string."""
        return f"{self.time} - {self.name} ({self.type}) - {self.duration} mins, Priority {self.priority}"


@dataclass
class Pet:
    name: str
    tasks: List[PetTask] = field(default_factory=list)

    def addTask(self, task: PetTask):
        """Add a task to the pet."""
        self.tasks.append(task)

    def removeTask(self, task: PetTask):
        """Remove a task from the pet."""
        if task in self.tasks:
            self.tasks.remove(task)

    def getTasks(self):
        """Return all tasks for the pet."""
        return self.tasks


@dataclass
class UserPreferences:
    availableTime: int
    preferredTime: str


class Scheduler:
    def sortByPriority(self, tasks):
        """Sort tasks by priority (highest first)."""
        return sorted(tasks, key=lambda t: t.priority, reverse=True)

    def sortByTime(self, tasks):
        """Sort tasks by time (HH:MM)."""
        return sorted(tasks, key=lambda t: t.time)

    def filterTasks(self, tasks, completed=None, min_priority=None):
        """Filter tasks by completion status or minimum priority."""
        result = tasks

        if completed is not None:
            result = [t for t in result if t.completed == completed]

        if min_priority is not None:
            result = [t for t in result if t.priority >= min_priority]

        return result

    def generatePlan(self, tasks, preferences):
        """Generate a schedule based on priority and available time."""
        sorted_tasks = self.sortByPriority(tasks)

        selected = []
        total_time = 0

        for task in sorted_tasks:
            if total_time + task.duration <= preferences.availableTime:
                selected.append(task)
                total_time += task.duration

        return selected


class Planner:
    def __init__(self, pet: Pet, preferences: UserPreferences, scheduler: Scheduler):
        self.pet = pet
        self.preferences = preferences
        self.scheduler = scheduler

    def createPlan(self):
        """Create a schedule using the scheduler."""
        return self.scheduler.generatePlan(self.pet.getTasks(), self.preferences)

    def explainPlan(self):
        """Explain why tasks were selected."""
        plan = self.createPlan()

        if not plan:
            return "No tasks could be scheduled within the available time."

        total_time = sum(task.duration for task in plan)
        task_names = [task.name for task in plan]

        return f"Selected {len(plan)} high-priority tasks ({', '.join(task_names)}) that fit within {self.preferences.availableTime} minutes, using {total_time} minutes total."