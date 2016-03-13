from client import Client
from recognition_parser import parse_data
from recognition_parser import buckets_to_chars
from recognition_parser import reduce_data
from recognition_parser import guess_seq_len
from recognition_parser import get_patterns
from recognition_parser import count_signs
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import pickle
powerValue = 500

class Segment(object):
    def __init__(self, turns, typ):
        self.explor_turns = turns
        self.seg_type = typ
        self.time_spent = 0
        self.a = -1
    def get_val(self, it):
        return a*x*(x-turns)*it + 130

class MsgHandler(object):
    def __init__(self):
        self.list_lap_gyroz = list()
        self.filtered_data = list()
        self.buckets_data = list()
        self.reduced = list()
        self.time1 = 0
        self.time2 = 0
        self.exploration_time = 10000
        self.started = False
        self.exploration = True
        self.segmenty = list()
        self.client = Client("Hairy Harries")
        self.client.onRaceStart(self.onRaceStart)
        self.client.onVelocity(self.onVelocity)
        self.client.onSensor(self.onRaceStart)
        self.client.onPenalty(self.onPenalty)
        self.client.onRoundPassed(self.onRoundPassed)
        self.client.onRaceStop(self.onRaceStop)
        self.client.connect("localhost")
        self.client.announce()

    def receive(self, msg):
#        print 'received' + str(msg)
        pass

    def onRaceStart(self, msg):
        self.started = True
        self.exploration_run(msg)
        self.receive(msg)
        if u'g' in msg:
            data = msg[u'g'][2]
            self.list_lap_gyroz.append(data)
        else: 
            pass

    def onVelocity(self, msg):
        self.receive(msg)
        self.filtered_data = savgol_filter(self.list_lap_gyroz, 7,5, mode='constant')
        self.buckets_data += parse_data(self.filtered_data, buckets=8)
        tmp = buckets_to_chars(self.buckets_data)
        count = count_signs(tmp)
        self.reduced = reduce_data(tmp)
        print '-----------'
        print 'sequence: ' + self.reduced
        print 'patterns: '
        patterns = get_patterns(self.reduced)
        print patterns
        plt.close()
        plt.plot(self.buckets_data)
        plt.show()

        for typ, volume in zip(self.reduced, count):
            self.segmenty.append(Segment(volume,typ))
        
        self.list_lap_gyroz = list()
        if not self.exploration:
            patterns = get_patterns(self.reduced)
            size = len(patterns.keys()[0])
            actual_pattern = self.reduced[-size:]
            if actual_pattern in patterns:
                pass

    def onSensor(self, msg):
        self.receive(msg)

    def onPenalty(self, msg):
        self.receive(msg)

    def onRoundPassed(self, msg):
        self.receive(msg)

    def onRaceStop(self, msg):
        pass

    def exploration_run(self, msg):
        if not self.exploration:
            return 
        self.client.powerControl(120)
        if u'timeStamp' in msg and self.started and not self.time1:
            self.time1 = msg[u'timeStamp']
            print 'Exploring for ' + str(self.exploration_time) + ' milisec.'
            return 
        else:
            pass
        if u'timeStamp' in msg and self.started:
            self.time2 = msg[u'timeStamp']
            if self.time2 - self.time1 > self.exploration_time:
                print 'Exploration ended'
                self.exploration = False

handler = MsgHandler()




