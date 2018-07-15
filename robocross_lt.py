#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
import tf2_ros
import tf2_geometry_msgs


# TF2 stuff
tf_broadcaster = tf2_ros.TransformBroadcaster()
static_tf_broadcaster = tf2_ros.StaticTransformBroadcaster()

tf_buffer = tf2_ros.Buffer()
tf_listener = tf2_ros.TransformListener(tf_buffer)

rospy.init_node('robocross_lt')
print 'Initialized robocross lt'


lt_pub = rospy.Publisher('/mavros/landing_target/send', PoseStamped, queue_size=1)
ps = PoseStamped()
ps.pose.orientation.w = 1
ps.header.frame_id = 'shar'


def pose_update(pose):
    p = tf_buffer.transform(ps, 'local_origin', rospy.Duration(0.1))
    # p.pose.position.y += 0.34
    # p.pose.position.x += 0.04
    lt_pub.publish(p)


rospy.Subscriber('/aruco_pose/pose', PoseStamped, pose_update)


rospy.spin()
