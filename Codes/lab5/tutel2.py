#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys


def turtle_circle(length, breath):
    rospy.init_node("turtlesim", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(5)
    vel = Twist()
    vel.linear.x = 1
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0
    d = [0, 0]
    v = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    count = 0
    while not rospy.is_shutdown():
        if vel.linear.x:
            d[0] += 1
            if d[0] == length:
                count += 1
                vel.linear.x = v[count % 4][0]
                vel.linear.y = v[count % 4][1]
                d = [0, 1]
        else:
            d[1] += 1
            if d[1] == breath:
                count += 1
                vel.linear.x = v[count % 4][0]
                vel.linear.y = v[count % 4][1]
                d = [1, 0]

        rospy.loginfo("Radius = %f %f", d[0], d[1])
        rospy.loginfo("Count = %f", count)
        pub.publish(vel)
        rate.sleep()


if __name__ == "__main__":
    try:
        turtle_circle(float(sys.argv[1]), float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass
