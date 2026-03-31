from dataclasses import dataclass, field
from typing import List

@dataclass
class PetTask:
    name: str
    duration: int
    priority: int
    type: str

    def getDetails(self):
        return f"Task: {self.name}, Type: {self.type}, Duration: {self.duration} minutes, Priority: {self.priority}"

@dataclass
class Pet:
    name: str
    tasks: List[PetTask] = field(default_factory=list)

    def addTask(self, task: PetTask):
        self.tasks.append(task)

    def removeTask(self, task: PetTask):
        if task in self.tasks:
            self.tasks.remove(task)

    def getTasks(self):
        return self.tasks

@dataclass
class UserPreferences:
    availableTime: int
    preferredTime: str

class Scheduler:
    def generatePlan(self, tasks, preferences):
        sorted_tasks = self.sortByPriority(tasks)
        selected = []
        total_time = 0
        for task in sorted_tasks:
            if total_time + task.duration <= preferences.availableTime:
                selected.append(task)
                total_time += task.duration
        return selected

    def sortByPriority(self, tasks):
        return sorted(tasks, key=lambda t: t.priority, reverse=True)

class Planner:
    def __init__(self, pet: Pet, preferences: UserPreferences, scheduler: Scheduler):
        self.pet = pet
        self.preferences = preferences
        self.scheduler = scheduler

    def createPlan(self):
        return self.scheduler.generatePlan(self.pet.getTasks(), self.preferences)

    def explainPlan(self):
        plan = self.createPlan()
        if not plan:
            return "No tasks could be scheduled within the available time."
        total_time = sum(task.duration for task in plan)
        task_names = [task.name for task in plan]
        return f"Selected {len(plan)} high-priority tasks ({', '.join(task_names)}) that fit within {self.preferences.availableTime} minutes, using {total_time} minutes total."