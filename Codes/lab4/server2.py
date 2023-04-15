#!/usr/bin/env python3
import rospy
from std_srvs.srv import Trigger, TriggerResponse

def handle_append_strings(req):
    string1 = "Hello"
    string2 = "World"
    response = TriggerResponse()
    response.success = True
    response.message = string1 + " " + string2
    return response

if __name__ == "__main__":
    rospy.init_node("append_strings_server")
    rospy.loginfo("Strings Append Server Node Is Created")
    service = rospy.Service("append_strings", Trigger, handle_append_strings)
    rospy.spin()
