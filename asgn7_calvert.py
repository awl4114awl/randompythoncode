import os

# Function to read employee data from the file
def read_employee_data(file_name):
    employee_data = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                last_name, first_name, salary, hire_date = line.strip().split('*')
                employee_data.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'salary': float(salary),
                    'hire_date': hire_date
                })
    return employee_data

# Function to sort employee data by last name
def sort_by_last_name(employee):
    return employee['last_name']

# Function to display employee information
def display_employee_info(employee_data):
    sorted_data = sorted(employee_data, key=sort_by_last_name)
    for i, employee in enumerate(sorted_data, start=1):
        hire_year = int(employee['hire_date'].split('/')[2])
        years_worked = 2023 - hire_year
        print(str(i) + '. ' + employee['last_name'] + ', ' + employee['first_name'] + ' - Salary: $' + '{:.2f}'.format(employee['salary']) + ', Years Worked: ' + str(years_worked))

# Function to search for an employee
def search_employee(employee_data, last_name, first_name):
    for employee in employee_data:
        if employee['last_name'].lower() == last_name.lower() and employee['first_name'].lower() == first_name.lower():
            hire_year = int(employee['hire_date'].split('/')[2])
            years_worked = 2023 - hire_year
            print("Last Name: " + employee['last_name'])
            print("First Name: " + employee['first_name'])
            print("Salary: $" + '{:.2f}'.format(employee['salary']))
            print("Years Worked: " + str(years_worked))
            return
    print("Employee not found.")

# Function to add an employee
def add_employee(employee_data, last_name, first_name, salary, hire_date):
    employee_data.append({
        'last_name': last_name,
        'first_name': first_name,
        'salary': float(salary),
        'hire_date': hire_date
    })
    print(first_name + ' ' + last_name + ' has been added.')

# Function to delete an employee
def delete_employee(employee_data, last_name, first_name):
    for employee in employee_data:
        if employee['last_name'].lower() == last_name.lower() and employee['first_name'].lower() == first_name.lower():
            employee_data.remove(employee)
            print(first_name + ' ' + last_name + ' has been deleted.')
            return
    print("Employee not found.")

# Function to save data to the file
def save_employee_data(file_name, employee_data):
    with open(file_name, 'w') as file:
        for employee in employee_data:
            file.write(employee['last_name'] + '*' + employee['first_name'] + '*' + '{:.2f}'.format(employee['salary']) + '*' + employee['hire_date'] + '\n')

# Main function
def main():
    file_name = "employee_data.txt"
    employee_data = read_employee_data(file_name)
    
    while True:
        print("\nEmployee Database App")
        print("1. View all employees")
        print("2. Search for an employee")
        print("3. Add an employee")
        print("4. Delete an employee")
        print("5. Done (save and exit)")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_employee_info(employee_data)
        elif choice == '2':
            last_name = input("Enter the last name: ")
            first_name = input("Enter the first name: ")
            search_employee(employee_data, last_name, first_name)
        elif choice == '3':
            last_name = input("Enter the last name: ")
            first_name = input("Enter the first name: ")
            salary = input("Enter the salary: ")
            hire_date = input("Enter the hire date (MM/DD/YYYY): ")
            add_employee(employee_data, last_name, first_name, salary, hire_date)
        elif choice == '4':
            last_name = input("Enter the last name: ")
            first_name = input("Enter the first name: ")
            delete_employee(employee_data, last_name, first_name)
        elif choice == '5':
            save_employee_data(file_name, employee_data)
            print("Data has been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
