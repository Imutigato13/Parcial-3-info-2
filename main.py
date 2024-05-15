from clases import *
dic_data = {}
dic_pac = {}

def main():
    print("Bienvenido al sistema de imagenes hospitalarias".center(90, "-"))
    print("")
    while True:
        menu_1 = int(input("1.Ingresar paciente\n2.Ingresar imagen JPG o PNG\n3.Transformacion de imagen DICOM\n4.Manipulacion de imagen JPG o PNG\n5.Salir\n:"))
        try:
            if menu_1 == 1:
                ruta = input(r"Ingrese la ruta de la carpeta del paciente: ")
                ran_id = random.randint(1, 1000)
                carpeta = archivador()
                carpeta.extraer_archivos(ruta)
                nombre, id, edad = carpeta.datos_paciente()
                paciente = Paciente(nombre, edad, id)
                imagenes = carpeta.extraer_imagen(ruta)
                paciente.set_imagenes(imagenes)
                dic_pac[ran_id] = paciente
                dic_data[ran_id] = carpeta
                print("Paciente ingresado con exito con el siguiente ID: ", ran_id)
            elif menu_1 == 2:
                ruta = input(r"Ingrese la ruta de la imagen en formato JPG O PNG a subir: ")
                ran_id = random.randint(1, 1000)
                imagen_format = archivador()
                imagen_format.ingresar_imagen(ruta)
                dic_data[ran_id] = imagen_format
                print("Imagen ingresada con exito con el siguiente ID: ", ran_id)
            elif menu_1 == 3:
                id = int(input("Ingrese el ID de la carpeta DICOM: "))
                carpeta = archivador()
                carpeta.rotar_imagen(dic_data,id)
            elif menu_1 == 4:
                id = int(input("Ingrese el ID de la imagen JPG o PNG: "))
                imagen_format = archivador()
                imagen_format.binzarizacion_transformacion(dic_data,id)
            elif menu_1 == 5:
                print("Gracias por usar el sistema")
                break
            else:
                print("Opcion no valida")
        except:
            print("Error, intentelo de nuevo")
if __name__ == "__main__":
    main()