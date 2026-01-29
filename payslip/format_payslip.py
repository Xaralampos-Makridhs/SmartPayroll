def format_payslip(payroll_data: dict) -> str:
    """Formats the payroll dictionary into a human-readable English payslip."""

    payslip = f"""
=========================================
            PAYSLIP REPORT
=========================================
Employee Name:      {payroll_data["Full Name"]}
--------------------------------------------------
Gross Salary:       {payroll_data["Gross Salary"]:>12.2f} EUR
Social Insurance:  -{payroll_data["Insurance"]:>12.2f} EUR
Taxable Income:     {payroll_data["Taxable Amount"]:>12.2f} EUR
Income Tax:        -{payroll_data["Tax"]:>12.2f} EUR
--------------------------------------------------
NET PAY:            {payroll_data["Net Salary"]:>12.2f} EUR
==================================================
    """
    return payslip