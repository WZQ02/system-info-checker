# coding=utf-8
import cv2
import numpy as np
import random
print("将图像扩大4倍并生成缩放回去就消失的随机噪点\r\n")
source = input("请输入源图像路径（完整路径，路径不能有中文）：")
im = cv2.imread(source)
imwid = im.shape[0]#获取图像尺寸
imhei = im.shape[1]
im = cv2.resize(im,None,fx=2,fy=2,interpolation = cv2.INTER_NEAREST)#使用邻值算法，将图像横纵像素数翻倍
imarr = (np.array(im))#图像转换成像素阵列
imlst = list(imarr)#阵列转换成列表
confusion = input("请指定混乱程度，0仅缩放，1为低，2为中等，3为高")
for i in range(0,imwid*2,2):
    for j in range(0,imhei*2,2):
        for k in (0,1,2):
            #imlst[i][j][k] = 63+imlst[i][j][k]*0.5#灰度处理(0-255到63-191)
            #imlst[i+1][j][k] = 63+imlst[i+1][j][k]*0.5
            #imlst[i][j+1][k] = 63+imlst[i][j+1][k]*0.5
            #imlst[i+1][j+1][k] = 63+imlst[i+1][j+1][k]*0.5
            jto0 = imlst[i][j][k]
            jto255 = 255 - imlst[i][j][k]
            jto = min(jto0,jto255)#母像素到最亮与最暗值的差的最小值jto
            if confusion == "0":
                break
            elif confusion == "1":
                s = random.randrange(0,jto+1,1)
                s2 = random.randrange(0,jto+1,1)
            elif confusion == "2":
                s = random.randrange((int((jto+1)/2)),jto+1,1)
                s2 = random.randrange((int((jto+1)/2)),jto+1,1)
            elif confusion == "3":
                s = jto
                s2 = jto
            else:
                quit()
            s3 = random.randrange(0,4,1)
            if s3 == 0:#对四个子像素进行随机变换
                #imlst[i][j][k] = 255 - imlst[i][j][k]#对任一子像素进行反转
                imlst[i][j][k] = imlst[i][j][k] + s
                imlst[i+1][j][k] = imlst[i+1][j][k] - s
                imlst[i][j+1][k] = imlst[i][j+1][k] + s2
                imlst[i+1][j+1][k] = imlst[i+1][j+1][k] - s2
            elif s3 == 1:
                #imlst[i+1][j][k] = 255 - imlst[i+1][j][k]
                imlst[i][j][k] = imlst[i][j][k] - s
                imlst[i+1][j][k] = imlst[i+1][j][k] + s
                imlst[i][j+1][k] = imlst[i][j+1][k] - s2
                imlst[i+1][j+1][k] = imlst[i+1][j+1][k] + s2
            elif s3 == 2:
                #imlst[i][j+1][k] = 255 - imlst[i][j+1][k]
                imlst[i][j][k] = imlst[i][j][k] - s
                imlst[i+1][j][k] = imlst[i+1][j][k] + s
                imlst[i][j+1][k] = imlst[i][j+1][k] + s2
                imlst[i+1][j+1][k] = imlst[i+1][j+1][k] - s2
            else:
                #imlst[i+1][j+1][k] = 255 - imlst[i+1][j+1][k]
                imlst[i][j][k] = imlst[i][j][k] + s
                imlst[i+1][j][k] = imlst[i+1][j][k] - s
                imlst[i][j+1][k] = imlst[i][j+1][k] - s2
                imlst[i+1][j+1][k] = imlst[i+1][j+1][k] + s2
imarr = np.array(imlst)#列表转换回图像阵列
cv2.imwrite(source[0:-4]+"_processed.png",imarr)
print("已将图片生成至 {}_processed.png".format(source[0:-4]))
input("按回车退出...")
