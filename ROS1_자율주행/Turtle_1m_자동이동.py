#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def drive_forward():
    rospy.init_node('test_1_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    move_cmd = Twist()
    move_cmd.linear.x = 0.2 
    duration = 5.0         

    rate = rospy.Rate(10)  
    start_time = rospy.Time.now().to_sec()

    rospy.loginfo("TurtleBot3 자동 주행")

    while not rospy.is_shutdown():
        current_time = rospy.Time.now().to_sec()
        if current_time - start_time < duration:
            pub.publish(move_cmd)
        else:
            pub.publish(Twist()) 
            rospy.loginfo(" 주행 완료")
            break
        rate.sleep()

if __name__ == '__main__':
    try:
        drive_forward()
    except rospy.ROSInterruptException:
        pass
