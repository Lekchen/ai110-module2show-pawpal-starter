import streamlit as st
from pawpal_system import Pet, PetTask, UserPreferences, Scheduler, Planner


if "pet" not in st.session_state:
    st.session_state.pet = Pet("Buddy")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "preferences" not in st.session_state:
    st.session_state.preferences = UserPreferences(availableTime=60, preferredTime="Any")

if "tasks" not in st.session_state:
    st.session_state.tasks = []


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    "Plan your pet's daily tasks based on priority and available time."
)

st.subheader("Pet Info")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])


st.markdown("### Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)

with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)


if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority
        }
    )


if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    pet = st.session_state.pet
    scheduler = st.session_state.scheduler
    preferences = st.session_state.preferences

    # Clear old tasks
    pet.tasks.clear()

    # Convert UI tasks into PetTask objects
    for t in st.session_state.tasks:
        if t["priority"] == "high":
            p = 3
        elif t["priority"] == "medium":
            p = 2
        else:
            p = 1

        task = PetTask(
            name=t["title"],
            duration=t["duration_minutes"],
            priority=p,
            type="General",
            time="09:00"  # you can improve this later with input
        )
        pet.addTask(task)

    # ---------------- CONFLICT DETECTION ----------------
    conflicts = scheduler.detectConflicts(pet.getTasks())

    if conflicts:
        st.warning("⚠️ Task conflicts detected!")
        for a, b in conflicts:
            st.write(f"- {a.name} and {b.name} are both scheduled at {a.time}")

    # ---------------- SORT TASKS ----------------
    sorted_tasks = scheduler.sortByTime(pet.getTasks())

    st.subheader("Sorted Tasks")
    st.table([{
        "Task": t.name,
        "Time": t.time,
        "Priority": t.priority
    } for t in sorted_tasks])

    # ---------------- GENERATE PLAN ----------------
    planner = Planner(pet, preferences, scheduler)
    plan = planner.createPlan()

    if plan:
        st.success("Today's Schedule:")
        st.table([{
            "Task": t.name,
            "Time": t.time,
            "Duration": t.duration,
            "Priority": t.priority
        } for t in plan])

        st.markdown("### Explanation")
        st.info(planner.explainPlan())
    else:
        st.warning("No tasks could fit within the available time.")