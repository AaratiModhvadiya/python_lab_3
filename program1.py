class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Date of Join: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary:.2f}")

# Example usage
if __name__ == "__main__":
    # Create employee objects
    emp1 = Employee("John Doe", "2024-01-15", "Software Engineer", 75000)
    emp2 = Employee("Jane Smith", "2023-06-22", "Project Manager", 85000)
    
    # Display employee information
    print("Employee 1 Information:")
    emp1.display_info()
    
    print("\nEmployee 2 Information:")
    emp2.display_info()
