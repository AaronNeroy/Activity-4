class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        t1 = Task("Buy groceries")
        t2 = Task("Write report")
        t3 = Task("Call dentist")
        t4 = Task("Read book")
        t5 = Task("Clean house")
        t6 = Task("Plan holiday")

        t1.mark_completed()
        t2.mark_completed()
        t3.mark_completed()

        self.tasks = [t1, t2, t3, t4, t5, t6]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    todo_titles = [task.title for task in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in todo_titles:
        print(title)

    done_titles = [task.title for task in pool.get_done_tasks()]
    print("Done Tasks:")
    for title in done_titles:
        print(title)


if __name__ == "__main__":
    main()
