print("hello world")

print("bug aowanb uqushangke")
import numpy as np
import cv2
if __name__ =='__main__':
    img1 = cv2.imread('D:/python code/vscode/fishc.png') #颜色空间BGR

    img2 = cv2.cvtColor(img1,code = cv2.COLOR_BGR2HSV) #转变颜色空间
    #定义hsv颜色空间中蓝色的范围
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])  

    #根据蓝色的范围，标记图片中哪些位置是蓝色
    mask = cv2.inRange(img2,lower_blue,upper_blue)
    #与运算
    res  = cv2.bitwise_and(img1,img1,mask = mask)


    cv2.imshow('hsv',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #销毁释放内存