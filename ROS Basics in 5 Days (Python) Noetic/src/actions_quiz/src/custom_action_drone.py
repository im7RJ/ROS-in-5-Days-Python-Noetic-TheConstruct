#! /usr/bin/env python

import rospy
import time
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult

class CustomActionDroneClass(object):

    _feedback = CustomActionMsgFeedback()
    _result = CustomActionMsgResult()

    def __init__(self):

        self._as = actionlib.SimpleActionServer("move_drone_custom_as", CustomActionMsgAction, self.goal_callback, False)
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

    def goal_callback(self, goal):   

        r = rospy.Rate(1)
        success = True
        
        self.takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self.takeoff_msg = Empty()
        self.land = rospy.Publisher('/drone/land', Empty, queue_size=1) 
        self.land_msg = Empty()
        
        traj = goal.goal
        i = 0

        for i in range(0,4):
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                # the following line, sets the client in preempted state (goal cancelled)
                self._as.set_preempted()
                success = False
                # we end the calculation of the Fibonacci sequence
           
            if traj == 'TAKEOFF':
                self.takeoff.publish(self.takeoff_msg)
                self._feedback.feedback = "Taking Off"
                self._as.publish_feedback(self._feedback)
                time.sleep(1)

            if traj == 'LAND':
                self.land.publish(self.land_msg)
                self._feedback.feedback = "Landing..."
                self._as.publish_feedback(self._feedback)
                time.sleep(1)
            
            
            r.sleep()    

        if success:
            self._result = Empty()
            self._as.set_succeeded(self._result)            

if __name__ == '__main__':
    rospy.init_node('custom_action_drone')
    CustomActionDroneClass()
    rospy.spin()


  