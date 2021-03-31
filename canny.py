import cv2

while True:
    name = input("file name > ")
    img = cv2.imread(name ,0)
    edges = cv2.Canny(img,100,120)

    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
