#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
enc_data=""

def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

def callback_receive_radio_data(msg):
    global enc_data
    rospy.loginfo("----"*8)
    rospy.loginfo(msg)
    rospy.loginfo("KEY=3")
    enc_data=encrypt_text(msg.data,3)
    rospy.loginfo("encrypted data: "+ enc_data)

if __name__ == '__main__':
    rospy.init_node('subscriber_publisher')
    sub = rospy.Subscriber("/robot_publisher_node", String, callback_receive_radio_data)
    pub = rospy.Publisher("/robot_publisher_node_2",String, queue_size=10)
    # global enc_data
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        msg = String()
        msg.data = enc_data
        pub.publish(msg)
        rate.sleep()
    rospy.spin()