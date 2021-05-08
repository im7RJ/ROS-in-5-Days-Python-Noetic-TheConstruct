#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('service_client')
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_duraN_service = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)
move_bb8_duraN_object = MyCustomServiceMessageRequest()

move_bb8_duraN_object.duration = 5

result = move_bb8_duraN_service(move_bb8_duraN_object)
print(str(result))