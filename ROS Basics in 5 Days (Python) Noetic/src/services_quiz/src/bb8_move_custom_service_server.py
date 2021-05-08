#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been entered")
    print("Request Data ==> side = "+str(request.side))
    print("Request Data ==> repetitions = "+str(request.repetitions))
    i = 0
    j = 0
    k = 0
    l = 0

    while k <= (request.repetitions):  
        
        while j <= 3:      
            
            while i <= 2:
                var.linear.x = 0
                var.angular.z = 0.5
                pub.publish(var)
                rate.sleep()
                i += 1

            while l <= request.side:
                var.linear.x = 0.5
                var.angular.z = 0
                pub.publish(var)
                rate.sleep()
                l += 1
            
            i = 0
            l = 0
            j += 1
        
        j = 0
        k += 1            

    k = 0
    var.linear.x = 0
    var.angular.z = 0
    pub.publish(var)
    print("Duration of Motion has ended")

    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
var = Twist()
rate = rospy.Rate(1)
print("Service Ready")
rospy.spin()


            
