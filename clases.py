import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pydicom

class sistema:

    def __init__(self):
        self.__archivo = ''
class Paciente(sistema):

    def __init__(self):
        super().__init__()
        self.__nombre = ''
        self.__edad = 0
        self.__id = 0
        self.__imagen = ''

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_id(self):
        return self.__id
    def get_imagen(self):    
        return self.__imagen
    