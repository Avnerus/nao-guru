#! /usr/bin/env python
import roslib
import rospy

import json
import time
import random

from naoqi_bridge_msgs.msg import (
        AudioBuffer
    )


class AudioOutput():
    def __init__(self):
        rospy.init_node('audio_output', anonymous=True)
        rospy.Subscriber("/naoqi_microphone/audio_raw", AudioBuffer, self.handleAudioMessage, queue_size=10)
        rospy.loginfo("Audio Output Running")

        rospy.spin()

    def handleAudioMessage(self, msg):
        rospy.loginfo("Audio message!")


if __name__ == '__main__':
    try:
        audio_output = AudioOutput()
        rospy.loginfo("Audio Output")
    except rospy.ROSInterruptException:
        pass   

