#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def circle():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_circle')
    rate = rospy.Rate(10)  # 10Hz — 부드러운 움직임을 위해

    msg = Twist()
    msg.linear.x = 2.0   # 전진 속도
    msg.angular.z = 2.0   # 회전 속도

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
