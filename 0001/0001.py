# -*- coding:utf-8 -*-
# 第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）

import random
import string

# 随机字符内容集合
forSelect = string.ascii_letters + "0123456789"


# 生成随机激活码函数
def generate_active_code(count, length):
    # 循环需要生成的个数
    for x in range(count):
        active_code = ""  # 激活码指针
        for y in range(length):  # 循环需要的长度
            active_code += random.choice(forSelect)  # 从随机集合中随机取一个字符拼接上去
        print(active_code)
# 主函数


if __name__ == "__main__":
    generate_active_code(30, 20)
