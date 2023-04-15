#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def decrypt(encrypted_message):
        letters="abcdefghijklmnopqrstuvwxyz"
        k = 3
        decrypted_message = ""
        for ch in encrypted_message:
                if ch in letters:
                        position = letters.find(ch)
                        new_pos = (position - k) % 26
                        new_char = letters[new_pos]
                        decrypted_message += new_char
                else:
                        decrypted_message += ch
        return decrypted_message


def callback_receive_radio_data(msg):
        rospy.loginfo(msg)
        enc_data=decrypt(msg.data)
        rospy.loginfo("decrypted: "+ enc_data)

if __name__ == '__main__':
        rospy.init_node('subscriber_2')
        sub = rospy.Subscriber("/robot_publisher_node_2", String, callback_receive_radio_data)
        rate = rospy.Rate(2)
        rospy.spin()