#!/usr/bin/env python3

import yaml
import subprocess

with open("../ros_ws/src/crazyswarm/launch/crazyflies.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for crazyflie in cfg["crazyflies"]:
    uri = "radio://0/{}/2M/E7E7E7E7{}".format(crazyflie["channel"], crazyflie["id"])
    subprocess.call(["rosrun crazyflie_tools reboot --uri " + uri + " --mode sysoff"], shell=True)
