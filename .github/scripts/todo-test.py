import unittest
from io import StringIO
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Test task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        open_titles = [t.title for t in open_tasks]
        self.assertIn("Read book", open_titles)
        self.assertIn("Clean house", open_titles)
        self.assertIn("Plan holiday", open_titles)

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        done_titles = [t.title for t in done_tasks]
        self.assertIn("Buy groceries", done_titles)
        self.assertIn("Write report", done_titles)
        self.assertIn("Call dentist", done_titles)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTaskPool)

    captured = StringIO()
    runner = unittest.TextTestRunner(stream=captured, verbosity=2)
    runner.run(suite)

    lines = captured.getvalue().splitlines()
    for line in lines:
        if " ... ok" in line:
            test_name = line.split(" ... ")[0].strip()
            print(f"{test_name} ... ok")
