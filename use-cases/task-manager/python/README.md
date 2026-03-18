# Task Manager CLI

A modular Python-based Command Line Interface (CLI) application for managing personal tasks with local JSON persistence.

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
