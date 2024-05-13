from clases import *
dic_data = {}
dic_pac = {}

def main():
    print("Bienvenido al sistema de imagenes hospitalarias\n".center(90, "-"))
    while True:
        menu_1 = int(input("1.Ingresar paciente\n2.Ingresar imagen JPG o PNG\n3.Transformacion de imagen DICOM\n4.Manipulacion de imagen JPG o PNG\n5.Salir\n:"))
        if menu_1 == 1:
            ruta = input(r"Ingrese la ruta de la carpeta del paciente: ")
            ran_id = random.randint(1, 1000)
            carpeta = archivador()
            dicom = carpeta.extraer_archivos(ruta)
            nombre, id, edad = carpeta.datos_paciente()
            paciente = Paciente(nombre, edad, id)
            imagenes = carpeta.extraer_imagen(ruta)
            paciente.set_imagenes(imagenes)
            dic_pac[ran_id] = paciente
            dic_data[ran_id] = dicom
            print("Paciente ingresado con exito con el siguiente ID: ", ran_id)
        elif menu_1 == 2:
            imagen = 1
            dic_data[imagen.get_id()] = imagen
            print("Imagen ingresada con exito")
        elif menu_1 == 3:
            imagen = 2
            dic_data[imagen.get_id()] = imagen
            imagen.dicom_to_jpg()
        elif menu_1 == 4:
            imagen = 3
            dic_data[imagen.get_id()] = imagen
            imagen.show_image()
        elif menu_1 == 5:
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    main()