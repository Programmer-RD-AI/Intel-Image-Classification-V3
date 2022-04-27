import torch
import os
import cv2
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


import torchvision


from torchvision import transforms


transformation_data = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ToTensor()
])


img = cv2.imread('./data/buildings/0.jpg')


from PIL import Image
img_pil_image = Image.fromarray(img)
transformation_data(img_pil_image)


def load_image(data_dir="./data/"):
    labels = {}
    labels_r = {}
    idx = -1
    data = []
    for label in os.listdir(data_dir):
        idx += 1
        labels[label] = idx
        labels_r[idx] = label
    for directory in os.listdir(data_dir):
        for file_dir in os.listdir(data_dir + directory):
            img = cv2.imread('./data/
