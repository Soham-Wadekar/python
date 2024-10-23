import unittest
from unittest.mock import patch
from employees import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("SetUpClass")

    @classmethod
    def tearDownClass(cls):
        print("\nTearDownClass")

    def setUp(self):
        '''
        Creation of variables, files, directories. This blocks runs at the start
        '''
        print("\nSetUp")
        self.emp1 = Employee("John", "Doe", 50000)
        self.emp2 = Employee("Jane", "Doe", 40000)
        

    def tearDown(self):
        '''
        Deletion of variables, files, directories. This block runs at the end
        '''
        print("TearDown")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email, 'John.Doe@company.com')
        self.assertEqual(self.emp2.email, 'Jane.Doe@company.com')

        self.emp1.first = "Jack"
        self.emp2.first = "Joan"

        self.assertEqual(self.emp1.email, 'Jack.Doe@company.com')
        self.assertEqual(self.emp2.email, 'Joan.Doe@company.com')

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp1.fullname, 'John Doe')
        self.assertEqual(self.emp2.fullname, 'Jane Doe')

        self.emp1.first = "Jack"
        self.emp2.first = "Joan"

        self.assertEqual(self.emp1.fullname, 'Jack Doe')
        self.assertEqual(self.emp2.fullname, 'Joan Doe')

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 42000)

    def test_monthly_schedule(self):
        print("test_monthly_schedule")
        with patch('employees.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success!"

            schedule = self.emp1.monthly_schedule('July')
            mocked_get.assert_called_with("http://company.com/Doe/July")
            self.assertEqual(schedule, "Success!")

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with("http://company.com/Doe/June")
            self.assertEqual(schedule, "Bad Response!")

if __name__ == "__main__":
    unittest.main()
