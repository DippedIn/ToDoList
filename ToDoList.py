'''Functions to read the tasks from the file and write tasks to the file:
Read file contents into a list of dictionaries
Define each line and read and read the first character if "-" that means it's a bullet point, if [] that means it's a checkbox,
and if [x] that means it's a completed checkbox.

After the file is read, print the list of tasks to the console with justification for each column.
Prompt the user to add/remove/mark tasks as completed.
After modifying the list, write the updated list back to the file in the same format.'''


'''functions:
    - load_tasks(filename="tasks.csv")
    - read_tasks(filename="tasks.csv")
#get first character of each line to determine task status:
    - task_status(char)
        - if char == "-": return "bullet"
        - elif char == "[]": return "incomplete"
        - elif char == "[x]": return "completed"
#Modify task list:
    - add_task(task_list, next_id, description, priority)
        - 'id': next_id
    - save_tasks(task_list, filename="tasks.csv")
    - Append to task_list
    - Increment next_id


'''

import csv    

of = open("tasks.csv", "r")
class ToDoList:
    global of
    def ReadTasks(self):
        print(of.read())
        print("\n")
        pass

    def TaskStatus(self):
        # Determine task status based on the first character
        #go thorugh each line in the file and get the first character
        for line in of:
            first_char = line[0]
            if first_char == "-":
                print("bullet point")
            elif first_char == "[":
                if line[1] == "X" or line[1] == "x":
                    print("completed checkbox")
                else:
                    print("incomplete checkbox")
            else:
                print("n")

        pass

    def AddTask(self, task_name, task_list, next_id, description, priority):
        pass

    def RemoveTask(self, task_list, task_id):
        pass#

    def MarkCompleted(self, task_list, task_id):
        pass

    def SaveTasks(self, task_list, filename="tasks.csv"):
        pass

    def EditTask(self, task_list, task_id, new_description=None, new_priority=None):
        pass


if __name__ == "__main__":
    todo = ToDoList()
    todo.ReadTasks()
    todo.TaskStatus()  