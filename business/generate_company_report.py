from model.employee import Employee


class CompanyReport:
    def __init__(self):
        self.INSURANCE_RATE=0.1387 #13.87%
        self.TAX_RATE=0.20 #20%

    def calculate_employee_payroll(self,employee:Employee)->dict:
        total_gross=employee.get_total_gross_salary()

        insurance=round(total_gross*self.INSURANCE_RATE,2)
        taxable_income=round(total_gross-insurance,2)
        tax=round(taxable_income*self.TAX_RATE,2)
        net_salary=round(taxable_income-tax,2)

        return {
            "Full Name": employee.fullname,
            "Gross Salary": total_gross,
            "Insurance": insurance,
            "Taxable Amount": taxable_income,
            "Tax": tax,
            "Net Salary": net_salary
        }

    def generate_company_report(self, employees_list: list) -> dict:
        report = {
            "Total Employees": len(employees_list),
            "Total Net Pay": 0.0,
            "Total Taxes": 0.0,
            "Total Insurance": 0.0,
            "Total Gross": 0.0
        }

        for emp in employees_list:
            payroll = self.calculate_employee_payroll(emp)

            report["Total Net Pay"] += payroll["Net Salary"]
            report["Total Taxes"] += payroll["Tax"]
            report["Total Insurance"] += payroll["Insurance"]
            report["Total Gross"] += payroll["Gross Salary"]

        for key in report:
            if key != "Total Employees":
                report[key] = round(report[key], 2)
        return report