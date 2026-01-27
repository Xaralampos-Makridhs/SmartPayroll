import unittest
from model.employee import Employee
from business.payroll_calculator import PayrollCalculator

class TestPayrollCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=PayrollCalculator()

        self.emp=Employee(
            emp_id=1,
            fullname="Test User",
            department="IT",
            base_salary=1000.0,
            overtime_hour=10.0,
            hourly_rate=20.0
        )

    def test_calculate(self):
        result=self.calculator.calculate_employee_payroll(self.emp)

        self.assertEqual(result["Gross Salary"],1200.0)
        self.assertEqual(result["Insurance"], 166.44)
        self.assertEqual(result["Tax"], 206.71)
        self.assertEqual(result["Net Salary"],826.85)


