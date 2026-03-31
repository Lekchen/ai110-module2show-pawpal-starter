from pawpal_system import Pet, PetTask

def test_add_task():
    pet = Pet("Buddy")

    task = PetTask("Walk", 30, 3, "Exercise")
    pet.addTask(task)

    assert len(pet.getTasks()) == 1


def test_remove_task():
    pet = Pet("Buddy")

    task = PetTask("Feed", 10, 5, "Food")
    pet.addTask(task)
    pet.removeTask(task)

    assert len(pet.getTasks()) == 0