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
