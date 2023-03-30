import unittest
from Employee import Employee

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.project = Employee('zhu','fengyuan',50000)

    def test_something(self):
        self.project.give_raise(50000)
        self.assertEqual(self.project.salary,100000)  # add assertion here


if __name__ == '__main__':
    unittest.main()
