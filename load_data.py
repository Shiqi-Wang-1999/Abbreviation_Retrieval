import pandas as pd

""" 读取excel数据"""


def read_excel(filepath):
    # 读取数据
    data = pd.read_excel(filepath)
    return data


"""将数据写入文档"""


def write_data(filepath, data):
    fo = open(filepath, "w+", encoding='utf8')
    if len(data) > 0:
        fo.write("\n".join(data))
    # 关闭打开的文件
    fo.close()


if __name__ == '__main__':
    """
    对excel的数据进行处理
    """
    filepath = "高校信息.xls"
    data = read_excel(filepath)
    # 观察数据格式
    print(data.values[3][1])
    # 获取高校全称
    new_data = [line[1] for line in data.values[3:] if str(line[1]) != 'nan']
    print(new_data[0])
    # 去除重复项
    new_data = list(set(new_data))
    outfile = "高校名称.txt"
    # 高校名称写入文档
    write_data(outfile, new_data)
