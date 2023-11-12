import unittest
from assignment3_code import EmployeeDataProcessor, Employee 

class TestEmployeeDataProcessor(unittest.TestCase):

    def setUp(self):
        self.emp_data_processor = EmployeeDataProcessor()
        self.file_name = "C:\\Users\\angel\\Downloads\\employee_data.csv"  

    def test_get_data_list_from_csvfile(self):
        data_list = self.emp_data_processor.get_data_list_from_csvfile(self.file_name)
        self.assertTrue(isinstance(data_list, list))
        self.assertTrue(len(data_list) > 0)
        self.assertTrue(isinstance(data_list[0], Employee))

    def test_get_data_size(self):
        self.emp_data_processor.initialize(self.file_name)
        data_size = self.emp_data_processor.get_data_size()
        self.assertTrue(data_size > 0)

    def test_get_employee_record(self):
        self.emp_data_processor.initialize(self.file_name)
        employee = self.emp_data_processor.get_employee_record("John", "Doe", 5)
        self.assertIsNotNone(employee)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.years, 5)

    def test_get_employee_list(self):
        self.emp_data_processor.initialize(self.file_name)
        employee_list = self.emp_data_processor.get_employee_list(0, 5, sorted=True)
        self.assertEqual(len(employee_list), 5)
        self.assertTrue(all(isinstance(emp, Employee) for emp in employee_list))

    def test_get_years_list(self):
        self.emp_data_processor.initialize(self.file_name)
        years_list = self.emp_data_processor.get_years_list()
        self.assertTrue(all(isinstance(year, int) for year in years_list))

if __name__ == '__main__':
    unittest.main()
