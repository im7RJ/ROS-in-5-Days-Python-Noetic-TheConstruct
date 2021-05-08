#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

class Odom_Reader(object):

    def __init__(self):
        self.sub = rospy.Subscriber('/odom', Odometry, self.callback)
        self.Odomdata = Odometry()
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

    def check_odom_ready(self):
        self.odomdata = None
        while self.odomdata is None and not rospy.is_shutdown():
            try:
                self.odomdata = rospy.wait_for_message('/odom', Odometry, timeout=1.0)
                rospy.logdebug("Current "+'/odom'+" READY=>" + str(self.odomdata))

            except:
                rospy.logerr("Current "+self._topic_name+" not ready yet, retrying for getting "+'/odom'+"")
        
        rospy.loginfo("Initialised Odometry Data="+str(self.odomdata))
        return self.odomdata    

    def callback(self, msg):
        self.odomdata = msg
        rospy.logdebug(self.odomdata)    

    def get_odomdata(self):
        return self.odomdata    

if __name__ == '__main__':
    rospy.init_node('odom_subscriber', log_level=rospy.INFO)
    odomreader_object = Odom_Reader()
    rospy.loginfo(odomreader_object.get_odomdata())
    time.sleep(2)
    rate = rospy.Rate(0.5)
    
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True 

    rospy.on_shutdown(shutdownhook)

    while not ctrl_c:
        data = odomreader_object.get_odomdata()
        rospy.loginfo(data)
        rate.sleep()     
