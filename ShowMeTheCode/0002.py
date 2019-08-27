# -*- coding:utf-8 -*-

import string
import random
import pymysql

forSelect = string.ascii_letters + "0123456789"


def generate_active_code(count, length):
    # 创建空的激活码集合
    active_codes = set()
    # 循环需要生成的个数
    for x in range(count):
        active_code = ""  # 激活码指针
        for y in range(length):  # 循环需要的长度
            active_code += random.choice(forSelect)  # 从随机集合中随机取一个字符拼接上去
            active_codes.add(active_code)  # 添加到集合
    return active_codes  # 返回激活码集合


if __name__ == "__main__":
    print("将生成的激活码存入MySQL数组")
    # 打开数据库
    db = pymysql.connect("localhost", "dlfkid", "test123" "0002DB")
    cursor = db.cursor()
    sql = "CREATE TABLE IF NOT EXISTS active_code (id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT NOT NULL"
    cursor.execute(sql)
    # 生成激活码集合
    my_active_codes = generate_active_code(30, 20)
    for active_code in my_active_codes:
        print("激活码" + active_code)
        insert_sql = "INSERT INTO active_code(code) VALUES('{active}')".format(active=active_code)
        cursor.execute(insert_sql)
        db.commit()