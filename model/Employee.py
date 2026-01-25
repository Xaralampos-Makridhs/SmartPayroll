class Employee:
    def __init__(self,emp_id:int,fullname:str,department:str,base_salary:float,overtime_hours:float,hourly_rate:float):
        self.emp_id=emp_id
        self.fullname=fullname
        self.department=department
        self.base_salary=base_salary
        self.overtime_hours=overtime_hours
        self.hourly_rate=hourly_rate

        self._validation()

    def _validation(self):
        if not self.fullname.strip()==0:
            raise ValueError("Full name is required and cannot be empty.")
        if self.emp_id<0:
            raise ValueError("Id must be positive number.")
        if len(self.department)==0:
            raise ValueError("Department is required.")
        if self.base_salary<=0:
            raise ValueError("Base salary must be positive number.")
        if self.overtime_hours<0:
            raise ValueError("Overtime hours must be positive number.")
        if self.hourly_rate<0:
            raise ValueError("Hourly rate must be positive number.")



    def calculate_gross_salary(self)->float:
        return self.overtime_hours*self.hourly_rate

    def get_total_gross_salary(self)->float:
        return self.base_salary+self.calculate_gross_salary()

    def to_dict(self):
        return {
            "Employee ID": self.emp_id,
            "Full Name": self.fullname,
            "Department": self.department,
            "Base Salary": self.base_salary,
            "Overtime Hours": self.overtime_hours,
            "Hourly Rate": self.hourly_rate,
            "Total Gross": self.get_total_gross_salary()
        }

    def __str__(self):
        return f"Employee: {self.fullname} (ID: {self.emp_id} | Department:{self.department})"