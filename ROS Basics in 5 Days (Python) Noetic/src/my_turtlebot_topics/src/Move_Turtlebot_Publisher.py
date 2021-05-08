#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Move_Turtlebot(object):

    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.move = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1) # 10hz
        rospy.on_shutdown(self.shutdownhook)
    
    def publish_once_in_cmd_vel(self):

        while not self.ctrl_c:
            connections = self.cmd_vel_pub.get_num_connections()
            if connections > 0:
                self.cmd_vel_pub.publish(self.move)
                rospy.loginfo('Cmd_Published')
                break
            else:
                self.rate.sleep()   
    
             
    def Move_Robot(self,direction):
        if direction == 'forward':
            self.move.linear.x = 0.5
            self.move.angular.z = 0
        elif direction == 'right':
            self.move.linear.x = 0
            self.move.angular.z = 0.5
        elif direction == 'backward':
            self.move.linear.x = -0.5
            self.move.angular.z = 0
        elif direction == 'left':
            self.move.linear.x = 0
            self.move.angular.z = -0.5
        elif direction == 'stop':
            self.move.linear.x = 0
            self.move.angular.z = 0    

        self.publish_once_in_cmd_vel()        

if __name__ == '__main__':
    rospy.init_node('move_turtlebot', anonymous=True)
    moveturtlebot_object = Move_Turtlebot()
    try:
        moveturtlebot_object.Move_Robot(direction = 'forward')
    except rospy.ROSInterruptException:
        pass

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True  
        moveturtlebot_object.Move_Robot(direction = 'stop')

