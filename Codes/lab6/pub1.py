#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import String
if __name__ == '__main__':
        rospy.init_node('publisher_node')
        pub = rospy.Publisher("/robot_publisher_node",String, queue_size=10)
        rate = rospy.Rate(2)
        data=sys.argv[1]
        while not rospy.is_shutdown():
                msg = String()
                msg.data = data
                pub.publish(msg)
                rate.sleep()
        rospy.loginfo("Publisher Node stopped")