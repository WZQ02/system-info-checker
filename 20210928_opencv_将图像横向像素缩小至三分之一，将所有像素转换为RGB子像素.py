# coding=utf-8
import cv2
import numpy as np
import random
print("将图像横向像素缩小至1/3，将所有像素转换为R/G/B子像素\r\n")
source = input("请输入源图像路径（完整路径，路径不能有中文）：")
im = cv2.imread(source)
imhei = im.shape[0]#获取图像尺寸
imwid = im.shape[1]
togrey = input("是否去除原图色度信息？Y或1为是，其他为否")
if togrey == 'Y' or togrey == '1':
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im = cv2.cvtColor(im,cv2.COLOR_GRAY2RGB)
imarr = (np.array(im))#图像转换成像素阵列
imlst = list(imarr)#阵列转换成列表
for i in range(0,imhei,1):
    for j in range(0,int(imwid/3)*3,3):
        imlst[i][j][1] = imlst[i][j+1][1]#每横向三个像素为R1G1B1,R2G2B2,R3G3B3.先更改第一个像素,R1不动,G2传递给G1,B3传递给B1
        imlst[i][j][2] = imlst[i][j+2][2]
        imlst[i][j+1][0] = imlst[i][j][0]#后面两个像素R2G2B2,R3G3B3的值全部换成R1G1B1的
        imlst[i][j+1][1] = imlst[i][j][1]
        imlst[i][j+1][2] = imlst[i][j][2]
        imlst[i][j+2][0] = imlst[i][j][0]
        imlst[i][j+2][1] = imlst[i][j][1]
        imlst[i][j+2][2] = imlst[i][j][2]
imarr = np.array(imlst)#列表转换回图像阵列
imarr = cv2.resize(imarr,None,fx=(1/3),fy=1,interpolation = cv2.INTER_NEAREST)#使用邻值算法，将图像横像素数压回1/3
cv2.imwrite(source[0:-4]+"_processed.png",imarr)
print("已将图片生成至 {}_processed.png".format(source[0:-4]))
input("按回车退出...")
