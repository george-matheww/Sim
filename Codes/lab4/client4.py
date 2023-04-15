#!/usr/bin/env python3
import rospy
import sys
from std_srvs.srv import Trigger, TriggerRequest

def append_strings_client(string1, string2):
    rospy.wait_for_service("append_strings")
    try:
        append_strings = rospy.ServiceProxy("append_strings", Trigger)
        response = append_strings(TriggerRequest())
        return string1 + " " + string2
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    result = append_strings_client(string1, string2)
    print(result)
