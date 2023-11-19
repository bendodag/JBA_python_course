import math
import argparse
import sys


def overpayment(total, principal):
    print(f"Overpayment = {math.ceil(total - principal)}")


parser = argparse.ArgumentParser(description="This program calculates your loan properties based on your input.")
parser.add_argument("--type", type=str)
parser.add_argument("-pa", "--payment", type=float)
parser.add_argument("-pr", "--principal", type=float)
parser.add_argument("-per", "--periods", type=int)
parser.add_argument("-in", "--interest", type=float)

args = parser.parse_args()
loan_type = args.type
loan_principal = args.principal
monthly_payment = args.payment
interest = args.interest
n_months = args.periods

if loan_type is None or loan_type not in ["annuity", "diff"] or interest is None or len(sys.argv) <= 4:
    print("Incorrect parameters")
    sys.exit()

if loan_type == "diff" and monthly_payment is not None:
    print("Incorrect parameters")
    sys.exit()

if any(arg is not None and arg < 0 for arg in [loan_principal, monthly_payment, interest, n_months]):
    print("Incorrect parameters")
    sys.exit()

total_amount = 0
nom_interest = interest / (12 * 100)

if loan_type == "diff":

    for month in range(1, n_months + 1):
        diff_payment = math.ceil(loan_principal / n_months + nom_interest * (loan_principal - loan_principal * (month - 1) / n_months))
        total_amount += diff_payment
        print(f"Month {month}: payment is {diff_payment}")

    overpayment(total_amount, loan_principal)

if loan_type == "annuity":

    if n_months is None:
        n_months = math.ceil(
            math.log(monthly_payment / (monthly_payment - nom_interest * loan_principal), 1 + nom_interest))
        if n_months == 1:
            print("It will take 1 month to repay the loan")
        elif n_months in range(2, 12):
            print(f'It will take {n_months} months to repay the loan')
        elif n_months == 12:
            print("It will take 1 year to repay the loan")
        elif n_months % 12 == 0:
            print(f'It will take {int(n_months / 12)} years to repay the loan')
        else:
            print(f'It will take {math.floor(n_months / 12)} years and {n_months % 12} months to repay the loan')
        overpayment(n_months * monthly_payment, loan_principal)

    elif monthly_payment is None:
        monthly_payment = math.ceil(loan_principal * nom_interest * pow((1 + nom_interest), n_months) / (
                pow(1 + nom_interest, n_months) - 1))
        print(f'Your monthly payment = {monthly_payment}!')
        overpayment(n_months * monthly_payment, loan_principal)

    elif loan_principal is None:
        loan_principal = monthly_payment * (pow(1 + nom_interest, n_months) - 1) / (
                    nom_interest * pow((1 + nom_interest), n_months))
        print(f'Your loan principal = {math.floor(loan_principal)}!')
        overpayment(n_months * monthly_payment, loan_principal)

    else:
        print("Unexpected behavior. Option is not implemented.")

