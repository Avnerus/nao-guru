#! /usr/bin/env python

import roslib
import rospy
import actionlib

import json
import time
import random

from naoqi_bridge_msgs.msg import (
    SpeechWithFeedbackGoal,
    SpeechWithFeedbackResult,
    SpeechWithFeedbackFeedback,
    SpeechWithFeedbackAction,
    JointAnglesWithSpeedGoal,
    JointAnglesWithSpeedAction
    )

if __name__ == '__main__':
    rospy.init_node('ros_haiku_guru')
    client = actionlib.SimpleActionClient('speech_action', SpeechWithFeedbackAction)
    client.wait_for_server()
    print("Speech action server ready!")

    joint_client = actionlib.SimpleActionClient('joint_angles_action', JointAnglesWithSpeedAction)
    joint_client.wait_for_server()
    print("Joint action server ready!")
    
    # Say something
    with open('haikus.json') as data_file:    
        data = json.load(data_file)

    haiku = random.choice(data["haikus"])
    lines = haiku["lines"]

    print(lines[0])
    goal = SpeechWithFeedbackGoal(say=lines[0])
    client.send_goal(goal)
    joint_goal = JointAnglesWithSpeedGoal()
    joint_goal.joint_angles.joint_names = ['HeadYaw']
    joint_goal.joint_angles.joint_angles = [0.5]
    joint_goal.joint_angles.speed = 0.2
    joint_client.send_goal(joint_goal)

    client.wait_for_result()
    
    time.sleep(1)

    print(lines[1])
    goal = SpeechWithFeedbackGoal(say=lines[1])
    client.send_goal(goal)
    joint_goal = JointAnglesWithSpeedGoal()
    joint_goal.joint_angles.joint_names = ['HeadYaw']
    joint_goal.joint_angles.joint_angles = [-0.5]
    joint_goal.joint_angles.speed = 0.2
    joint_client.send_goal(joint_goal)
    client.wait_for_result()
    time.sleep(2)


    print(lines[2])
    goal = SpeechWithFeedbackGoal(say=lines[2])
    client.send_goal(goal)
    joint_goal = JointAnglesWithSpeedGoal()
    joint_goal.joint_angles.joint_names = ['HeadYaw']
    joint_goal.joint_angles.joint_angles = [0]
    joint_goal.joint_angles.speed = 0.5
    joint_client.send_goal(joint_goal)
    client.wait_for_result()

