#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan

class Laser_Reader(object):

    def __init__(self):
        self.sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.callback)
        self.laserdata = LaserScan()
        self.front = 0.0
        self.right = 0.0
        self.left = 0.0
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

    def callback(self, msg):
        self.laserdata = msg
        rospy.logdebug(self.laserdata) 

    def get_laserdata(self):

         return self.laserdata  

    def crash_detector(self):
        
        self.front = self.laserdata.ranges[360]
        self.right = self.laserdata.ranges[0]
        self.left = self.laserdata.ranges[719]
        rospy.loginfo("Front Distance == "+str(self.front))
        rospy.loginfo("Left Distance == "+str(self.left))
        rospy.loginfo("Right Distance == "+str(self.right))
        
        
        return self.convert_to_dict()  

    def convert_to_dict(self):
        """
        Converts the fiven message to a dictionary telling in which direction there is a detection
        """
        detect_dict = {}
        # We consider that when there is a big Z axis component there has been a very big front crash
        detection_dict = {"front":self.front,
                          "left":self.left,
                          "right":self.right}
        return detection_dict       

if __name__ == '__main__':
    rospy.init_node('laser_subscriber', log_level=rospy.INFO)
    laserreader_object = Laser_Reader()
    time.sleep(2)
    rate = rospy.Rate(0.5)
    
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True 

    rospy.on_shutdown(shutdownhook)

    while not ctrl_c:
        data = laserreader_object.get_laserdata()
        laserreader_object.crash_detector()
        rospy.loginfo(data)
        rate.sleep()     
