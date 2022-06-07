import constant


def get_money():  # 从文件中读取现有金额
    f = open("money.txt")  # 返回一个文件对象
    constant.now_money = f.read()  # 这里得到的是str类型
    f.close()


def format_money(now_money):  # 将金额格式化为字符串格式
    # 拆分成整数部分和小数部分
    x = str(now_money)
    number_str_list = x.split('.')
    integer_part = number_str_list[0]
    decimal_part = None if len(number_str_list) == 1 else number_str_list[1]

    new_integer_part = ''
    reversed_integer_part = integer_part[::-1]  # 将字符串左右反转
    for i, c in enumerate(reversed_integer_part):  # 遍历字符，每隔3个字符加逗号
        if i > 0 and i % 3 == 0:
            new_integer_part = new_integer_part + ',' + c
        else:
            new_integer_part += c
    new_integer_part = new_integer_part[::-1]  # 将字符串左右反转

    if decimal_part:
        # print('添加千分位后数字变为', new_integer_part)
        constant.format_money = new_integer_part + '.' + decimal_part
    else:
        # print('添加千分位后数字变为', new_integer_part)
        constant.format_money = new_integer_part
