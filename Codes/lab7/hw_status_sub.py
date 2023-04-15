#!/usr/bin/env python3
import rospy
from my_robot_msgs.msg import HardwareStatus


def callback_receive_radio_data(msg):
    rospy.loginfo("Message received for pub:")
    rospy.loginfo(msg)


if __name__ == "__main__":
    rospy.init_node("subscriber_1")
    sub = rospy.Subscriber(
        "/my_robot/hardware_status", HardwareStatus, callback_receive_radio_data
    )
    rospy.spin()
