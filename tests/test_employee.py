import unittest
from model.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Initial Data"""
        self.valid_emp=Employee(
            emp_id=1,
            fullname="Makridhs Xaralampos",
            department="IT",
            base_salary=1200.0,
            overtime_hours=10.0,
            hourly_rate=20.0
        )

    def test_initialization(self):
        """Tests if data saved during initialization"""
        self.assertEqual(self.valid_emp.emp_id,1)
        self.assertEqual(self.valid_emp.fullname,"Makridhs Xaralampos")

    def test_salary_calculation(self):
        """Tests the mathematician functions"""
        self.assertEqual(self.valid_emp.calculate_gross_salary(),200)
        self.assertEqual(self.valid_emp.get_total_gross_salary(),1400)

    def test_to_dict(self):
        """Tests if dictionary has the right keys"""
        data=self.valid_emp.to_dict()
        self.assertEqual(data['Employee ID'],1)
        self.assertEqual(data['Total Gross'],1400)

    def test_invalid_id_raise_error(self):
        """Tests if raises ValueError for negative ID"""
        with self.assertRaises(ValueError):
            Employee(-1,"Name","IT",1000,0,0)

    def test_invalid_salary_raises_error(self):
        """Tests if raises ValueError for 0 or negative salary"""
        with self.assertRaises(ValueError):
            Employee(2,"Name","IT",0,0,0)

if __name__=='__main__':
    unittest.main()




