#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest 

rospy.init_node('service_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
bb8_move_custom_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
bb8_move_custom_object = BB8CustomServiceMessageRequest()

i = 1

while i <= 2:

    bb8_move_custom_object.side = 2*i
    bb8_move_custom_object.repetitions = 0
    i += 1
    result = bb8_move_custom_service(bb8_move_custom_object)
    print(result)