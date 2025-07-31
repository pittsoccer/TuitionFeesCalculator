# input
name = input("Enter student's name: ")
student_number = input("Enter student ID: ")
credit_hours = int(input("Enter credit hours: "))
tuition_per_credit = float(input("Enter tuition per credit hour: "))
fee_per_credit = float(input("Enter fees per credit hour: "))

# calculation
tuition = credit_hours * tuition_per_credit
fees = credit_hours * fee_per_credit
total_due = tuition + fees

# output
print()
print("~" * 40)
print(f"Student Name: {name}")
print(f"Student Number: {student_number}")
print(f"Credit Hours Registered: {credit_hours}")
print(f"Credit Hour Tuition: ${tuition_per_credit:.2f}")
print(f"Credit Hour Fee: ${fee_per_credit:.2f}")
print(f"Total Tuition: ${tuition:.2f}")
print(f"Total Fees: ${fees:.2f}")
print(f"Total Due: ${total_due:.2f}")
print("~" * 40)
