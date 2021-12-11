# ------------------------------STAGE 1----------------------------------------------
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

# ------------------------------STAGE 3----------------------------------------------
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

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
    elif y == 'M':
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
        if answer == 'y':
            memory = result
        elif answer != 'n':
            continue
        break
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
