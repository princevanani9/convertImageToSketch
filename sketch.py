
import cv2
image= cv2.imread("friends.jpeg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert= 255-grey_img
blur= cv2.GaussianBlur(invert,(21,21),0)
invertedblur = 255-blur
sketch =cv2.divide(grey_img,invertedblur,scale=256.0)
cv2.imwrite("sketch2.jpeg",sketch)
# cv2.bitwise_not(blur)