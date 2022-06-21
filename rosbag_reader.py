#!/usr/bin/env python
from asyncore import file_dispatcher
from unicodedata import name
import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import argparse
import tempfile
import sys
import rospy
import soundfile as sf
from sounddevice_ros.msg import AudioInfo, AudioData

#######################################
# Read Rosbag files for audio and generate wav file
# input: rosbag name
# output: wav file
#######################################


bag = bagreader('/home/marklee/rosbag/ambient.bag')

# print(bag.topic_table)

topic_audio_info = bag.message_by_topic('/audio_info')
topic_audio = bag.message_by_topic('/audio')

# print(topic_audio_info)

df_audio_info = pd.read_csv(topic_audio_info)
print(df_audio_info[0])