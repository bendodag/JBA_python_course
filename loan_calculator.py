# monthly_payment = math.ceil(loan_principal / months)
# last_payment = loan_principal - (months - 1) * monthly_payment
import math

print("What do you want to calculate?")
print("type 'n' for number of monthly payments,")
print("type 'a' for annuity monthly payment amount,")
print("type 'p' for loan principal:")
question = input()

if question == "n":
    loan_principal = float(input("Enter the loan principal:"))
    monthly_payment = float(input("Enter the monthly payment:"))
    interest = float(input("Enter the loan interest:"))

    nom_interest = interest / (12 * 100)
    months = math.ceil(
        math.log(monthly_payment / (monthly_payment - nom_interest * loan_principal), 1 + nom_interest))
    if months == 1:
        print("It will take 1 month to repay the loan")
    elif months in range(2, 12):
        print(f'It will take {months} months to repay the loan')
    elif months == 12:
        print("It will take 1 year to repay the loan")
    elif months % 12 == 0:
        print(f'It will take {months / 12} years to repay the loan')
    else:
        print(f'It will take {math.floor(months / 12)} years and {months % 12} months to repay the loan')

elif question == "a":
    loan_principal = float(input("Enter the loan principal:"))
    months = float(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))

    nom_interest = interest / (12 * 100)
    monthly_payment = loan_principal * nom_interest * pow((1 + nom_interest), months) / (
                pow(1 + nom_interest, months) - 1)

    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')

elif question == "p":
    monthly_payment = float(input("Enter the annuity payment:"))
    months = float(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))

    nom_interest = interest / (12 * 100)
    loan_principal = monthly_payment * (pow(1 + nom_interest, months) - 1) / (
                nom_interest * pow((1 + nom_interest), months))

    print(f'Your loan principal = {loan_principal}!')

else:
    pass

