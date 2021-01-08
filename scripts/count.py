#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
if __name__ == '__main__':
    rospy.init_node('count',anonymous=True) # ノード名「count」に設定
    pub = rospy.Publisher('count_up', String, queue_size=1) # パブリッシャ「count_up」を作成
    rate = rospy.Rate(10) # 10Hzで実行 n = 0
while not rospy.is_shutdown():
    rospy.loginfo("えんちゃん：0匹")
    str = "現在時刻 %s"%rospy.get_time()
    pub.publish(str)
    rate.sleep()
