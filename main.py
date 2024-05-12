from clases import *
dic_data = {}
dic_pac = {}

def main():
    print("Bienvenido al sistema de imagenes hospitalarias".center(90, "-"))
    while True:
        menu_1 = int(input("1.Ingresar paciente\n2.Ingresar imagen JPG o PNG\n3.Transformacion de imagen DICOM\n4.Manipulacion de imagen JPG o PNG\n5.Salir\n:"))
        if menu_1 == 1:
            paciente = Paciente()
            dic_pac[paciente.get_id()] = paciente
            print("Paciente ingresado con exito")
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