from cv2 import cv2
import os

images= []
def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
folder=r'C:\Users\mohan\OneDrive\Desktop\Images'
load_images_from_folder(folder)

#This code is working. Change the directory in line11.