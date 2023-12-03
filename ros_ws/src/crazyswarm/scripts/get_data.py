# 导入csv模块，用于读取csv文件
import csv

# 定义一个函数，用于从文件中读取每一行内容，并返回一个列表
def get_lines_from_file(filename):

    # 打开文件，创建一个csv读取对象
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        # 定义一个空列表，用于存储每一行内容
        lines = []

        # 遍历每一行，将其添加到列表中
        for line in reader:
            lines.append(line)

        # 返回列表
        return lines

    # 调用函数，传入文件名，打印结果



if __name__ == '__main__':
    lines = get_lines_from_file('points.csv')
    print(lines)