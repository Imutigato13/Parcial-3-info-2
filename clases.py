import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pydicom
import dicom2nifti
import nilearn
import nilearn.plotting
import random
class archivador:

    def __init__(self):
        self.__archivos = []

    def extraer_archivos(self, ruta):
        archivos = os.listdir(ruta)
        for archivo in archivos:
            if archivo.endswith('.dcm'): 
                ruta_dicom = os.path.join(ruta, archivo)
                dicom = pydicom.dcmread(ruta_dicom) 
                self.__archivos.append(dicom)
        return self.__archivos
    def datos_paciente(self):
        nombre = self.__archivos[0].PatientName
        id = self.__archivos[0].PatientID
        try:
            edad = self.__archivos[0][ 0x0010 , 0x1010 ].value
        except:
            edad = 'No disponible'
        return nombre, id, edad

    def extraer_imagen(self,ruta_dicom):
        precont = 0
        for filename in os.listdir(r'D:\Programas Py\Informatica 2\Parcial 3 info 2\NIFTI'):
            if filename.startswith('NIFTI'):
                subcont = int(filename.split("_")[-1])
                if precont < subcont:
                    precont = subcont
                elif precont >= subcont:
                    cont = precont
        cont = precont
        cont +=1
        ruta_NIFTI = r'D:\Programas Py\Informatica 2\Parcial 3 info 2\NIFTI\NIFTI' + f'_{cont}' 
        os.makedirs(ruta_NIFTI, exist_ok=True)
        dicom2nifti.convert_directory(ruta_dicom,ruta_NIFTI)
        conversion_NIFTI = os.listdir(ruta_NIFTI)
        ruta_imagen = os.path.join(ruta_NIFTI, conversion_NIFTI[0])
        imagen = nilearn.image.load_img(ruta_imagen)
        return imagen
class Paciente():

    def __init__(self, nombre, edad, id):
        self.__nombre = nombre
        self.__edad = edad
        self.__id = id
        self.__imagen = ''
        

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_id(self):
        return self.__id
    def get_imagen(self):    
        return self.__imagen
    
    def set_imagenes(self, imagen):
        self.__imagen = imagen