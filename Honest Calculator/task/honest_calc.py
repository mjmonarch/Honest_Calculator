# # ------------------------------STAGE 1----------------------------------------------
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
#
# while True:
#     print(msg_0)
#     operation_string = input()
#     operation_list = operation_string.split(sep=" ", maxsplit=3)
#     x = operation_list[0]
#     oper = operation_list[1]
#     y = operation_list[2]
#     try:
#         float(x) and float(y)
#     except:
#         print(msg_1)
#         continue
#     if not (oper in ['+', '-', '*', '/']):
#         print(msg_2)
#         continue
#     break

# # ------------------------------STAGE 2----------------------------------------------
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
#
# while True:
#     print(msg_0)
#     operation_string = input()
#     operation_list = operation_string.split(sep=" ", maxsplit=3)
#     try:
#         x = float(operation_list[0])
#         y = float(operation_list[2])
#     except:
#         print(msg_1)
#         continue
#     oper = operation_list[1]
#     if not (oper in ['+', '-', '*', '/']):
#         print(msg_2)
#         continue
#     if oper == '+':
#         result = x + y
#     elif oper == '-':
#         result = x - y
#     elif oper == "*":
#         result = x * y
#     elif oper == "/" and y == 0:
#         print(msg_3)
#         continue
#     else:
#         result = x / y
#     print(result)
#     break

# # ------------------------------STAGE 3----------------------------------------------
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):"
# msg_5 = "Do you want to continue calculations? (y / n):"
#
# memory = 0.0
# finished = True
# while True:
#     print(msg_0)
#     operation_string = input()
#     operation_list = operation_string.split(sep=" ", maxsplit=3)
#     x = operation_list[0]
#     oper = operation_list[1]
#     y = operation_list[2]
#     if x == 'M':
#         x = memory
#     elif y == 'M':
#         y = memory
#     try:
#         x = float(x)
#         y = float(y)
#     except:
#         print(msg_1)
#         continue
#     oper = operation_list[1]
#     if not (oper in ['+', '-', '*', '/']):
#         print(msg_2)
#         continue
#     if oper == '+':
#         result = x + y
#     elif oper == '-':
#         result = x - y
#     elif oper == "*":
#         result = x * y
#     elif oper == "/" and y == 0:
#         print(msg_3)
#         continue
#     else:
#         result = x / y
#     print(result)
#     while True:
#         print(msg_4)
#         answer = input()
#         if answer == 'y':
#             memory = result
#         elif answer != 'n':
#             continue
#         break
#     while True:
#         print(msg_5)
#         answer = input()
#         if answer == 'y':
#             finished = False
#             break
#         elif answer != 'n':
#             continue
#         finished = True
#         break
#     if finished:
#         break

# # ------------------------------STAGE 4----------------------------------------------
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):"
# msg_5 = "Do you want to continue calculations? (y / n):"
# msg_6 = " ... lazy"
# msg_7 = " ... very lazy"
# msg_8 = " ... very, very lazy"
# msg_9 = "You are"
#
#
# def check(v1, v2, v3):
#     msg = ""
#     if is_one_digit(v1) and is_one_digit(v2):
#         msg += msg_6
#     if (v1 == 1 or v2 == 1) and v3 == '*':
#         msg += msg_7
#     if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
#         msg += msg_8
#     if msg != "":
#         msg = msg_9 + msg
#         print(msg)
#
#
# def is_one_digit(v):
#     if -10 < v < 10 and v.is_integer():
#         return True
#     return False
#
#
# memory = 0.0
# finished = True
# while True:
#     print(msg_0)
#     operation_string = input()
#     operation_list = operation_string.split(sep=" ", maxsplit=3)
#     x = operation_list[0]
#     oper = operation_list[1]
#     y = operation_list[2]
#     if x == 'M':
#         x = memory
#     elif y == 'M':
#         y = memory
#     try:
#         x = float(x)
#         y = float(y)
#     except:
#         print(msg_1)
#         continue
#     oper = operation_list[1]
#     if not (oper in ['+', '-', '*', '/']):
#         print(msg_2)
#         continue
#     check(x, y, oper)
#     if oper == '+':
#         result = x + y
#     elif oper == '-':
#         result = x - y
#     elif oper == "*":
#         result = x * y
#     elif oper == "/" and y == 0:
#         print(msg_3)
#         continue
#     else:
#         result = x / y
#     print(result)
#     while True:
#         print(msg_4)
#         answer = input()
#         if answer == 'y':
#             memory = result
#         elif answer != 'n':
#             continue
#         break
#     while True:
#         print(msg_5)
#         answer = input()
#         if answer == 'y':
#             finished = False
#             break
#         elif answer != 'n':
#             continue
#         finished = True
#         break
#     if finished:
#         break

# ------------------------------STAGE 5----------------------------------------------
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
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msgs = {0: msg_0, 1: msg_1, 2: msg_2, 3: msg_3, 4: msg_4, 5: msg_5, 6: msg_6,
        7: msg_7, 8: msg_8, 9: msg_9, 10: msg_10, 11: msg_11, 12: msg_12}


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


memory = 0.0
finished = True
while True:
    print(msg_0)
    operation_string = input()
    operation_list = operation_string.split(sep=" ", maxsplit=3)
    x = operation_list[0]
    oper = operation_list[1]
    y = operation_list[2]
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except:
        print(msg_1)
        continue
    oper = operation_list[1]
    if not (oper in ['+', '-', '*', '/']):
        print(msg_2)
        continue
    check(x, y, oper)
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y == 0:
        print(msg_3)
        continue
    else:
        result = x / y
    print(result)
    while True:
        print(msg_4)
        answer = input()
        if answer != 'n' and answer != 'y':
            continue
        break
    if answer == 'y':
        if is_one_digit(result):
            msg_index = 10
            while True:
                print(msgs[msg_index])
                answer = input()
                if answer == 'y':
                    if msg_index < 12:
                        msg_index += 1
                        continue
                    else:
                        memory = result
                        break
                elif answer != 'n':
                    continue
                else:
                    break
        else:
            memory = result
    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            finished = False
            break
        elif answer != 'n':
            continue
        finished = True
        break
    if finished:
        break
