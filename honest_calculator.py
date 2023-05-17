# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_index10_12 = ["Are you sure? It is only one digit! (y / n)",
                  "Don't be silly! It's just one number! Add to the memory? (y / n)",
                  "Last chance! Do you really want to embarrass yourself? (y / n)"]
operands = ["+", "-", "*", "/"]
memory = 0.0
result = 0.0
msg_index = 0


def calculation(a, b, operand):
    if operand == "+":
        return a + b
    elif operand == "-":
        return a - b
    elif operand == "*":
        return a * b
    elif operand == "/":
        return a / b


def is_one_digit(a):
    if a > -10 and a < 10 and a.is_integer():
        return True
    else:
        return False


def honest_check(a, b, operand):
    msg_check = ""
    # print(msg_check)
    if is_one_digit(a) == True and is_one_digit(b) == True:
        msg_check += msg_6
        # print(b.is_integer())
    if (a == 1 or b == 1) and operand == "*":
        msg_check += msg_7
        # print(msg_check)
    if (a == 0 or b == 0) and (operand in ["*", "+", "-"]):
        msg_check += msg_8
        # print(msg_check)
    if msg_check != "":
        msg_check = msg_9 + msg_check
        print(msg_check)


while True:
    print(msg_0)
    x, oper, y = input().split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
        x / y
    except ValueError:
        print(msg_1)
        continue
    except ZeroDivisionError:
        honest_check(x, y, oper)
        print(msg_3)
        continue
    else:
        if oper not in operands:
            print(msg_2)
            continue

        else:
            honest_check(x, y, oper)
            result = calculation(x, y, oper)
            print(result)
            if oper == "-" and (x or y) == 5: print(x, y, oper)

        while True:
            print(msg_4)
            store = input()
            if store == "y":
                if is_one_digit(result):
                    msg_index = 0
                    while True:
                        print(msg_index10_12[msg_index])
                        answer = input()
                        if answer == "y":
                            if msg_index < 2:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                        else:
                            continue
                else:
                    memory = result
                break
            elif store == "n":
                memory = 0.
                break
            else:
                continue

        while True:
            print(msg_5)
            cont = input()
            if cont == "y" or cont == "n":
                break
            else:
                continue

        if cont == "y":
            continue
        else:
            break