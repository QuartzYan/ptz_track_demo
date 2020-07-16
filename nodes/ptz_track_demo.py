#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import rospy 
import std_msgs

from pan_tilt_msg.msg import PanTiltCmd
from geometry_msgs.msg import PointStamped

sub = None
pub = None

def callBack(msg):
  msg.point.x 
  ptz_cmd = PanTiltCmd()
  '''
  if msg.point.x<346 and msg.point.y<130:
    yaw = 60 - (msg.point.x / 10 * 1.7)
    pitch = (msg.point.y / 10 * 4.6) - 60
  elif msg.point.x>346 and msg.point.y<130:
    yaw = 60 - (msg.point.x / 10 * 1.7)
    pitch = (msg.point.y / 10 * 4.6) - 60
  elif msg.point.x<346 and msg.point.y>130:
    yaw = 60 - (msg.point.x / 10 * 1.7)
    pitch = (msg.point.y / 10 * 4.6) - 60
  elif msg.point.x>346 and msg.point.y>130:
    yaw = 60 - (msg.point.x / 10 * 1.7)
    pitch = (msg.point.y / 10 * 4.6) - 60
  else:
      pass
  '''
  ptz_cmd.yaw = 60 - (msg.point.x / 10 * 1.7)
  ptz_cmd.pitch = (msg.point.y / 10 * 4.6) - 60
  ptz_cmd.speed = 20
  pub.publish(ptz_cmd)

def main():
  global sub, pub
  rospy.init_node("ptz_track_demo")
  sub = rospy.Subscriber("obj_point", PointStamped, callBack)
  pub = rospy.Publisher("pan_tilt_cmd", PanTiltCmd, queue_size=1)
  rospy.spin()

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass