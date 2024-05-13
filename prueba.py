from clases import *
img0 = cv2.imread(r'D:\Programas Py\Informatica 2\Parcial 3 info 2\datos\Imagenes JPG-PNG\Cromo.png')
img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
media=np.mean(img)
tamaño = int(input("Ingrese el tamaño del kernel: "))
kernel = np.ones((tamaño,tamaño),np.uint8)

color_texto = (255, 255, 255) if media < 128 else (0, 0, 0)
Umb,imgB=cv2.threshold(img,media,256,cv2.THRESH_BINARY)
imaOp2=cv2.morphologyEx(imgB, cv2.MORPH_OPEN, kernel, iterations = 1)

texto = (f"Imagen binarizada umbral: {int(media)} kernel: {tamaño}x{tamaño}")
altura, anchura = imaOp2.shape[:2]
cv2.putText(imaOp2, texto, (10, altura - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color_texto, 1, cv2.LINE_AA)

plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(imaOp2, cmap='gray')
plt.axis('off')

plt.show()
