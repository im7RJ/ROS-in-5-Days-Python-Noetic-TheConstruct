#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 


def callback(msg): 
  print (msg.data)

rospy.init_node('src')
pub = rospy.Publisher('/counter', Int32, queue_size=1)
rate = rospy.Rate(2)
count = Int32()
count.data = 0
sub = rospy.Subscriber('/counter', Int32, callback)
rospy.spin()  

while not rospy.is_shutdown(): 
  pub.publish(count)
  count.data += 1
  rate.sleep()


