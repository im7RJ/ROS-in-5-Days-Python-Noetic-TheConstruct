#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
    var.linear.x = 0.5
    var.angular.z = 0.5
    pub.publish(var)
    return EmptyResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('service_server') 
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called move_bb8_in_circle with the defined callback
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
var = Twist()
rospy.spin() # mantain the service open.