from clases import *

ruta = r'D:\Programas Py\Informatica 2\Parcial 3 info 2\datos\T2'

carpeta = archivador()
carpeta.extraer_archivos(ruta)
nombre, id, edad = carpeta.datos_paciente()
paciente = Paciente(nombre, edad, id)
cont,imagenes = carpeta.extraer_imagen(ruta)
paciente.set_imagenes(imagenes)
print(paciente.get_imagen())

img=r"D:\Programas Py\Informatica 2\Parcial 3 info 2\NIFTI\NIFTI_1\301_st2tset.nii.gz" 
img1=nilearn.image.load_img(img)
nilearn.plotting.plot_anat(img1,
                title='TC abdomen',display_mode="mosaic")

