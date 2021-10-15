# coding=utf-8
import cv2
import numpy as np
import random
print("将“将图像横向像素缩小至1/3，将所有像素转换为R/G/B子像素”的图还原为灰度图像\r\n")
source = input("请输入处理过的图像路径（完整路径，路径不能有中文）：")
im = cv2.imread(source)
im = cv2.resize(im,None,fx=3,fy=1,interpolation = cv2.INTER_NEAREST)#使用邻值算法，将图像横像素数扩大到3倍
imhei = im.shape[0]#获取拉伸后图像尺寸
imwid = im.shape[1]
imarr = (np.array(im))#图像转换成像素阵列
imlst = list(imarr)#阵列转换成列表
for i in range(0,imhei,1):
    for j in range(0,imwid,3):
        for k in (0,1,2):
            imlst[i][j][k] = imlst[i][j][0]
            imlst[i][j+1][k] = imlst[i][j+1][1]
            imlst[i][j+2][k] = imlst[i][j+2][2]
imarr = np.array(imlst)#列表转换回图像阵列
imarr = cv2.cvtColor(imarr,cv2.COLOR_BGR2GRAY)
cv2.imwrite(source[0:-4]+"_restored.png",imarr)
print("已将图片生成至 {}_restored.png".format(source[0:-4]))
input("按回车退出...")
