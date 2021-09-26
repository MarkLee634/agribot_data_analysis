# pip install pycryptodomex 
# pip install pycryptodome
# pip install gnupg

#references
#https://gist.github.com/PrieureDeSion/f9e185ec14556e905373c5be72718d6d

import rosbag
import numpy as np
import sys, os
import csv
import yaml
import shutil #for file management, copy file
import pdb

rosbag_path = "/rosbag/"
rosbag_name = ["2021-05-24-16-41-48"]
desired_rostopics = ["/ft_sensor"]
csv_file_name = ["FT_" + rosbag_name[0] + ".csv"]



#open rosbag
bag = rosbag.Bag(rosbag_path+rosbag_name[0]+".bag")
bag_info = yaml.load(bag._get_yaml_info())
print ("Found bag name: ", rosbag_name[0], " with duration: ", bag_info['duration'], " seconds")


#create a new directory
folder = rosbag_name[0]
try:	#else already exists
	os.makedirs(folder)
except:
	pass
# shutil.copyfile(bagName, folder + '/' + bagName)


#access bag topics
bagContents = bag.read_messages()
bagName = bag.filename


#get list of topics from the bag
listOfTopics = []
for topic, msg, t in bagContents:
	if topic not in listOfTopics:
		listOfTopics.append(topic)

#iterate through all topics
for topicName in listOfTopics:
	if topicName == desired_rostopics[0]:
		print("found topic" + topicName)

		#create CSV file
		csv_file_path = folder + '/' + csv_file_name[0]
		csvfile = open(csv_file_path, 'w')
		filewriter = csv.writer(csvfile, delimiter=',')

		for subtopic, msg, t in bag.read_messages(topicName):	# for each instant in time that has data for topicName
			row = []

			row.append([msg.force.x, msg.force.y, msg.force.z, msg.torque.x, msg.torque.y, msg.torque.z])
			#print(row)
			filewriter.writerow(row)

bag.close()
print ("============= Parsed data. Saved as: ", csv_file_name[0], "============= ")

