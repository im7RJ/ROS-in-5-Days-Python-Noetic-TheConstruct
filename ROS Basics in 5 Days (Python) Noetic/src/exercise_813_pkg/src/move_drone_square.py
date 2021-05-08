#! /usr/bin/env python

import rospy
import time
import actionlib
from actionlib.msg import TestFeedback, TestResult, TestAction
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class move_square(object):
       
    _feedback = TestFeedback()
    _result   = TestResult()

    def __init__(self):
        
        self._as = actionlib.SimpleActionServer("move_drone_square_as", TestAction, self.goal_callback, False)
        self._as.start()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)

    def publish_once_in_cmd_vel(self, cmd):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.pub.get_num_connections()
            if connections > 0:
                self.pub.publish(cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()    

    def turn_drone(self):

        self.cmd.linear.x = 0
        self.cmd.angular.z = 1
        self.publish_once_in_cmd_vel(self.cmd)
        rospy.loginfo("Drone is turning")

    def move_forward_drone(self):

        self.cmd.linear.x = 1
        self.cmd.angular.z = 0
        self.publish_once_in_cmd_vel(self.cmd)
        rospy.loginfo("Drone is moving forward")

    def stop_drone(self):

        self.cmd.linear.x = 0
        self.cmd.angular.z = 0
        self.publish_once_in_cmd_vel(self.cmd)
        rospy.loginfo("Drone is stopping")    


    def goal_callback(self, goal):   

        r = rospy.Rate(1)
        success = True
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.cmd = Twist()
        self.takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self.takeoff_msg = Empty()
        self.land = rospy.Publisher('/drone/land', Empty, queue_size=1) 
        self.land_msg = Empty()
        
        i = 0
        while not i == 3:
            self.takeoff.publish(self.takeoff_msg)
            rospy.loginfo("Drone has taken-off...")
            time.sleep(1)
            i += 1

        side_traj_seconds = goal.goal
        turn_seconds = 1.8
        
        i = 0
        for i in range(0, 4):

            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                # the following line, sets the client in preempted state (goal cancelled)
                self._as.set_preempted()
                success = False
                # we end the calculation of the Fibonacci sequence
                break
            
            self.move_forward_drone()
            time.sleep(side_traj_seconds)
            self.turn_drone()
            time.sleep(turn_seconds)

            self._feedback.feedback = i + 1
            self._as.publish_feedback(self._feedback)
            r.sleep()

        if success:
            self._result.result = (side_traj_seconds*4) + (turn_seconds*4)
            rospy.loginfo('The total seconds it took the drone to perform the square was %i' % self._result.result )
            self._as.set_succeeded(self._result)
            
            self.stop_drone()
            i = 0
            while not i == 3:
                self.land.publish(self.land_msg)
                rospy.loginfo("Drone is landing...")
                time.sleep(1)
                i += 1

if __name__ == '__main__':
    rospy.init_node('move_square')        
    move_square()
    rospy.spin()     





