#Defining variables
monthly_income = int (input("Enter your monthly income: "))
monthly_expenses = int (input("Enter your total monthly expenses:: "))

#calculating monthly savings
monthly_savings = monthly_income - monthly_expenses
print("Your Monthly Savings are $ ", monthly_savings )

#projected savings after one year
annual_interestRate = 5
projected_savings = monthly_savings * 12 + ( monthly_savings * 12 * 0.05)

#Results
print("Projected Savings after one year, with interest, is: $", projected_savings)
