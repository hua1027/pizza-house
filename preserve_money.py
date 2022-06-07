# 保存现有金额
import constant

def preserve_money():
    money = str(constant.float_money)
    with open("money.txt", "w") as f:
        f.write(money)  # 自带文件关闭功能，不需要再写f.close()