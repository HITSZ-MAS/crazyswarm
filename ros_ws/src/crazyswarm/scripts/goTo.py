from pycrazyswarm import *
import numpy as np
import csv

# Initialize the swarm and get all Crazyflies
swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs

# Process each drone individually
for cf in allcfs.crazyflies:
    file_name = 'drone' + str(cf.id - 1) + '.csv'
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        data_line = next(reader)  # Read the next line for coordinates
        x, y = float(data_line[0]), float(data_line[1])  # Extract X and Y
        target_position = np.array([x, y, 1.0])  # Assuming Z = 1.0

    # Takeoff
    cf.takeoff(targetHeight=1.0, duration=2.0)
    timeHelper.sleep(2.5)

    # Move to target position
    cf.goTo(target_position, 0, 2.0)
    timeHelper.sleep(2.5)

    # Land
allcfs.land(targetHeight=0.02, duration=2.0)
timeHelper.sleep(2.0)

# After all drones have completed their sequence
print("All drones have reached their target positions and landed.")
