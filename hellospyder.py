# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:14:31 2018

@author: Hank2
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, strides=2, padding='same', activation='relu', input_shape=(128, 128, 3)))
model.summary()