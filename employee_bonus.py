import csv

employees = open('EmployeePay.csv', 'r')

employee_file = csv.reader(employees)

next(employee_file)

counter = 0

for rec in employee_file:

    total_pay = (int(rec[3])*(float(rec[4])+1))
    salary = int(rec[3])
    bonus = int(rec[3])*float(rec[4])
    print(rec[0] + ', ' + rec[1] + ' ' + rec[2])
    print(f"This is the employee's salary: $ {salary:,.2f}")
    print(f"This is the employee's bonus: $ {bonus:,.2f}")
    print(f"This is the employee's total pay: $ {total_pay:,.2f}")

   
    counter += 1

    input()
    
    
    







