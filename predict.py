#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

"""
import urllib.request
import numpy as np
from keras.models import load_model
from keras.preprocessing import image


#from tensorflow.keras.preprocessing.image import img_to_array
#from tensorflow.keras.models import load_model

class dogcat:
    def __init__(self,filename):
        self.filename =filename
    
    def load_model():
        if not os.path.isfile('model.h5'):
            urllib.request.urlretrieve('https://github.com/tabrejml/fb/blob/main/Model.h5', 'Model.h5')
        return tensorflow.keras.models.load_model('Model.h5')

    def predictiondogcat(self):
        # load model
        model = load_model(r'Model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (135, 135,3))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        print(result[0][0])

        if result[0][0] == 1:
            prediction = 'NonFibrosis'
            return [{ "image" : prediction}]
        else:
            prediction = 'Fibrosis'
            return [{ "image" : prediction}]


