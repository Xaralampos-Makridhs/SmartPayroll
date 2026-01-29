from model.employee import Employee

class PayrollCalculator:
    INSURANCE_RATE=0.1387 #13.87%
    TAX_RATE=0.20 #20%
    EMPLOYER_CONTRIBUTION_RATE=0.2229 #22.29%

    def calculate_employee_payroll(self,employee:Employee)->dict:
        """Calculates the salary based on insurance rate,tax rate and employee contribution rate"""

        base=employee.base_salary
        overtime_pay=employee.calculate_gross_salary()

        total_gross=employee.get_total_gross_salary()
        insurance=round(total_gross*self.INSURANCE_RATE,2)

        taxable_amount=round(total_gross-insurance,2)

        tax=round(taxable_amount*self.TAX_RATE,2)

        net_salary=round(taxable_amount-tax,2)

        return {
            "Full Name": employee.fullname,
            "Gross Salary": total_gross,
            "Insurance": insurance,
            "Taxable Amount": taxable_amount,
            "Tax": tax,
            "Net Salary": net_salary
        }