# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:54:03 2020

@author: sayya
"""

from keras.preprocessing.image import load_img,array_to_img,ImageDataGenerator
from keras.applications.inception_v3 import preprocess_input
import numoy as np

train_datagen=ImageDataGenerator(
        preprocessing_function=preprocess_input,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
        )


train_datagen=ImageDataGenerator(
        preprocessing_function=preprocess_input,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
        )


jf_datagen=ImageDataGenerator(
        preprocessing_function=preprocess_input,
        horizontal_flip=True
        
        )

train_generator = train_datagen.flow_from_directory('images/sample-train/',target_size=(150,150), save_to_dir='images/sample-confirm/')


i=0
for batch in train_datagen.flow_from_directory('images/sample-train/', target_size=(150,150), save_to_dir='images/sample-confirm/'):
    i+=1
    if (i>10):
        break
    
j=0
for batch in jf_datagen.flow_from_directory('images/sample-train/', target_size=(150,150), save_to_dir='images/sample-confirm/'):
    j+=1
    if ( j > 10):
        break 