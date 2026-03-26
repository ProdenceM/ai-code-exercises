# Task Manager CLI

A modular Python-based Command Line Interface (CLI) application for managing personal tasks with local JSON persistence.

**New to this project?** Start with [LEARNING_GUIDE.md](../LEARNING_GUIDE.md) to understand how to use this as a learning tool.

---

## 📚 Learning Resources

This project is designed to teach junior developers how to navigate and implement features in unfamiliar codebases. Start here:

1. **[LEARNING_GUIDE.md](../LEARNING_GUIDE.md)** → How to use this project as a learning tool (4-phase learning path)
2. **[LEARNING_JOURNEY.md](../LEARNING_JOURNEY.md)** → One junior dev's transformation story (what changed, insights gained)
3. **[ONBOARDING_GUIDE.md](../ONBOARDING_GUIDE.md)** → 7 strategies for approaching unfamiliar code (reusable for any project)

**Estimated time to proficiency:** 8-10 hours following the learning path

---

## Project Architecture
The project follows a **layered architecture** to ensure a separation of concerns:

* **Model Layer (`models.py`)**: Defines the core `Task` entity, including priorities, statuses, and business rules like overdue logic.
* **Persistence Layer (`storage.py`)**: Handles data serialization and deserialization using custom JSON encoders to support Python `datetime` objects.
* **Service Layer (`app.py`)**: The `TaskManager` class acts as an orchestrator, handling functional logic, date validation, and statistics calculation.
* **Presentation Layer (`cli.py`)**: Built with `argparse`, this layer manages user input and provides a formatted visual output of task data.


## Getting Started

### Prerequisites
* Python 3.x
* No external dependencies required (uses Standard Library only).
