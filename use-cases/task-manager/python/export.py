# task_manager/export.py
import csv
from datetime import datetime


class TaskCSVExporter:
    """Transform Task objects into CSV format and export to file."""

    HEADERS = ['ID', 'Title', 'Description', 'Status', 'Priority',
               'Due Date', 'Created', 'Tags', 'Overdue']

    @staticmethod
    def task_to_row(task):
        """Convert Task instance to CSV row dictionary."""
        return {
            'ID': task.id[:8],  # short UUID for readability
            'Title': task.title,
            'Description': task.description,
            'Status': task.status.value,
            'Priority': task.priority.value,
            'Due Date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
            'Created': task.created_at.strftime('%Y-%m-%d %H:%M'),
            'Tags': ', '.join(task.tags) if task.tags else '',
            'Overdue': 'Yes' if task.is_overdue() else 'No'
        }

    @staticmethod
    def export_to_file(tasks, output_path):
        """Write tasks list to CSV file with error handling."""
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=TaskCSVExporter.HEADERS)
                writer.writeheader()
                for task in tasks:
                    writer.writerow(TaskCSVExporter.task_to_row(task))
            return True, f"Successfully exported {len(tasks)} task(s) to {output_path}"
        except Exception as e:
            return False, f"Error exporting tasks: {e}"
