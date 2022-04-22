tax_rate=0.20
print("enter your income")
gross_income= int(input())

standar_deduction = 10000

print("enter number of dependents")
dependents= int(input())
dependent_deduction= 3000

taxable_income =gross_income - standar_deduction - (dependents*dependent_deduction)
tax= taxable_income*tax_rate
print('tax:')
if tax >=0:
  print(tax)
 else:
  print("0")
  
