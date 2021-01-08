#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def cb(message):
    rospy.loginfo(rospy.get_caller_id())
    rospy.loginfo("データ： %s",message.data)
    rospy.loginfo("えんちゃん %s 匹",rospy.get_caller_id())

if __name__ == '__main__':
    rospy.init_node('100')
    sub = rospy.Subscriber('count_up', String, cb)
    rospy.spin()
