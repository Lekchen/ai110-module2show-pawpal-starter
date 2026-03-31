from dataclasses import dataclass, field
from typing import List

@dataclass
class PetTask:
    name: str
    duration: int
    priority: int
    type: str

    def getDetails(self):
        pass

@dataclass
class Pet:
    name: str
    tasks: List[PetTask] = field(default_factory=list)

    def addTask(self, task: PetTask):
        pass

    def removeTask(self, task: PetTask):
        pass

    def getTasks(self):
        pass

@dataclass
class UserPreferences:
    availableTime: int
    preferredTime: str

class Scheduler:
    def generatePlan(self, tasks, preferences):
        pass

    def sortByPriority(self, tasks):
        pass

class Planner:
    def __init__(self, pet: Pet, preferences: UserPreferences, scheduler: Scheduler):
        self.pet = pet
        self.preferences = preferences
        self.scheduler = scheduler

    def createPlan(self):
        pass

    def explainPlan(self):
        pass