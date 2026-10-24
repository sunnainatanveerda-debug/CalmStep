# 🌱 CalmStep — One Clear Next Step

**Created by:** Sunnaina Tanveer

## About the Project

CalmStep is a student-focused productivity app designed to help people who feel overwhelmed by long to-do lists. It encourages users to take manageable actions, break large tasks into smaller steps, and focus on one unfinished task at a time.

## The Problem

Students often have assignments, exams, projects, and internship applications to manage. A long task list can feel overwhelming and make it difficult to decide what to do first.

## The Solution

CalmStep provides a simple, supportive workspace that helps students organize their work and choose their next step.

## Features

- **Dashboard:** Add tasks with importance, deadline, and estimated duration.
- **My Tasks:** View tasks and track completion progress.
- **Break Down a Task:** Turn a large goal into smaller, manageable steps.
- **Focus Mode:** Highlight a high-priority unfinished task.
- **Task Persistence:** Save tasks locally in `tasks.json`.
- **Progress Tracking:** See how many tasks are completed.

## Technology Stack

- Python
- Streamlit
- JSON for local task storage

## How to Run CalmStep

### Requirements

- Python 3.12 or compatible Python version
- pip

### Installation

1. Download or clone the project.
2. Open Command Prompt in the project folder.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the environment on Windows:

   ```bat
   .venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```

7. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Project Goal

CalmStep aims to make everyday planning feel more manageable by encouraging students to take one clear next step rather than trying to do everything at once.

## Limitations

- Tasks are stored locally in a JSON file.
- The task breakdown feature uses predefined suggestions and a general fallback; it is not an AI-powered planner.
- The app does not currently provide user accounts or cloud synchronization.

## Author

**Sunnaina Tanveer**

Built as a student productivity prototype for a hackathon.
