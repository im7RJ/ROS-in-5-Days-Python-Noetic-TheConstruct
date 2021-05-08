#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('service_client')
rospy.wait_for_service('/move_bb8_in_circle')
move_bb8_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
move_bb8_object = EmptyRequest()

result = move_bb8_service(move_bb8_object)
print(result)

