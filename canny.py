import cv2

while True:
    name = input("file name > ")
    img = cv2.imread(name ,0)
    edges = cv2.Canny(img,100,120)

    invert = cv2.bitwise_not(edges)

    tmp = cv2.cvtColor(invert, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)

    cv2.imshow("Edges", dst)
    cv2.waitKey(0)
