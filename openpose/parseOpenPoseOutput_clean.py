import json
import os

import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")



# from google.colab import drive
# drive.mount('/content/gdrive')
# os.chdir('/content/gdrive/MyDrive/Gait Analysis/normal_walk_output.json/')

BODY_PARTS= {
0:  "Nose",
1:  "Neck",
2:  "RShoulder",
3:  "RElbow",
4:  "RWrist",
5:  "LShoulder",
6:  "LElbow",
7:  "LWrist",
8:  "MidHip",
9:  "RHip",
10: "RKnee",
11: "RAnkle",
12: "LHip",
13: "LKnee",
14: "LAnkle",
15: "REye",
16: "LEye",
17: "REar",
18: "LEar",
19: "LBigToe",
20: "LSmallToe",
21: "LHeel",
22: "RBigToe",
23: "RSmallToe",
24: "RHeel",
25: "Background"
 }

i=0
zero_str='00'
path_str='../output_jsons/normal_walk_output.json/'+'normal_walk_000000000'+zero_str+str(i)+'_keypoints.json'
isFile = os.path.isfile(path_str)
body_part_x={k:[] for k in range(0,26)}
body_part_y={k:[] for k in range(0,26)}

while(os.path.isfile(path_str)):
    print("enter loop")
    if(i<9):
        zero_str='00'
    elif(i>=9 and i<99):
        zero_str='0'
    elif(i>=99):
        zero_str=''
    i+=1
    f = open(path_str)
    path_str='../output_jsons/normal_walk_output.json/'+'normal_walk_000000000'+zero_str+str(i)+'_keypoints.json'

    data = json.load(f)
    person_1=data['people']
    keypoints=person_1[0]['pose_keypoints_2d']
    k=0
    j=0
    while k< len(keypoints)-1:
#         print("enter inner loop")
        x=keypoints[k+0]
        y=keypoints[k+1]
        confidence=keypoints[k+2]
        # print("Body Part: "+BODY_PARTS[j])
        # print("x-> "+str(x)+", y-> "+str(y)+", confidence->"+str(confidence))
        body_part_x[j].append(x)
        body_part_y[j].append(y)
        k+=3
        j+=1

    print(path_str)

body_part_x

# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # toes dont have proper accuracy so we only take in heel
# keypoint=0
# for keypoint in [24,22,23,21,19,20]:
#   x=body_part_x[keypoint]
#   y=body_part_y[keypoint]
#   plt.title(BODY_PARTS[keypoint])
#   plt.plot(x, y)
#   plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# toes dont have proper accuracy so we only take in heel
keypoint=0
for keypoint in [24,21]:
  x=body_part_x[keypoint]
  y=body_part_y[keypoint]
  plt.title(BODY_PARTS[keypoint])
  plt.plot(x, y)
  plt.show()

y_=np.arange(128)
y_

import matplotlib.pyplot as plt
import numpy as np
import peakutils

# define data values
x1 = body_part_y[24]   # X-axis points
x2 = body_part_y[21]  
y=y_  # Y-axis points
# f = plt.figure()
# f.set_figwidth(10)
# f.set_figheight(10)
negx1 = [ -x for x in x1]
index1 = peakutils.indexes(negx1,thres=0.7,min_dist=1)
negx2 = [ -x for x in x2]
index2 = peakutils.indexes(negx2,thres=0.7,min_dist=1)
print(index1)
plt.figure(figsize=(10,10))
plt.plot(x1, y, label = "line 1") # yellow left leg
plt.plot(x2, y, label = "line 2")  # blue right leg
frames_left_leg=[]
frames_right_leg=[]
for ind in index1:
    plt.plot(x1[ind],y[ind], marker="o", ls="", ms=10 )
    frames_left_leg.append(y[ind])
    
for ind in index2:
    plt.plot(x2[ind],y[ind], marker="o", ls="", ms=10 )
    frames_right_leg.append(y[ind])

frames_left_leg

frames_right_leg



