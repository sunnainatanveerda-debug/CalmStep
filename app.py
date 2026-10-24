

import streamlit as st
import json
from pathlib import Path
TASKS_FILE = Path(__file__).parent / "tasks.json"
def load_tasks():
    if TASKS_FILE.exists():
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            st.session_state.tasks,
            file,
            indent=4,
            ensure_ascii=False
        )
st.set_page_config(
    page_title="CalmStep",
    page_icon="🌱",
    layout="wide"
)

with st.sidebar:
    st.title("🌱 CalmStep")
    st.caption("One Clear Next Step")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📋 My Tasks",
            "🧩 Break Down a Task",
            "🎯 Focus Mode"
        ]
    )

    st.divider()
    st.caption("One step at a time. You can do this!")



if page == "🏠 Dashboard":
    st.title("🌱 CalmStep")
    st.subheader("One Clear Next Step")
    st.write(
        "Feeling overwhelmed? Start small. "
        "Add your tasks, break big goals into manageable steps, "
        "and focus on one thing at a time."
    )

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

if page == "🏠 Dashboard":
    st.divider()
    st.header("📝 Add a Task")


    with st.form("task_form", clear_on_submit=True):
        task = st.text_input(
            "What do you need to do?",
            placeholder="Example: Complete my SQL assignment"
        )

        importance = st.selectbox(
            "How important is this task?",
            ["High", "Medium", "Low"]
        )

        deadline = st.selectbox(
            "When is it due?",
            ["Today", "Tomorrow", "Within 7 days", "No deadline"]
        )

        duration = st.selectbox(
            "How long might it take?",
            ["15 minutes", "30 minutes", "1 hour", "2 hours or more"]
        )

        add_task = st.form_submit_button("Add Task")

    if add_task:
        clean_task = task.strip()

        if not clean_task:
            st.warning("Please enter a task first.")

        elif any(
            item["task"].casefold() == clean_task.casefold()
            for item in st.session_state.tasks
        ):
            st.warning("This task is already on your list.")

        else:
            st.session_state.tasks.append({
                "task": clean_task,
                "importance": importance,
                "deadline": deadline,
                "duration": duration,
                "completed": False
            })
            save_tasks()
            st.success("Task added successfully!")


if page == "🧩 Break Down a Task":
    st.divider()
    st.header("🧩 Break a Big Task into Small Steps")



    big_task = st.text_input(
        "Enter a big task to break down",
        placeholder="Example: Complete my university project",
        key="big_task_input"
    )

    task_steps = {
        "Prepare my Data Science presentation": [
            "1. Choose your presentation topic",
            "2. Research three important points",
            "3. Create your presentation slides",
            "4. Practice explaining your slides"
        ],
        "Complete my SQL assignment": [
            "1. Read the assignment instructions",
            "2. Identify the SQL questions",
            "3. Write and test your SQL queries",
            "4. Review your answers"
        ],
        "Study for an exam": [
            "1. List the topics you need to study",
            "2. Review one topic at a time",
            "3. Practice questions",
            "4. Review the topics you found difficult"
        ],
        "Apply for an internship": [
            "1. Find a suitable internship",
            "2. Update your resume",
            "3. Prepare a short application message",
            "4. Review and submit your application"
        ]
    }

    st.write("Choose one small step at a time.")

    if big_task.strip():
        if big_task in task_steps:
            steps = task_steps[big_task]
        else:
            steps = [
                f"1. Write down the main goal: {big_task}",
                "2. Identify the first small action",
                "3. Work on that action",
                "4. Review your progress and choose the next action"
            ]

        for step in steps:
            st.checkbox(
                step,
                key=f"breakdown_{big_task}_{step}"
            )
    else:
        st.caption("Enter a task above to see its suggested steps.")


if page == "📋 My Tasks":
    st.divider()
    st.header("📋 Your Tasks")

    priority_score = {"High": 3, "Medium": 2, "Low": 1}
    deadline_score = {
        "Today": 4,
        "Tomorrow": 3,
        "Within 7 days": 2,
        "No deadline": 1
    }

    if st.session_state.tasks:
        tasks = st.session_state.tasks

        completed_count = sum(item["completed"] for item in tasks)
        total_count = len(tasks)

        st.write(f"Completed: {completed_count} of {total_count}")
        st.progress(completed_count / total_count)

        sorted_tasks = sorted(
            enumerate(tasks),
            key=lambda pair: (
                pair[1]["completed"],
                -(
                    priority_score[pair[1]["importance"]]
                    + deadline_score[pair[1]["deadline"]]
                )
            )
        )

        for index, item in sorted_tasks:
            st.checkbox(
                f"{item['task']} — {item['duration']}",
                value=item["completed"],
                key=f"task_{index}",
                on_change=lambda i=index: (
                    st.session_state.tasks[i].update(
                        completed=st.session_state[f"task_{i}"]
                    ),
                    save_tasks()
                )
            )

            st.caption(
                f"Importance: {item['importance']} · "
                f"Due: {item['deadline']}"
            )
    else:
        st.caption("Your task list is empty. Add your first task above.")
    
if page == "🎯 Focus Mode":
    st.divider()
    st.header("🎯 Focus Mode")

    priority_score = {"High": 3, "Medium": 2, "Low": 1}
    deadline_score = {
        "Today": 4,
        "Tomorrow": 3,
        "Within 7 days": 2,
        "No deadline": 1
    }

    unfinished = [
        (index, item)
        for index, item in enumerate(st.session_state.tasks)
        if not item["completed"]
    ]

    unfinished.sort(
        key=lambda pair: (
            priority_score[pair[1]["importance"]]
            + deadline_score[pair[1]["deadline"]]
        ),
        reverse=True
    )

    if unfinished:
        focus_index, focus_task = unfinished[0]

        st.write("Ignore the rest of your list for a moment.")
        st.info(f"Your focus: {focus_task['task']}")
        st.write(f"Estimated time: {focus_task['duration']}")

        st.caption(
            "Take one step at a time. You can return to your list whenever you need."
        )

        if st.button("Mark this task complete"):
            st.session_state.tasks[focus_index]["completed"] = True
            save_tasks()
            st.rerun()
    else:
        st.info("No unfinished tasks right now. Add a task on the Dashboard.")