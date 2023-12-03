from pycrazyswarm import *
import numpy as np
import csv

swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs

# 读取所有无人机的轨迹数据
trajectories = {}
for cf in allcfs.crazyflies:
    file = 'drone' + str(cf.id-1) + '.csv'
    with open(file, 'r') as f:
        reader = csv.reader(f)
        trajectory = [row for i, row in enumerate(reader) if i != 0]  # 跳过第一行
        trajectories[cf.id] = trajectory

# 计算起飞高度
takeoff_heights = {}
for cf in allcfs.crazyflies:
    takeoff_heights[cf.id] = float(trajectories[cf.id][0][2])

# 控制无人机起飞到起始高度
Z = 0.0
while Z < max(takeoff_heights.values()):
    for cf in allcfs.crazyflies:
        if Z < takeoff_heights[cf.id]:
            pos = np.array([float(trajectories[cf.id][0][0]), float(trajectories[cf.id][0][1]), Z])
            cf.cmdPosition(pos)
            print(f"Drone {cf.id} Takeoff Position:", pos)
    timeHelper.sleep(0.1)
    Z += 0.05

# 控制无人机移动
max_length = max(len(trajectory) for trajectory in trajectories.values())
for step in range(max_length):
    for cf in allcfs.crazyflies:
        trajectory = trajectories[cf.id]
        if step < len(trajectory):
            pos = np.array([float(trajectory[step][0]), float(trajectory[step][1]), float(trajectory[step][2])])
            cf.cmdPosition(pos)
            print(f"Drone {cf.id} Position:", pos)
    timeHelper.sleep(0.1)

timeHelper.sleep(1.0)

# 初始化Z为所有无人机中最高的起始高度
Z = max(float(trajectories[cf.id][-1][2]) for cf in allcfs.crazyflies)

while Z > 0.0:
    for cf in allcfs.crazyflies:
        # 获取当前无人机的最后一个位置坐标，但用循环中的Z值作为高度
        step = len(trajectories[cf.id]) - 1
        pos = np.array([float(trajectories[cf.id][step][0]), float(trajectories[cf.id][step][1]), Z])
        cf.cmdPosition(pos)
        print(f"Drone {cf.id} Landing Position:", pos)
    timeHelper.sleep(0.1)
    Z -= 0.05  # 在循环的每个迭代中统一减少高度

# turn-off motors
for cf in allcfs.crazyflies:
    cf.cmdStop()
