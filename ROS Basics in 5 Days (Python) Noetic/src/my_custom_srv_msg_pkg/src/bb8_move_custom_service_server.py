#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been entered")
    print("Request Data ==> duration = "+str(request.duration))
    i = 0
        
    while i <= request.duration:
            var.linear.x = 0.5
            var.angular.z = 0.5
            pub.publish(var)
            rate.sleep()
            i += 1

    var.linear.x = 0
    var.angular.z = 0
    pub.publish(var)
    print("Duration of Motion has ended")

    response = MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, my_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
var = Twist()
rate = rospy.Rate(1)
print("Service Ready")
rospy.spin()


            
