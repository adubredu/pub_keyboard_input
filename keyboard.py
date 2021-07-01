import rospy
from std_msgs.msg import String

if __name__ == "__main__":
	rospy.init_node("gripper_node")
	pub = rospy.Publisher("/keyboard_input", String, queue_size=1)

	while not rospy.is_shutdown():
		value = raw_input("Input: ") 
		msg = String()
		msg.data = value
		pub.publish(msg)



