salary = float(input('Enter income : '))
insurance = float(input('Enter insurance'))
diff = salary - insurance

if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff*rate - deduction) # abs to calculate absolute value
print ('tax is %.2f' %tax)
