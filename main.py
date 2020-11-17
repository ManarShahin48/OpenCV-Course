import cv2
img = cv2.imread('lena.jpg',0)
print(img)

cv2.imshow('image', img)
cv2.waitKey(6000)
cv2.destroyAllWindows()


cv2.imwrite('lena_coppy.jpg',img)