# Ask for a user's basic salary and calculate a 10% tax deduction. Print the final salary after tax
salary=int(input('enter your basic salary:'))
tax=salary*0.1
final_salary=salary-tax
print("the final salary after tax deduction:",final_salary)
