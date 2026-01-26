import os
import csv
from typing import Any

from model.employee import Employee

class CSVHandler:
    def __init__(self,filepath="data/payroll.csv"):
        self.filepath=filepath
        self.fieldnames = ["ID", "Full Name", "Base Salary", "Department", "Overtime Hours", "Hourly Rate"]
        self._initialize()


    def _initialize(self):
        #Makes directory
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        #makes file
        if not (os.path.exists("data/payroll.csv")):
            with open(self.filepath,"w",newline="",encoding="utf-8") as f:
                writer=csv.DictWriter(f,fieldnames=self.fieldnames)
                writer.writeheader()

    def _get_next_id(self)->int:
        """Reads the file and returns the next available id"""
        last_id=0
        try:
            with open(self.filepath,"r",encoding="utf-8") as f:
                reader=list(csv.DictReader(f))
                if reader:
                    last_id=int(reader[-1]["ID"])
        except(FileNotFoundError,IndexError,ValueError):
            pass
        return last_id+1

    def save_employee(self,emp_dict:dict):
        new_id=self._get_next_id()
        emp_dict["ID"]=new_id

        with open(self.filepath,"a",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=self.fieldnames)
            writer.writerow(emp_dict)
        return new_id

    def load_all_employees(self):
        employees=[]
        try:
            with open(self.filepath,"r",encoding="utf-8") as f:
                reader=csv.DictReader(f)
                for row in reader:
                    emp=Employee(
                        emp_id=int(row["ID"]),
                        fullname=row["Full Name"],
                        department=row["Department"],
                        base_salary=float(row["Base Salary"]),
                        overtime_hours=float(row["Overtime Hours"]),
                        hourly_rate=float(row["Hourly Rate"])
                    )
                    employees.append(emp)
        except FileNotFoundError:
            return []
        return employees


    def delete_employee(self,emp_id):
        data_loaded=self.load_all_employees()
        updated_list=[]

        for data in data_loaded:
            if not data.emp_id==emp_id:
                updated_list.append(data)

        try:
            with open(self.filepath,"w",newline="",encoding="utf-8") as f:
                writer=csv.DictWriter(f,self.fieldnames)
                writer.writeheader()

                for emp in updated_list:
                    writer.writerow(emp.to_dict())
                return True
        except FileNotFoundError,PermissionError:
            return False

    def update_employee(self, updated_emp: Employee) -> bool:
        data_loaded = self.load_all_employees()
        new_data = []
        found = False

        for emp in data_loaded:
            if emp.emp_id == updated_emp.emp_id:
                new_data.append(updated_emp)
                found = True
            else:
                new_data.append(emp)

        if not found:
            return False
        try:
            with open(self.filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()

                for emp in new_data:
                    writer.writerow(emp.to_dict())
            return True
        except (FileNotFoundError, PermissionError):
            return False