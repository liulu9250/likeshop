import csv
# 日志的配置信息
import logging
import random
from logging import config

config.fileConfig('config/log.conf')
# 获取打印日志对象
logger = logging.getLogger()

#自己定义一个随机函数-获取随机字符串
def getRandomStr(length):
    str = "abcdefghijklmnopqrstuvwxyz"
    randStr = ""
    for i in range(0, length):
        index = random.randint(0, len(str) - 1)
        # 根据索引获取字符
        c = str[index]
        randStr = randStr + c
    return randStr

def getRandomNum(min,max):
    return random.randint(min,max)


def getCsvData(csv_file):
    file = open(file=csv_file, mode='r', encoding='utf-8-sig')
    # 把表格里面所有的数据读取,记录到reader对象
    reader = csv.reader(file)
    list = []
    for index, row in enumerate(reader, 1):
        list.append(row)
    return list


# 读取单行csv数据
# 读取excel/csv表格数据..csv_file读取的文件路径,line读取哪一行
def getCsvDataByLine(csv_file, line):
    file = open(file=csv_file, mode='r', encoding='utf-8-sig')
    # 把表格里面所有的数据读取,记录到reader对象
    reader = csv.reader(file)
    for index, row in enumerate(reader, 1):
        # 判断行号是否和当前索引一样，如果一样，直接返回数据index，从1开始
        if index == line:
            file.close()
            return row
