from cv2 import cv2
import os


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            images.append(os.path.join(folder, filename))
    return images

