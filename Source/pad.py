import numpy as np
import sys
import cv2
import os
import matplotlib.pyplot as plt

PATH = './dataset/test50/'
OUTPATH = './dataset/test50_bg/'
SIZE = 64
COLOR = (0, 0, 0)

if not os.path.exists(OUTPATH):
    os.makedirs(OUTPATH)

for img_path in os.listdir(PATH):
    img = cv2.imread(PATH + img_path)
    height, width, channels = img.shape

    new_width = width + SIZE * 2
    new_height = height + SIZE * 2
    result = np.full((new_height, new_width, channels), COLOR, dtype=np.uint8)

    result[SIZE:height+SIZE, SIZE:width+SIZE] = img
    
    cv2.imwrite(OUTPATH + img_path, result)