# ------------------------------STAGE 1----------------------------------------------
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

while True:
    print(msg_0)
    operation_string = input()
    operation_list = operation_string.split(sep=" ", maxsplit=3)
    x = operation_list[0]
    oper = operation_list[1]
    y = operation_list[2]
    try:
        float(x) and float(y)
    except:
        print(msg_1)
        continue
    if not (oper in ['+', '-', '*', '/']):
        print(msg_2)
        continue
    break
