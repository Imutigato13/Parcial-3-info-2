import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pydicom

dic_data = {}
dic_pac = {}

class Paciente:

    def __init__(self):

        self.__nombre = ''
        self.__edad = ''
        self.__id = ''
        self.__imagen = ''

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_id(self):
        return self.__id
    def get_imagen(self):    
        return self.__imagen
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self, edad):
        self.__edad = edad
    def set_id(self, id):
        self.__id = id
    def set_imagen(self, imagen):
        self.__imagen = imagen