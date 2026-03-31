from pawpal_system import Pet, PetTask, Scheduler


# ---------------- SORTING TEST ----------------
def test_sort_by_time():
    scheduler = Scheduler()

    t1 = PetTask("Walk", 30, 3, "Exercise", time="10:00")
    t2 = PetTask("Feed", 10, 5, "Food", time="08:00")
    t3 = PetTask("Play", 20, 2, "Fun", time="12:00")

    tasks = [t1, t2, t3]
    sorted_tasks = scheduler.sortByTime(tasks)

    assert [t.time for t in sorted_tasks] == ["08:00", "10:00", "12:00"]


# ---------------- RECURRING TEST ----------------
def test_recurring_daily_task():
    task = PetTask("Feed", 10, 5, "Food", frequency="daily")

    new_task = task.mark_complete()

    assert new_task is not None
    assert new_task.frequency == "daily"
    assert new_task.date > task.date


# ---------------- CONFLICT TEST ----------------
def test_detect_conflicts():
    scheduler = Scheduler()

    t1 = PetTask("Walk", 30, 3, "Exercise", time="10:00")
    t2 = PetTask("Feed", 10, 5, "Food", time="10:00")  # same time
    t3 = PetTask("Play", 20, 2, "Fun", time="12:00")

    tasks = [t1, t2, t3]

    conflicts = scheduler.detectConflicts(tasks)

    assert len(conflicts) == 1
    assert conflicts[0][0].time == "10:00"
    assert conflicts[0][1].time == "10:00"