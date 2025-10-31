'''
To-Do List Application - Function Stubs

This file contains function stubs for the to-do list application.
Teams should agree on these function signatures before beginning implementation.

Each team member can then implement their assigned functions independently,
knowing that the functions will work together when merged.

Instructions:
1. Review all function stubs with your team
2. Modify signatures if needed (but discuss first!)
3. Create a branch for each function you implement
4. Replace 'pass' with your implementation
5. Test your function independently
6. Merge to main when complete
'''


def load_tasks(filename="tasks.csv"):
    '''
    Load tasks from a CSV file.

    Parameters:
        filename (str): Path to the CSV file (default: 'tasks.csv')

    Returns:
        tuple: (task_list, next_id)
            task_list (list): List of task dictionaries
            next_id (int): Next available ID number

    Behaviour:
        - If file doesn't exist, return empty list and ID 1
        - Read CSV and convert to list of dictionaries
        - Determine next_id from maximum existing ID + 1
        - Convert 'completed' string to boolean
    '''
    pass


def save_tasks(task_list, filename="tasks.csv"):
    '''
    Save tasks to a CSV file.

    Parameters:
        task_list (list): List of task dictionaries
        filename (str): Path to save location (default: 'tasks.csv')

    Returns:
        bool: True if successful, False if error occurred

    Behaviour:
        - Create/overwrite CSV file with header row
        - Write each task as a row
        - Return success status
    '''
    pass


def add_task(task_list, next_id, description, priority):
    '''
    Add a new task to the task list.

    Parameters:
        task_list (list): The current list of tasks
        next_id (int): The ID to assign to the new task
        description (str): The task description
        priority (str): Priority level ('high', 'medium', or 'low')

    Returns:
        tuple: (updated_task_list, next_id)
            updated_task_list (list): Task list with new task added
            next_id (int): Incremented ID for next task

    Behaviour:
        - Create task dictionary with current date
        - Append to task_list
        - Increment next_id
        - Return updated values
    '''
    pass


def view_tasks(task_list, show_completed=True):
    '''
    Display tasks in a formatted list.

    Parameters:
        task_list (list): List of tasks to display
        show_completed (bool): If False, hide completed tasks (default: True)

    Returns:
        None

    Behaviour:
        - Filter tasks based on show_completed parameter
        - Print formatted task information
        - Show completion statistics
        - Handle empty list case
    '''
    pass


def mark_complete(task_list, task_id):
    '''
    Toggle the completion status of a task.

    Parameters:
        task_list (list): The current list of tasks
        task_id (int): ID of the task to mark

    Returns:
        bool: True if successful, False if task ID not found

    Behaviour:
        - Search for task with matching ID
        - Toggle the 'completed' boolean
        - Return success/failure status
    '''
    pass


def delete_task(task_list, task_id):
    '''
    Remove a task from the list.

    Parameters:
        task_list (list): The current list of tasks
        task_id (int): ID of the task to delete

    Returns:
        bool: True if successful, False if task ID not found

    Behaviour:
        - Search for task with matching ID
        - Remove task from list
        - Return success/failure status
        - Note: Does not reassign IDs (gaps are OK)
    '''
    pass


def display_menu():
    '''
    Display the main menu options.

    Parameters:
        None

    Returns:
        None

    Behaviour:
        - Print formatted menu with numbered options
    '''
    pass


def get_valid_priority():
    '''
    Prompt user for priority level with validation.

    Parameters:
        None

    Returns:
        str: Valid priority ('high', 'medium', or 'low')

    Behaviour:
        - Prompt user for input
        - Validate against allowed values
        - Re-prompt until valid input received
        - Convert to lowercase for consistency
    '''
    pass


def get_valid_id(task_list):
    '''
    Prompt user for task ID with validation.

    Parameters:
        task_list (list): Current tasks (to validate ID exists)

    Returns:
        int: Valid task ID, or None if user cancels

    Behaviour:
        - Prompt for integer input
        - Check ID exists in task_list
        - Re-prompt if invalid
        - Allow cancellation (return None)
    '''
    pass


def main():
    '''
    Main program loop.

    Parameters:
        None

    Returns:
        None

    Behaviour:
        - Initialise program state
        - Run main menu loop
        - Handle user choices
        - Manage program exit
    '''
    pass


if __name__ == "__main__":
    main()