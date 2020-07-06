import rospy
from std_msgs.msg import Empty
rospy.init_node('flydistanceland')
pub_takeoff=rospy.Publisher('/drone/takeoff',Empty,queue_size=1)
var_empty=Empty()
pub_takeoff.publish(var_empty)

#code for land 
pub_land=rospy.Publisher('/drone/land',Empty,queue_size=1)
var_empty=Empty()
pub_land.publish(var_empty)
