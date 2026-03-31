# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial UML design focused on organizing the system into clear, separate classes so that each component had a specific responsibility.

I included the following classes:

PetTask
This class represents a single pet care task such as feeding, walking, or grooming.
It stores attributes like task name, duration, priority, and type. It also provides a method to return task details.
Pet
This class represents the pet and maintains a list of tasks associated with it.
It is responsible for adding, removing, and retrieving tasks.
UserPreferences
This class stores user constraints such as available time and preferred time of day.
It helps guide how the schedule is generated.
Scheduler
This class contains the core scheduling logic.
It is responsible for sorting tasks by priority and generating a daily plan based on time constraints.
Planner
This class acts as the main controller of the system.
It connects the pet, user preferences, and scheduler, and is responsible for creating the final plan and explaining it to the user.

This design follows object-oriented principles such as separation of concerns and modularity, making the system easier to maintain and extend.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
After reviewing my class skeleton, I made a few small refinements to improve the design.

One improvement was clarifying how the Scheduler interacts with PetTask objects. I ensured that tasks are clearly passed as a list and used consistently between the Pet, Scheduler, and Planner classes.

I also reviewed method structure and naming to keep the design clean and beginner-friendly, making it easier to implement later.

I decided not to add additional classes or complexity at this stage in order to keep the system simple and focused on the core functionality.

These changes helped make the design more organized, readable, and easier to extend in the next steps.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The scheduler considers two main constraints: available time and task priority. Each task has a duration and a priority level, and the scheduler selects tasks in order of highest priority while ensuring the total duration does not exceed the available time.

I decided that priority should matter most because some tasks, such as feeding or medication, are more important than others. Time is also critical because the user may not be able to complete all tasks in one day.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff the scheduler makes is prioritizing high-priority tasks over fitting more tasks into the schedule. This means some lower-priority tasks may be skipped even if there is still time available.

This tradeoff is reasonable because, in real life, important tasks like feeding or health-related activities should always come first, even if it means leaving out less important tasks.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used AI tools to help with designing the system, generating class skeletons, debugging errors, and refining my implementation. AI was especially helpful in converting UML designs into Python code and fixing issues with Git, pytest, and Streamlit.

The most helpful prompts were specific instructions such as asking for step-by-step guidance, requesting code corrections, and asking for explanations of errors.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
One situation where I did not fully accept AI suggestions was when it recommended adding extra classes like Owner or Plan. I chose not to include these because they were not required and would make the system more complex.

I verified the correctness of my decisions by testing the code, running the application, and ensuring that it met the assignment requirements without unnecessary complexity.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested adding tasks to a pet and removing tasks from a pet. These tests ensured that the basic task management functionality worked correctly.

These tests were important because the scheduler depends on having the correct list of tasks. If tasks are not added or removed properly, the scheduling logic would not work as expected.
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am confident that my scheduler works correctly for basic scenarios, such as selecting tasks based on priority and available time.

If I had more time, I would test edge cases such as having no tasks, having tasks that exceed available time, and handling tasks with the same priority.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The part I am most satisfied with is successfully connecting the backend logic with the Streamlit user interface. It was rewarding to see the system generate a schedule and explanation based on user input.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduler by adding support for recurring tasks and better time management. I would also enhance the user interface to allow editing and deleting tasks more easily.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned is how breaking a system into smaller components makes it easier to design and implement. I also learned how to effectively use AI as a tool while still making my own decisions about what is appropriate for the project.