# 导入re模块，用于正则表达式匹配
import re
# 导入csv模块，用于写入csv文件
import csv


# 定义一个函数，用于从文件中读取点坐标，并返回一个列表
def get_points_from_file(filename):
    # 打开文件，读取内容
    with open(filename, 'r') as f:
        content = f.read()

    # 定义一个空列表，用于存储点坐标
    points = []

    # 定义一个正则表达式，用于匹配点坐标的格式
    pattern = r'position:\s*x: (-?\d+\.?\d*)\s*y: (-?\d+\.?\d*)\s*z: (-?\d+\.?\d*)'
    # 使用re.findall函数，找到所有匹配的点坐标，并转换为浮点数
    matches = re.findall(pattern, content)
    for match in matches:
        # 将字符串转换为浮点数
        # 浮点数保留小数点后两位
        # 数据保存不要用科学计数法
        x, y, z = float(match[0]), float(match[1]), float(match[2])
        x = round(x, 2) / 2
        y = round(y, 2) / 2
        z = round(z, 2) / 2
        if not points or (x, y, z) != points[-1]:
            points.append((x, y, z))

    # 返回点坐标列表
    return points


def write_points_to_csv(points, filename):
    # 打开文件，创建一个csv写入对象
    with open(filename, 'w') as f:
        writer = csv.writer(f)

        # 写入表头
        writer.writerow(['x', 'y', 'z'])

        # 遍历每个点坐标，写入一行数据
        for point in points:
            writer.writerow(point)


# 调用函数，传入文件名，打印结果
points = get_points_from_file('drone0.txt')
print(points)
write_points_to_csv(points, 'drone0.csv')

points = get_points_from_file('drone1.txt')
print(points)
write_points_to_csv(points, 'drone1.csv')

points = get_points_from_file('drone2.txt')
print(points)
write_points_to_csv(points, 'drone2.csv')

points = get_points_from_file('drone3.txt')
print(points)
write_points_to_csv(points, 'drone3.csv')

points = get_points_from_file('drone4.txt')
print(points)
write_points_to_csv(points, 'drone4.csv')

points = get_points_from_file('drone5.txt')
print(points)
write_points_to_csv(points, 'drone5.csv')

points = get_points_from_file('drone6.txt')
print(points)
write_points_to_csv(points, 'drone6.csv')
