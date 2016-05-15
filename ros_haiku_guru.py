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
    SpeechWithFeedbackAction )

if __name__ == '__main__':
    rospy.init_node('ros_haiku_guru')
    client = actionlib.SimpleActionClient('speech_action', SpeechWithFeedbackAction)
    client.wait_for_server()
    print("Action server ready!")
    
    # Say something
    with open('haikus.json') as data_file:    
        data = json.load(data_file)

    haiku = random.choice(data["haikus"])
    lines = haiku["lines"]

    print(lines[0])
    goal = SpeechWithFeedbackGoal(say=lines[0])
    client.send_goal(goal)
    client.wait_for_result()
    
    time.sleep(1)

    print(lines[1])
    goal = SpeechWithFeedbackGoal(say=lines[1])
    client.send_goal(goal)
    client.wait_for_result()
    time.sleep(2)


    print(lines[2])
    goal = SpeechWithFeedbackGoal(say=lines[2])
    client.send_goal(goal)
    client.wait_for_result()

