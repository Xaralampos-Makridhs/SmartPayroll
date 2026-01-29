import sys
from business.payroll_calculator import PayrollCalculator
from business.generate_company_report import CompanyReport
from emailservice.emailservice import EmailService
from storage.csvhandler import CSVHandler
from payslip.format_payslip import format_payslip

def show_menu():
  print("\n"+ "="*30)
  print("    PAYROLL MANAGEMENT SYSTEM    ")
  print("="*30)
  print("1. View Employees and Salaries")
  print("2. Update Overtime hours for employees")
  print("3. Bulk Send Email Payslips")
  print("4. Generate Total Company Report")
  print("5. Add New Employee")
  print("6. Delete Employee")
  print("7. Exit")
  print("="*30)

def main():
    """Main entry point for the payroll Management System.
       Coordinates user input,payroll calculation, data persistence via CSV, and automated distribution of payslips
    """

    handler=CSVHandler("data/payroll.csv")
    calculator=PayrollCalculator()
    reporter=CompanyReport()
    mailer=EmailService()

    while True:
        show_menu()
        choice=input("Select an option (1-7): ")

        if choice=="1":
            employees=handler.load_all_employees()
            if not employees:
                print("\n[!] No employees found.")
                continue

            print("\n {:<5} {:<25} {:<12} {:<12}".format("ID","Full Name","Gross (Euros)","Net (Euros)"))
            print("-"*60)

            for emp in employees:
                res=calculator.calculate_employee_payroll(emp)
                print("{:<5} {:<25} {:< 12.2f} {:<12.2f}".format(emp.emp_id,emp.fullname,res['Gross Salary'],res['Net Salary']))

        elif choice=="2":
            try:
                emp_id=int(input("Enter employee ID to update overtime: "))
                employees=handler.load_all_employees()
                target_emp=next((e for e in employees if e.emp_id==emp_id),None)

                if target_emp:
                    hours=float(input(f"Enter overtime hours for {target_emp.fullname}: "))
                    target_emp.overtime_hours=hours
                    if handler.upfate_overtime_hours(target_emp):
                        print("Overtime updated successfully.")
                    else:
                        print("Failed to update CSV file.")
            except ValueError:
                print("Invalid inputs. Please enter numbers only.")

        elif choice=="3":
            employees=handler.load_all_employees()
            if not employees:
                print("\n[!] No employees to email")
                continue
            confirm=input(f"Confirm sending {len(employees)} emails? (y/n): ")
            if confirm.lower()=='y':
                for emp in employees:
                    res=calculator.calculate_employee_payroll(emp)
                    body=format_payslip(res)

                    print(f"Sending to {emp.email}...", end=" ")
                    subject=f"Monthly Payslips - {emp.fullname}"
                    if mailer.send_payslip(emp.email,subject,body):
                        print("Done!")
                    else:
                        print("Fail")
            else:
                print("Operation cancelled.")

        elif choice=="4":
            employees=handler.load_all_employees()
            if not employees:
                print("\n[!] No employees found")
                continue
            report=reporter.generate_company_report(employees)
            print("\n"+ "*"*30)
            print("    TOTAL COMPANY REPORT    ")
            print("*"*30)
            for key,value in report.items():
                unit="EUR" if "Total" in key and "Employees" not in key else ""
                print(f"{key}: {value} {unit}")
            print("*"*30)

        elif choice=="5":
            try:
                name=input("Full Name: ")
                email=input("Email: ")
                salary=float(input("Base Salary: "))
                dept=input("Department: ")
                hourly=float(input("Hourly Overtime Rate: "))

                new_emp_data={
                    "Full Name":name,
                    "Email": email,
                    "Base Salary": salary,
                    "Department": dept,
                    "Overtime Hours": 0.0,
                    "Hourly Rate":hourly
                }

                handler.save_employee(new_emp_data)
                print("Employee added successfully")
            except ValueError as e:
                print(f"Input Error:{e}")

        elif choice=="6":
            eid=int(input("Enter Employee ID to delete: "))
            if handler.delete_employee(eid):
                print(f"Employee {eid} removed.")
            else:
                print("Not found!")

        elif choice=="7":
            print("Exiting Payroll System.Goodbye!")
            sys.exit()
        else:
            print("Invalid selection.Try again.")


if __name__=="__main__":
    main()






