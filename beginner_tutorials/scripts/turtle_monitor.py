#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def callback(msg):
    warning = False

    if msg.x <= 1.0 or msg.x >= 10.0:
        rospy.logwarn("경고! x=%.1f — 좌우 벽에 가깝습니다!", msg.x)
        warning = True

    if msg.y <= 1.0 or msg.y >= 10.0:
        rospy.logwarn("경고! y=%.1f — 상하 벽에 가깝습니다!", msg.y)
        warning = True

    if not warning:
        rospy.loginfo("위치: (%.1f, %.1f) — 안전", msg.x, msg.y)

def monitor():
    rospy.init_node('turtle_monitor')
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    monitor()
