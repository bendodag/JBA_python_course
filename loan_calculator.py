import math
import argparse
import sys

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
months = args.periods


if loan_type is None or loan_type not in ["annuity", "diff"] or interest is None:
    print("Incorrect parameters")
    sys.exit()

if len(sys.argv) <= 4:
    print("Incorrect number of parameters")
    sys.exit()

if loan_type == "diff" and monthly_payment is not None:
    print("Incorrect diff option parameters")
    sys.exit()

if any(arg is not None and arg < 0 for arg in [loan_principal, monthly_payment, interest, months]):
    print("Incorrect values of parameters, can't be < 0")
    sys.exit()


if loan_type == "diff":
    pass

if loan_type == "annuity":

    if months is None:

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

        nom_interest = interest / (12 * 100)
        monthly_payment = loan_principal * nom_interest * pow((1 + nom_interest), months) / (
                    pow(1 + nom_interest, months) - 1)

        print(f'Your monthly payment = {math.ceil(monthly_payment)}!')

    elif loan_principal is None:

        nom_interest = interest / (12 * 100)
        loan_principal = monthly_payment * (pow(1 + nom_interest, months) - 1) / (
                    nom_interest * pow((1 + nom_interest), months))

        print(f'Your loan principal = {round(loan_principal)}!')

    else:
        print("Unexpected behavior. Option is not implemented.")
        pass

