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
    )

if __name__ == '__main__':
    rospy.init_node('ros_talker')
    client = actionlib.SimpleActionClient('speech_action', SpeechWithFeedbackAction)
    client.wait_for_server()
    print("Speech action server ready!")

    while True:
        text = raw_input('--> ');
        goal = SpeechWithFeedbackGoal(say=text)
        client.send_goal(goal)
        client.wait_for_result()
        print("Done");
    

