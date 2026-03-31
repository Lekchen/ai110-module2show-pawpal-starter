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
The current scheduling logic in main.py is simple and focuses on selecting tasks based on priority and available time. It sorts tasks by priority and adds them to the schedule until the time limit is reached.

However, this approach is somewhat basic. It does not consider the order of tasks during the day, does not handle recurring tasks, and does not check for conflicts between tasks. It also does not filter tasks based on status or type.

To improve the system, I would add features such as sorting tasks by time, supporting recurring tasks, filtering tasks by type or status, and implementing basic conflict detection. These improvements would make the scheduler more realistic and useful for pet owners.

I decided that priority should matter most because some tasks, such as feeding or medication, are more important than others. Time is also critical because the user may not be able to complete all tasks in one day.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff my scheduler makes is that it only checks for exact time conflicts rather than overlapping durations. For example, if one task starts at 10:00 and another starts at 10:15, the system does not detect this as a conflict even if the first task has not finished.

This approach keeps the implementation simple and easy to understand, but it is less accurate for real-world scheduling where tasks can overlap based on duration.

I chose this tradeoff because it reduces complexity and ensures the system remains beginner-friendly, while still demonstrating the concept of conflict detection.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used AI tools such as VS Code Copilot and ChatGPT to assist with designing, implementing, and debugging my scheduler system. Copilot was especially helpful for generating class structures, method suggestions, and completing repetitive code patterns. ChatGPT was useful for explaining concepts step-by-step, debugging errors, and helping integrate different parts of the system such as the UI and backend.

The most helpful prompts were specific questions like “How do I implement sorting by time?” or “How can I detect task conflicts?” because they provided focused and practical solutions.

**b. Judgment and verification**

One example where I modified an AI suggestion was when adding complexity to the scheduler design. Some suggestions included adding extra classes or overly complex logic. I chose to simplify the implementation to keep the system beginner-friendly and aligned with the assignment requirements.

I verified AI suggestions by testing the code using simple examples, running the program, and checking if the output matched expected behavior. I also made sure the design stayed consistent with my UML and project goals.

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

## 6. Reflection on AI Strategy

Working with AI tools taught me that I am responsible for making design decisions, while AI acts as a helper. I learned to guide AI with clear prompts and to critically evaluate its suggestions instead of blindly accepting them.

Being the "lead architect" means balancing simplicity, functionality, and clarity. AI can generate solutions quickly, but it is important to choose approaches that are understandable and maintainable. This project helped me understand how to effectively collaborate with AI while staying in control of the system design.