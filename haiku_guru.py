NAOQI_PYTHON_PATH = "/home/avnerus/Apps/NAO/pynaoqi-python2.7-2.1.4.13-linux64"

import sys
import json
import time

if not NAOQI_PYTHON_PATH in sys.path:
    print("Appending path: %s" % NAOQI_PYTHON_PATH)
    sys.path.append(NAOQI_PYTHON_PATH)


with open('haikus.json') as data_file:    
    data = json.load(data_file)


from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

#tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)

class HaikuGuru(ALModule):
    
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.tts = ALProxy("ALTextToSpeech")
        
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("ALTextToSpeech/TextDone",
            "haiku_guru",
            "on_tts_text_done")
        
    def on_tts_text_done(self, name, value):
        """ callback for event  """
        print "TTS Text Done!! value:", value

def main():

    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       "127.0.0.1",         # parent broker IP
       9559)       # parent broker port

    global haiku_guru
    haiku_guru = HaikuGuru("haiku_guru")   


    try:
        while True:
            time.sleep(1)
            haiku_guru.tts.say("Hello!")

    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    main()
