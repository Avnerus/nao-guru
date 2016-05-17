#! /usr/bin/env python
import roslib
import rospy

import wave

import json
import time
import random

import pyaudio
import math
import numpy as np

from naoqi_bridge_msgs.msg import (
        AudioBuffer
    )


PyAudio = pyaudio.PyAudio
p = PyAudio()

class AudioOutput():
    def __init__(self):
        self.blah = 1
        rospy.init_node('audio_output', anonymous=True)
        rospy.Subscriber("/naoqi_microphone/audio_raw", AudioBuffer, self.handleAudioMessage, queue_size=10)
        rospy.loginfo("Audio Output Running")

        #self.nao_output = wave.open('nao.wav', 'w')
        #self.nao_output.setparams((2, 2, 32000, 1365, 'NONE', 'not compressed'))

        BITRATE = 32000 #number of frames per second/frameset.      
        self.stream = p.open(format = pyaudio.paInt16,
                        channels = 2, 
                        rate = BITRATE, 
                        output = True)

        self.stream.start_stream()

        rospy.spin()

    def handleAudioMessage(self, msg):
        a = np.array(msg.data).tostring()

        #self.nao_output.writeframes(a)

        self.stream.write(a)


if __name__ == '__main__':
    try:
        audio_output = AudioOutput()
        rospy.loginfo("Audio Output Shut down")

        audio_output.stream.stop_stream()
        audio_output.stream.close()
        #audio_output.nao_output.close()

        p.terminate()
    except rospy.ROSInterruptException:
        pass   








