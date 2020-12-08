# Write your code here
annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))


current_savings = 0
r = .04
portion_down_payment= .25
number_of_months = 0
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
   number_of_months += 1
   current_savings += current_savings * r/12
   current_savings += annual_salary * portion_saved /12
  

 
print("Number of months: ", number_of_months)    
