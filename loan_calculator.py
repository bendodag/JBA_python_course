import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates your loan properties based on you input.")
parser.add_argument("-pa", "--payment")
parser.add_argument("-pr", "--principal")
parser.add_argument("-per", "--periods")
parser.add_argument("-in", "--interest")

args = parser.parse_args()
loan_principal = args.principal
monthly_payment = args.payment
interest = args.interest
n_months = args.periods


if n_months is None:
    loan_principal = float(loan_principal)
    monthly_payment = float(monthly_payment)
    interest = float(interest)

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

elif monthly_payment is None:
    loan_principal = float(loan_principal)
    months = float(n_months)
    interest = float(interest)

    nom_interest = interest / (12 * 100)
    monthly_payment = loan_principal * nom_interest * pow((1 + nom_interest), months) / (
                pow(1 + nom_interest, months) - 1)

    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')

elif loan_principal is None:
    monthly_payment = float(monthly_payment)
    months = float(n_months)
    interest = float(interest)

    nom_interest = interest / (12 * 100)
    loan_principal = monthly_payment * (pow(1 + nom_interest, months) - 1) / (
                nom_interest * pow((1 + nom_interest), months))

    print(f'Your loan principal = {round(loan_principal)}!')

else:
    print("Unexpected behavior. Option is not implemented.")
    pass

