#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callback(msg):
    if msg.data >= 35.0:
        rospy.logwarn("경고! 고온 감지: %.1f도", msg.data)
    else:
        rospy.loginfo("정상: %.1f도", msg.data)

def listener():
    rospy.init_node('temp_sub')
    rospy.Subscriber('temperature', Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
