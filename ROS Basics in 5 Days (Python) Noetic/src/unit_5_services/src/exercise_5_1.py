#! /usr/bin/env python

import rospkg
import rospy
# Import the service message used by the service /trajectory_by_name
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
# Create the connection to the service
exec_traj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type ExecTrajRequest
exec_traj_object = ExecTrajRequest()

rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

# Fill the variable exec_traj of this object with the desired value
exec_traj_object.exec_traj = traj
# Send through the connection the name of the trajectory to be executed by the robot
result = exec_traj_service(exec_traj_object)
# Print the result given by the service called
print(result)