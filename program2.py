# Define the main class Company
class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_info(self):
        print(f"Company Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Mobile No: {self.mobile_no}")

# Define the subclass Employee that inherits from Company
class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        # Initialize attributes of the base class
        super().__init__(name, city, mobile_no)
        # Initialize attributes of the subclass
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_employee_info(self):
        # Call the method to display company info
        self.display_company_info()
        print(f"Employee Name: {self.emp_name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

# Main program
if __name__ == "__main__":
    # Create an instance of the Employee class
    emp = Employee("Tech Solutions", "New York", "123-456-7890", "John Doe", "Software Engineer", 80000)
    
    # Display information
    emp.display_employee_info()
