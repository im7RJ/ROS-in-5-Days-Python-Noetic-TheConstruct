#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

var = Twist()

def callback(msg):

    if msg.ranges[360] > 1:
        var.linear.x = 0.5
        var.angular.z = 0
       
    if msg.ranges[360] < 1:
        var.linear.x = 0
        var.angular.z = 0.5

    if msg.ranges[0] < 1:
        var.linear.x = 0
        var.angular.z = 0.5

    if msg.ranges[719] < 1:
        var.linear.x = 0
        var.angular.z = -0.5  

    pub.publish(var)        


rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
rospy.spin()


    