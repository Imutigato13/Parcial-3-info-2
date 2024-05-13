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

    def set_archivos(self, archivos):
        self.__archivos.append(archivos)

    def get_archivos(self):
        return self.__archivos

    def extraer_archivos(self, ruta):
        archivos = os.listdir(ruta)
        for archivo in archivos:
            if archivo.endswith('.dcm'): 
                ruta_dicom = os.path.join(ruta, archivo)
                dicom = pydicom.dcmread(ruta_dicom) 
                self.__archivos.append(dicom)

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
    
    def ingresar_imagen(self, ruta):
        imagen = cv2.imread(ruta)
        self.__archivos.append(imagen)
    
    def rotar_imagen(self,dic,id):
        if id in dic:
                archivos = dic[id]
                dicom = archivos.get_archivos()
                posicion = int(input(f"Cual es la imagen que decea transformar del paciente, escoja etre 0 y {len(dicom)-1}: "))
                if 0 <= posicion <= (len(dicom)-1):
                    imagen = dicom[posicion].pixel_array
                    while True:
                        theta = int(input("Ingrese el angulo de rotacion(90°,180°,270°): "))
                        if theta == 90 or theta == 180 or theta == 270:
                            imagen = imagen.astype(np.uint8)
                            imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
                            row,col,chn = np.shape(imagen)
                            MR = cv2.getRotationMatrix2D((col/2,row/2),theta,1)
                            rotacion = cv2.warpAffine(imagen,MR,(col,row))
                            precont_2 = 0
                            for filename in os.listdir(r'D:\Programas Py\Informatica 2\Parcial 3 info 2\Rotaciones'):
                                if filename.endswith('.JPG'):
                                    subcont_2 = int(filename.split(".")[0].split("_")[-1])
                                    if precont_2 < subcont_2:
                                        precont_2 = subcont_2
                                    elif precont_2 >= subcont_2:
                                        cont_2 = precont_2
                            cont_2 = precont_2
                            cont_2 +=1 #HACER FUNCION
                            cv2.imwrite(f'D:\Programas Py\Informatica 2\Parcial 3 info 2\Rotaciones\Rotacion_{cont_2}.JPG',rotacion)
                            plt.subplot(1, 2, 1)
                            plt.imshow(rotacion)
                            plt.title("Imagen rotada")
                            plt.axis('off')
                            plt.subplot(1, 2, 2)
                            plt.imshow(imagen)
                            plt.title("Imagen original")
                            plt.axis('off')
                            plt.show()
                            print('')
                            break
                        else:
                            print("Angulo no valido")
                else:
                    print("Posicion no valida")
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