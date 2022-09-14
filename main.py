import cv2

image1 = cv2.imread('oui.png')
image2 = cv2.imread('spaaaace.png')

#Hauteur / largeur
h, l = image1.shape[:2]
print("Largeur = {}, Hauteur = {}".format(h, l))

#Valeur RGB d'un pixel
(b, g, r) = image1[100, 100]
print("R = {}, G = {}, B = {}".format(r, g, b))

#Région d'intérêt (ROI)
roi = image1[100: 500, 200: 700]

#Redimensionnage
ratio = 800 / l
dim = (800, int(h * ratio))
redimension = cv2.resize(image1, dim)

#Rotation
center = (l // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
rotation = cv2.warpAffine(image1, matrix, (l, h))

#Dessiner un rectangle
output = image1.copy()
rectangle = cv2.rectangle(output, (10, 10), (100, 100), (255, 0, 0), 2)

#Texte
output = image1.copy()
text = cv2.putText(output, 'OpenCV Demo', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 2)

#Fusion
fusion = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow('ROI', roi)
cv2.waitKey(0)

cv2.imshow('Redimension', redimension)
cv2.waitKey(0)

cv2.imshow('Rotation', rotation)
cv2.waitKey(0)

cv2.imshow('Rectangle', rectangle)
cv2.waitKey(0)

cv2.imshow('Texte', text)
cv2.waitKey(0)

cv2.imshow('Fusion', fusion)
cv2.waitKey(0)
