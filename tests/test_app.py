import unittest

from app import add_task, complete_task, list_tasks, tasks


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        task = add_task("Learn Git")
        self.assertEqual(task["title"], "Learn Git")
        self.assertFalse(task["completed"])

    def test_reject_empty_task(self):
        with self.assertRaises(ValueError):
            add_task("   ")

    def test_list_tasks(self):
        add_task("Create GitHub repository")
        self.assertEqual(len(list_tasks()), 1)

    def test_complete_task(self):
        add_task("Create a branch")
        task = complete_task(0)
        self.assertTrue(task["completed"])

    def test_complete_invalid_task(self):
        with self.assertRaises(IndexError):
            complete_task(0)


if __name__ == "__main__":
    unittest.main()
